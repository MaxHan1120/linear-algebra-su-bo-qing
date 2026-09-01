#!/usr/bin/env python3
"""Validate Markdown and LaTeX conventions used by the LA notes repository."""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


CJK_PUNCTUATION = set("、，。：；！？（）【】《》〈〉「」『』")
OBSIDIAN_LINK_RE = re.compile(r"!?\[\[")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\((?P<target>[^)]+)\)")
URL_SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
MATH_RENDERER_RE = re.compile(r"<math-renderer\b.*?</math-renderer>", re.DOTALL)
CODE_HTML_RE = re.compile(r"<(?:pre|code)\b.*?</(?:pre|code)>", re.DOTALL)
RAW_INLINE_MATH_RE = re.compile(r"(?<!\$)\$(?!\$)[^$<\r\n]*?\$(?!\$)")
RAW_DISPLAY_MATH_RE = re.compile(
    r"<p>\s*\$\$|\$\$\s*<br>|<h[1-6]>\s*\$\$", re.IGNORECASE
)
FORBIDDEN_MATH_MACRO_RE = re.compile(r"\\operatorname\b")


@dataclass
class FileMathCounts:
    inline: int = 0
    display: int = 0


def strip_inline_code(line: str) -> str:
    """Remove inline-code contents while retaining surrounding prose."""
    output: list[str] = []
    in_code = False
    index = 0
    while index < len(line):
        if line[index] == "`":
            in_code = not in_code
            output.append(" ")
        elif in_code:
            output.append(" ")
        else:
            output.append(line[index])
        index += 1
    return "".join(output)


def check_link(
    source: Path, target: str, repository_root: Path, errors: list[str], line_number: int
) -> None:
    target = target.strip().strip("<>")
    path_part = target.split("#", 1)[0].split("?", 1)[0]
    if not path_part or URL_SCHEME_RE.match(path_part):
        return

    decoded = unquote(path_part)
    if decoded.startswith("/"):
        resolved = repository_root / decoded.lstrip("/")
    else:
        resolved = source.parent / decoded

    if not resolved.resolve().exists():
        errors.append(
            f"{source.relative_to(repository_root)}:{line_number}: "
            f"relative link target does not exist: {target}"
        )


def check_file(path: Path, repository_root: Path, errors: list[str]) -> FileMathCounts:
    lines = path.read_text(encoding="utf-8").splitlines()
    counts = FileMathCounts()
    in_fence = False
    fence_marker = ""
    in_display_math = False

    for index, original_line in enumerate(lines):
        line_number = index + 1
        stripped = original_line.strip()

        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue

        if in_fence:
            continue

        macro_scan_line = strip_inline_code(original_line)
        if FORBIDDEN_MATH_MACRO_RE.search(macro_scan_line):
            errors.append(
                f"{path.relative_to(repository_root)}:{line_number}: "
                r"GitHub disallows \operatorname; use \mathrm{...} instead"
            )

        if stripped == "$$":
            if original_line != "$$":
                errors.append(
                    f"{path.relative_to(repository_root)}:{line_number}: "
                    "display-math delimiter must start at column 1"
                )

            if not in_display_math:
                counts.display += 1
                if index > 0 and lines[index - 1].strip():
                    errors.append(
                        f"{path.relative_to(repository_root)}:{line_number}: "
                        "opening $$ must have a blank line before it"
                    )
                in_display_math = True
            else:
                if index + 1 < len(lines) and lines[index + 1].strip():
                    errors.append(
                        f"{path.relative_to(repository_root)}:{line_number}: "
                        "closing $$ must have a blank line after it"
                    )
                in_display_math = False
            continue

        if in_display_math:
            if r"\\" in original_line:
                errors.append(
                    f"{path.relative_to(repository_root)}:{line_number}: "
                    r"use \cr instead of \\ inside display math"
                )
            if re.fullmatch(r"[=-]+", stripped):
                errors.append(
                    f"{path.relative_to(repository_root)}:{line_number}: "
                    "a standalone '=' or '-' line can be parsed as a Setext heading"
                )
            continue

        cleaned = strip_inline_code(original_line)

        if "$$" in cleaned:
            errors.append(
                f"{path.relative_to(repository_root)}:{line_number}: "
                "$$ must be the only content on its line"
            )

        if OBSIDIAN_LINK_RE.search(cleaned):
            errors.append(
                f"{path.relative_to(repository_root)}:{line_number}: "
                "Obsidian Wikilink syntax is not GitHub-compatible"
            )

        for match in MARKDOWN_LINK_RE.finditer(cleaned):
            check_link(path, match.group("target"), repository_root, errors, line_number)

        in_inline_math = False
        index_in_line = 0
        while index_in_line < len(cleaned):
            character = cleaned[index_in_line]
            is_escaped = index_in_line > 0 and cleaned[index_in_line - 1] == "\\"
            if character == "$" and not is_escaped:
                if index_in_line + 1 < len(cleaned) and cleaned[index_in_line + 1] == "$":
                    index_in_line += 2
                    continue
                if not in_inline_math:
                    previous = cleaned[index_in_line - 1] if index_in_line else ""
                    if previous in CJK_PUNCTUATION:
                        errors.append(
                            f"{path.relative_to(repository_root)}:{line_number}: "
                            "add a space between Chinese punctuation and opening $"
                        )
                else:
                    counts.inline += 1
                in_inline_math = not in_inline_math
            index_in_line += 1

        if in_inline_math:
            errors.append(
                f"{path.relative_to(repository_root)}:{line_number}: "
                "unbalanced inline-math delimiter"
            )

    if in_fence:
        errors.append(f"{path.relative_to(repository_root)}: unclosed fenced code block")
    if in_display_math:
        errors.append(f"{path.relative_to(repository_root)}: unclosed display-math block")

    return counts


def render_with_github(text: str) -> str:
    request = json.dumps({"text": text, "mode": "gfm"}, ensure_ascii=False)
    try:
        result = subprocess.run(
            ["gh", "api", "markdown", "--input", "-"],
            input=request,
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=False,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("GitHub CLI (gh) is required for --github-render") from exc

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "GitHub Markdown API request failed")
    return result.stdout


def check_github_render(
    path: Path,
    repository_root: Path,
    counts: FileMathCounts,
    errors: list[str],
) -> None:
    if counts.inline == 0 and counts.display == 0:
        return

    rendered_html = render_with_github(path.read_text(encoding="utf-8"))
    rendered_inline = rendered_html.count('class="js-inline-math"')
    rendered_display = rendered_html.count('class="js-display-math"')

    without_renderers = MATH_RENDERER_RE.sub("", rendered_html)
    without_code = CODE_HTML_RE.sub("", without_renderers)
    without_code = html.unescape(without_code)
    raw_inline = len(RAW_INLINE_MATH_RE.findall(without_code))
    raw_display = len(RAW_DISPLAY_MATH_RE.findall(rendered_html))

    if rendered_inline != counts.inline or raw_inline:
        errors.append(
            f"{path.relative_to(repository_root)}: GitHub inline math "
            f"rendered={rendered_inline}, expected={counts.inline}, raw={raw_inline}"
        )
    if rendered_display != counts.display or raw_display:
        errors.append(
            f"{path.relative_to(repository_root)}: GitHub display math "
            f"rendered={rendered_display}, expected={counts.display}, raw={raw_display}"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--github-render",
        action="store_true",
        help="Validate actual rendering through the GitHub Markdown API",
    )
    args = parser.parse_args()

    repository_root = Path(__file__).resolve().parents[1]
    markdown_files = sorted(repository_root.rglob("*.md"))
    errors: list[str] = []
    counts_by_file: dict[Path, FileMathCounts] = {}

    for path in markdown_files:
        counts_by_file[path] = check_file(path, repository_root, errors)

    if args.github_render and not errors:
        for path, counts in counts_by_file.items():
            check_github_render(path, repository_root, counts, errors)

    if errors:
        print("Markdown validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    inline_total = sum(count.inline for count in counts_by_file.values())
    display_total = sum(count.display for count in counts_by_file.values())
    github_status = " + GitHub render" if args.github_render else ""
    print(
        f"OK: {len(markdown_files)} Markdown files, "
        f"{inline_total} inline math, {display_total} display math{github_status}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
