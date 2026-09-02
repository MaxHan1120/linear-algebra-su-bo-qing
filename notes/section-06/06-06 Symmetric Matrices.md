---
aliases:
  - 6.6 Symmetric Matrices
  - 對稱矩陣
tags:
  - course/linear-algebra
  - linear-algebra/symmetric-matrix
  - linear-algebra/spectral-theorem
---

# 6.6 Symmetric Matrices

> **講義範圍**
>
> `45_講義_Symmetric Matrices(1)`，PDF 第 1-21 頁。

## Symmetric Matrices

Real square matrix $A$ 稱為 symmetric，若

$$
A^T=A.
$$

Symmetry 對 eigenvalues、eigenvectors 與 diagonalization 帶來比一般 matrices 更強的結構。

## Real Eigenvalues

Real symmetric matrix 的所有 eigenvalues 都是 real。

即使先允許 complex eigenvector $\mathbf x$，由

$$
A\mathbf x=\lambda\mathbf x
$$

與 $A^H=A$ 可得 Rayleigh quotient

$$
\lambda
=\frac{\mathbf x^HA\mathbf x}{\mathbf x^H\mathbf x}
$$

為 real number。

## Theorem 6.14

若 $A$ symmetric，則對應於 distinct eigenvalues 的 eigenvectors 彼此 orthogonal。

**Proof.** 若

$$
A\mathbf u=\lambda\mathbf u,
\qquad
A\mathbf v=\mu\mathbf v,
\qquad
\lambda\neq\mu,
$$

則

$$
\lambda(\mathbf u\cdot\mathbf v)
=(A\mathbf u)\cdot\mathbf v
=\mathbf u\cdot(A^T\mathbf v)
=\mu(\mathbf u\cdot\mathbf v).
$$

因此 $(\lambda-\mu)(\mathbf u\cdot\mathbf v)=0$，故 $\mathbf u\cdot\mathbf v=0$。

## Theorem 6.15: Spectral Theorem

對 real matrix $A$，下列條件等價：

1. $A$ symmetric。
2. $\mathbb R^n$ 存在由 $A$ 的 eigenvectors 組成的 orthonormal basis。
3. 存在 orthogonal matrix $P$ 與 real diagonal matrix $D$，使

$$
P^TAP=D.
$$

等價地，

$$
A=PDP^T.
$$

這稱為 orthogonal diagonalization。相較一般 diagonalization，inverse 可直接寫成 transpose。

## Orthogonal Diagonalization Procedure

1. 求出所有 distinct eigenvalues $\lambda_1,\ldots,\lambda_k$。
2. 求出 eigenspaces $E_{\lambda_1},\ldots,E_{\lambda_k}$。
3. 在每個 eigenspace 內使用 Gram-Schmidt，取得 orthonormal basis。
4. 合併各 eigenspace bases，依序放入 $P$ 的 columns。
5. 將對應 eigenvalues 依相同順序放入 $D$。
6. 驗證 $P^TAP=D$。

Distinct eigenspaces 已互相 orthogonal，因此只需在各 eigenspace 內部執行 Gram-Schmidt。

## Quadratic Forms

Symmetric matrix $A$ 對應 quadratic form

$$
q(\mathbf x)=\mathbf x^TA\mathbf x.
$$

若 $A=PDP^T$ 且 $\mathbf x=P\mathbf y$，則

$$
q(\mathbf x)
=\mathbf y^TD\mathbf y
=\lambda_1y_1^2+\cdots+\lambda_ny_n^2.
$$

Orthogonal change of coordinates 可消去 cross terms，並用 eigenvalues 判斷 conic 或 quadric 的幾何類型。

## Theorem 6.16: Spectral Decomposition

令 $\mathbf u_1,\ldots,\mathbf u_n$ 是 $A$ 的 orthonormal eigenbasis，對應 eigenvalues 為 $\lambda_1,\ldots,\lambda_n$。則

$$
A
=\sum_{i=1}^n
\lambda_i\mathbf u_i\mathbf u_i^T.
$$

令

$$
P_i=\mathbf u_i\mathbf u_i^T,
$$

則 $P_i$ 是投影至 $\mathrm{Span}\{\mathbf u_i\}$ 的 rank-one orthogonal projection matrix，且

$$
P_i^2=P_i,
\qquad
P_iP_j=O\quad(i\neq j).
$$

因此

$$
A=\lambda_1P_1+\cdots+\lambda_nP_n.
$$

## Complex Analogue

Complex matrix 滿足 $A^H=A$ 時稱為 Hermitian。Hermitian matrix 具有 real eigenvalues，distinct eigenspaces mutually orthogonal，且可由 unitary matrix diagonalize。

## Common Pitfalls

- 一般 diagonalizable matrix 不一定能 orthogonally diagonalize；real matrix 能 orthogonally diagonalize 若且唯若 symmetric。
- Repeated eigenvalue 的 eigenspace 內仍需 orthonormalize basis。
- $P^TAP=D$ 等價於 $A=PDP^T$，因 $P^{-1}=P^T$。
- Spectral decomposition 中 $\mathbf u_i$ 必須為 unit eigenvectors。

## Assigned Exercises

Section 6.6：Problems 15, 18, 19, 21, 23, 25, 43, 47, 48, 55, 56, 59, 61, 64。

---

- 上一篇：[6.5 Orthogonal Matrices and Operators](./06-05%20Orthogonal%20Matrices%20and%20Operators.md)
- 下一篇：[7.1 Vector Spaces and Their Subspaces](../section-07/07-01%20Vector%20Spaces%20and%20Their%20Subspaces.md)
- 上層：[線性代數－蘇柏青](../../README.md)
