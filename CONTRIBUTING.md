# GitHub-Compatible Markdown and LaTeX Guide

本專案的筆記必須同時能在 Obsidian 與 GitHub 正確顯示。編輯後、上傳前，請遵守以下規則並執行驗證腳本。

## Links and Images

- 使用標準 Markdown 相對連結，不使用 Obsidian Wikilink。
- 檔名含空格時，在連結路徑中使用 `%20`。
- 圖片使用標準 Markdown image syntax，並保留在筆記同層的 `_attachments/<note-name>_image/`。

```md
[1.1 Matrices and Vectors](./01-01%20Matrices%20and%20Vectors.md)
![Rotation matrix](./_attachments/example_image/rotation.png)
```

禁止：

```md
[[01-01 Matrices and Vectors]]
![[rotation.png]]
```

## Display Math

1. `$$` 必須單獨佔一行、位於行首，且數學區塊前後須有空白行。
2. 不要把 display math 縮排在 Markdown list 內；應將公式退出 list indentation。
3. 矩陣、`aligned`、`cases` 等環境的換列使用 `\cr`，不要使用 `\\`。GitHub Markdown 會在數學渲染前處理雙反斜線，使 `\\` 變成錯誤的單反斜線。
4. display math 內不要出現只有 `=` 或 `-` 的實體行，否則可能被 GFM 誤判為 Setext heading。
5. GitHub 會拒絕 `\operatorname` macro；矩陣運算名稱統一使用 `\mathrm{rref}`、`\mathrm{rank}`、`\mathrm{nullity}`。

建議：

```md
前文。

$$
\mathbf v=
\begin{bmatrix}
v_1\cr
v_2\cr
\vdots\cr
v_n
\end{bmatrix}.
$$

後文。
```

## Inline Math

inline math 的開頭 `$` 前面若是中文文字或中文標點，應保留一個空格。公式結尾後可以直接接中文標點。

```md
因此， $A\mathbf v$ 有定義。
表示為： $\mathbf b$。
若 $m=n$，則稱為方陣。
```

避免：

```md
因此，$A\mathbf v$ 有定義。
表示為：$\mathbf b$。
```

已知會影響 GitHub inline-math 邊界判定的中文標點包含 `、，。：；！？（）`。本專案統一採用「標點後空一格再開啟 `$`」的寫法。

## Validation

本地靜態檢查：

```powershell
python scripts/validate_markdown.py
```

上傳前再使用 GitHub Markdown API 驗證實際渲染：

```powershell
python scripts/validate_markdown.py --github-render
```

驗證必須通過後才能提交。GitHub Actions 也會在 Markdown 或驗證腳本變更時自動執行靜態檢查。
