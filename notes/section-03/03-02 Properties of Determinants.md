---
aliases:
  - 3.2 Properties of Determinants
  - 行列式的性質
tags:
  - course/linear-algebra
  - linear-algebra/determinant
  - linear-algebra/row-operations
---

# 3.2 Properties of Determinants

> **講義範圍**
>
> `24_講義_Determinants(1)(2)`，PDF 第 1-17 頁。

## Notation

- $A,B\in\mathcal M_{n\times n}$。
- $E$ 表示 $n\times n$ elementary matrix。
- 若 Gaussian elimination 將 $A$ 化為 upper triangular matrix $U$，以 $r$ 表示過程中 row interchanges 的次數。
- minor、cofactor 與 $\det(A)$ 的定義沿用 [3.1 Cofactor Expansion](./03-01%20Cofactor%20Expansion.md)。

## Theorem 3.3: Determinants and Row Operations

令 $B$ 由 $A$ 經一次 elementary row operation 得到。

### (a) Row Interchange

若交換 $A$ 的兩個 rows，則

$$
\det(B)=-\det(A).
$$

因此每次 row interchange 都使 determinant 改變 sign。

### (b) Row Scaling

若將某個 row 乘以 scalar $k$，則

$$
\det(B)=k\det(A).
$$

特別地，從某一 row 提出 factor $k$，determinant 也會提出相同 factor。

### (c) Row Replacement

若將某個 row 的 $k$ 倍加到另一個不同的 row，則

$$
\det(B)=\det(A).
$$

這是利用 Gaussian elimination 計算 determinant 時最重要的性質：row replacement 不改變 determinant。

### (d) Elementary Matrices

對任意 elementary matrix $E$，

$$
\det(EA)=\det(E)\det(A).
$$

三類 elementary matrices 的 determinants 分別為：

| Row operation | $\det(E)$ |
|---|---:|
| interchange two rows | $-1$ |
| multiply one row by $k$ | $k$ |
| add a multiple of one row to another | $1$ |

## Repeated or Zero Rows

若 $A$ 有兩個 identical rows，交換這兩列不會改變矩陣，但依 Theorem 3.3(a) determinant 應改變 sign，因此

$$
\det(A)=-\det(A)
\implies
\det(A)=0.
$$

若 $A$ 有 zero row，也可由任意 row scaling 推得 $\det(A)=0$。

## Computing a Determinant by Gaussian Elimination

若只使用 row replacement 與 row interchange，將 $A$ 化為 upper triangular matrix $U=[u_{ij}]$，則

$$
\det(A)=(-1)^r\det(U)
=(-1)^r u_{11}u_{22}\cdots u_{nn}.
$$

若 elimination 過程另有 row scaling，必須把相應 scaling factors 一併補回，不可直接只乘 $U$ 的 diagonal entries。

### Workflow

1. 用 row replacement 在 pivot 下方製造 zeros。
2. 必要時交換 rows，並記錄交換次數 $r$。
3. 若縮放 row，另外記錄 scaling factor。
4. 對所得 triangular matrix 取 diagonal product，再依前述 factors 修正。

對 dense matrices，此方法通常遠快於 cofactor expansion。

## Singularity Criterion

對任意 $A\in\mathcal M_{n\times n}$，

$$
A\text{ is singular}
\iff
\det(A)=0.
$$

equivalently，

$$
A\text{ is invertible}
\iff
\det(A)\ne0.
$$

理由是 $A$ singular 恰好表示其 row echelon form 有 zero row；因此 triangular form 的 diagonal product 為 zero。

## Theorem 3.4: Fundamental Properties

令 $A,B\in\mathcal M_{n\times n}$。

### (a) Invertibility

$$
A\text{ is invertible}
\iff
\det(A)\ne0.
$$

這使 determinant 成為 square matrix invertibility 的 scalar test。

### (b) Product Rule

$$
\det(AB)=\det(A)\det(B).
$$

**Proof idea.** 若 $A$ 可逆，將 $A$ 寫成 elementary matrices 的乘積，再反覆使用 Theorem 3.3(d)。若 $A$ singular，則 $AB$ 也 singular，等式兩側皆為 zero。

由 product rule 可得

$$
\det(A^k)=\det(A)^k
$$

對所有正整數 $k$ 成立。

### (c) Transpose

$$
\det(A^T)=\det(A).
$$

因此所有 row-operation properties 都有對應的 column-operation versions，也可以沿任意 column 做 cofactor expansion：

$$
\det(A)=a_{1j}c_{1j}+a_{2j}c_{2j}+\cdots+a_{nj}c_{nj}.
$$

### (d) Inverse

若 $A$ 可逆，則

$$
\det(A^{-1})=\frac{1}{\det(A)}.
$$

因為

$$
1=\det(I_n)=\det(AA^{-1})
=\det(A)\det(A^{-1}).
$$

## Block Triangular Matrices

若 $A\in\mathcal M_{m\times m}$、 $C\in\mathcal M_{n\times n}$，且 block dimensions 相容，則

$$
M=
\left[
\begin{array}{cc}
A&B\cr
0&C
\end{array}
\right]
$$

是 block upper triangular matrix，並且

$$
\det(M)=\det(A)\det(C).
$$

同理，block lower triangular matrix 的 determinant 也是 diagonal blocks determinants 的乘積。

## Determinant Is Not Additive

一般而言，

$$
\det(A+B)\ne\det(A)+\det(B).
$$

例如

$$
A=
\left[
\begin{array}{cc}
1&0\cr
0&0
\end{array}
\right],
\qquad
B=
\left[
\begin{array}{cc}
0&0\cr
0&1
\end{array}
\right].
$$

則 $\det(A)=\det(B)=0$，但 $A+B=I_2$，所以 $\det(A+B)=1$。

## Parameter-Dependent Invertibility

若矩陣含 parameter $c$，可將其視為 symbolic matrix 並計算 $\det(A(c))$。由 Theorem 3.4(a)，

$$
A(c)\text{ is invertible}
\iff
\det(A(c))\ne0.
$$

因此先找出使 determinant 為 zero 的 parameters，即可得到所有 singular cases。

## Common Pitfalls

- row interchange 使 determinant 乘以 $-1$，不是維持不變。
- row scaling 會同步 scaling determinant；只有 row replacement 不改變 determinant。
- $\det(AB)$ 有乘法性，但 $\det(A+B)$ 沒有加法性。
- $\det(A^T)=\det(A)$，不是 $-\det(A)$。
- 只有在 $A$ 可逆時， $\det(A^{-1})$ 才有意義。

## Assigned Exercises

Section 3.2：Problems 7, 13, 22, 36, 39-44。

---

- 上一篇：[3.1 Cofactor Expansion](./03-01%20Cofactor%20Expansion.md)
- 下一篇：[4.1 Subspaces](../section-04/04-01%20Subspaces.md)
- 上層：[線性代數－蘇柏青](../../README.md)
