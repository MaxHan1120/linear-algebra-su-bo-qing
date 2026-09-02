---
aliases:
  - 5.2 The Characteristic Polynomial
  - 特徵多項式
tags:
  - course/linear-algebra
  - linear-algebra/characteristic-polynomial
  - linear-algebra/multiplicity
---

# 5.2 The Characteristic Polynomial

> **講義範圍**
>
> `33_講義_The Characteristic Polynomial(1)`，PDF 第 1-20 頁。

## Characteristic Polynomial

對 $A\in\mathcal M_{n\times n}$，定義 characteristic polynomial

$$
p_A(t)=\det(A-tI_n).
$$

它是 degree $n$ 的 polynomial。使用 $\det(tI_n-A)$ 也是常見 convention，兩者只相差 factor $(-1)^n$，roots 完全相同。

## Eigenvalue Criterion

$\lambda$ 是 $A$ 的 eigenvalue，若且唯若

$$
p_A(\lambda)=\det(A-\lambda I_n)=0.
$$

理由是

$$
\det(A-\lambda I_n)=0
\iff
A-\lambda I_n\text{ is singular}
\iff
(A-\lambda I_n)\mathbf x=\mathbf0
$$

具有 nontrivial solution。

因此求 eigenvalues 的基本流程為：

1. 計算 $p_A(t)$。
2. 解 characteristic equation $p_A(t)=0$。
3. 對每個 root $\lambda$ 解 $(A-\lambda I_n)\mathbf x=\mathbf0$，取得 eigenspace。

## Basic Properties

- 一般而言，row-equivalent matrices 不具有相同的 characteristic polynomial，因此不可先 row reduce 再求 $p_A(t)$。
- Upper triangular matrix 的 eigenvalues 正是其 diagonal entries。
- Real matrix 的 characteristic polynomial 可能有 complex roots，因此在 $\mathbb R^n$ 中可能沒有足夠的 eigenvalues。

## Similarity Preserves the Characteristic Polynomial

若 $A$ 與 $B$ similar，即

$$
B=P^{-1}AP
$$

其中 $P$ invertible，則

$$
\det(B-tI_n)
=\det\bigl(P^{-1}(A-tI_n)P\bigr)
=\det(A-tI_n).
$$

所以 similar matrices 具有相同的 characteristic polynomial、eigenvalues 與 algebraic multiplicities。

## Characteristic Polynomial of an Operator

linear operator $T$ 的 characteristic polynomial 定義為其任一 matrix representation 的 characteristic polynomial。此定義與 basis 無關，因為不同 bases 下的 matrices 彼此 similar。

例如 $90^\circ$ rotation 的 standard matrix 為

$$
A=
\left[
\begin{array}{rr}
0&-1\cr
1&0
\end{array}
\right],
$$

故

$$
p_A(t)=t^2+1.
$$

它在 $\mathbb R$ 上沒有 roots，但在 $\mathbb C$ 上有 roots $\pm i$。

## Algebraic Multiplicity

若 $\lambda$ 是 eigenvalue，且

$$
p_A(t)=(t-\lambda)^kq(t),
\qquad
q(\lambda)\neq0,
$$

則 $k$ 稱為 $\lambda$ 的 algebraic multiplicity，記為 $m_a(\lambda)$。

## Geometric Multiplicity

eigenspace 的 dimension 稱為 geometric multiplicity：

$$
m_g(\lambda)
=\dim E_\lambda(A)
=\mathrm{nullity}(A-\lambda I_n).
$$

## Theorem 5.1

對任一 eigenvalue $\lambda$，

$$
1\leq m_g(\lambda)\leq m_a(\lambda).
$$

**Proof idea.** 令 $m_g(\lambda)=k$，取 $E_\lambda(A)$ 的 basis 並擴充成 $\mathbb R^n$ 的 basis。在此 basis 下， $A$ 的 matrix representation 左上角為 $\lambda I_k$，所以 characteristic polynomial 含有 factor $(t-\lambda)^k$。因此 algebraic multiplicity 至少為 $k$。

當 $m_a(\lambda)=1$ 時，必有 $m_g(\lambda)=1$；但當 algebraic multiplicity 大於 $1$ 時，geometric multiplicity 可能較小。

## Common Pitfalls

- Elementary row operations 不保留 characteristic polynomial。
- Algebraic multiplicity 由 polynomial 的 root multiplicity 決定；geometric multiplicity 由 eigenspace dimension 決定。
- 兩種 multiplicities 不必相等，但一定滿足 $m_g(\lambda)\leq m_a(\lambda)$。
- 使用 $\det(A-tI_n)$ 或 $\det(tI_n-A)$ 時需全程維持同一 convention。

## Assigned Exercises

Section 5.2：Problems 1, 3, 5, 7, 9, 13, 15, 17, 21, 25, 27, 29, 33, 35, 39, 41, 53, 55, 57, 59, 61, 65, 69, 71。

---

- 上一篇：[5.1 Eigenvalues and Eigenvectors](./05-01%20Eigenvalues%20and%20Eigenvectors.md)
- 下一篇：[5.3 Diagonalization of Matrices](./05-03%20Diagonalization%20of%20Matrices.md)
- 上層：[線性代數－蘇柏青](../../README.md)
