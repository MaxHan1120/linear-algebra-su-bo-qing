---
aliases:
  - 5.3 Diagonalization of Matrices
  - 矩陣對角化
tags:
  - course/linear-algebra
  - linear-algebra/diagonalization
  - linear-algebra/eigenbasis
---

# 5.3 Diagonalization of Matrices

> **講義範圍**
>
> `36_講義_Diagonalization of Matrices(1)`，PDF 第 1-18 頁。

## Diagonalizable Matrices

$A\in\mathcal M_{n\times n}$ 稱為 diagonalizable，若存在 invertible matrix $P$ 與 diagonal matrix $D$，使得

$$
A=PDP^{-1}.
$$

此時

$$
A^m=PD^mP^{-1},
$$

而 $D^m$ 只需將 diagonal entries 各自取 $m$ 次方，因此 diagonalization 特別適合計算高次矩陣乘冪與離散動態系統。

並非每個 square matrix 都可 diagonalize。例如 nonzero nilpotent matrix

$$
\left[
\begin{array}{cc}
0&1\cr
0&0
\end{array}
\right]
$$

不能 diagonalize。

## Theorem 5.2: Diagonalization Criterion

$A$ diagonalizable，若且唯若 $\mathbb R^n$ 存在一組由 $A$ 的 eigenvectors 組成的 basis。

更具體地，若

$$
P=[\mathbf p_1\ \mathbf p_2\ \cdots\ \mathbf p_n]
$$

invertible，且

$$
D=\mathrm{diag}(\lambda_1,\ldots,\lambda_n),
$$

則

$$
A=PDP^{-1}
$$

若且唯若

$$
A\mathbf p_i=\lambda_i\mathbf p_i,
\qquad i=1,\ldots,n.
$$

因此 $P$ 的 columns 是 eigenvectors， $D$ 的 diagonal entries 必須按相同順序放置其對應 eigenvalues。

## Diagonalization Procedure

1. Factor $p_A(t)$ 並列出 $n$ 個 eigenvalues，重根依 algebraic multiplicity 重複計數。
2. 對每個 $\lambda$ 求 $E_\lambda(A)=\mathrm{Null}(A-\lambda I_n)$ 的 basis。
3. 檢查所有 eigenspace bases 合計是否提供 $n$ 個 L.I. eigenvectors。
4. 依序把 eigenvectors 放入 $P$，並把對應 eigenvalues 放入 $D$。
5. 驗證 $AP=PD$ 或 $A=PDP^{-1}$。

## Theorem 5.3

對應於 distinct eigenvalues 的 eigenvectors 為 linearly independent。

**Proof idea.** 假設 $\mathbf v_1,\ldots,\mathbf v_m$ 對應 distinct eigenvalues $\lambda_1,\ldots,\lambda_m$ 且為 L.D.。取最早可由前面向量表示的 $\mathbf v_k$，對該關係作用 $A$，再減去 $\lambda_k$ 倍的原關係，便得到前 $k-1$ 個向量的非平凡線性關係，與最小性矛盾。

### Corollaries

- 從不同 eigenspaces 各取 L.I. sets，所有向量的 union 仍為 L.I.。
- 若 $A$ 有 $n$ 個 distinct eigenvalues，則 $A$ 必為 diagonalizable。

## Complete Test for Diagonalizability over $\mathbb R$

$A\in\mathcal M_{n\times n}$ 可在 $\mathbb R$ 上 diagonalize，若且唯若：

1. $p_A(t)$ 在 $\mathbb R$ 上可完全分解成 linear factors；
2. 對每個 eigenvalue $\lambda$，

$$
m_g(\lambda)=m_a(\lambda).
$$

等價地，所有 eigenspaces 的 dimensions 總和為 $n$。

若允許 complex eigenvalues，條件 1 對 complex matrices 自動成立；但條件 2 仍可能失敗。

## Similarity Interpretation

Diagonalization 正是尋找一組 eigenbasis $\mathcal B$，使 linear operator 的 matrix representation 成為 diagonal matrix：

$$
[T]_{\mathcal B}=D,
\qquad
A=PDP^{-1}.
$$

在 eigenbasis 中，每個 coordinate direction 都獨立地乘上一個 eigenvalue。

## Common Pitfalls

- 有 $n$ 個 eigenvalues（含重複計數）不代表一定有 $n$ 個 L.I. eigenvectors。
- $P$ 中 eigenvectors 的順序必須與 $D$ 中 eigenvalues 的順序一致。
- Algebraic multiplicity 與 geometric multiplicity 不相等時，矩陣不可 diagonalize。
- 只在指定 scalar field 上判斷；有 complex eigenvalues 的 real matrix 可能無法在 $\mathbb R$ 上 diagonalize。

## Assigned Exercises

Section 5.3：Problems 1, 3, 5, 9, 13, 17, 29, 31, 33, 35, 41, 43, 47。

---

- 上一篇：[5.2 The Characteristic Polynomial](./05-02%20The%20Characteristic%20Polynomial.md)
- 下一篇：[6.1 The Geometry of Vectors](../section-06/06-01%20The%20Geometry%20of%20Vectors.md)
- 上層：[線性代數－蘇柏青](../../README.md)
