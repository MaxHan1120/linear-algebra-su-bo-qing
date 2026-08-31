# Editing Instructions

編輯本專案前，先閱讀 `CONTRIBUTING.md`。

- 所有連結與圖片必須使用標準 Markdown 相對路徑；禁止 `[[...]]` 與 `![[...]]`。
- display math 的 `$$` 必須獨立置於行首，前後保留空白行，不可縮排在 list 內。
- LaTeX alignment row break 使用 `\cr`，禁止使用 `\\`。
- display math 內禁止只有 `=` 或 `-` 的實體行。
- inline math 開頭 `$` 不可緊貼中文標點；使用 `中文標點 $...$`。
- 不得只以 Obsidian preview 判定成功；上傳前必須驗證 GitHub 實際解析。
- 完成編輯後執行 `python scripts/validate_markdown.py`。
- 上傳前執行 `python scripts/validate_markdown.py --github-render`，並確認 inline/display math 的 expected 與 rendered 數量相同、raw 數量為零。
- 只 stage 與推送本次預期修改的檔案，推送前執行 `git diff --cached --check`。
