---
aliases:
  - 6.5 Orthogonal Matrices and Operators
  - 正交矩陣與正交算子
tags:
  - course/linear-algebra
  - linear-algebra/orthogonal-matrix
  - linear-algebra/isometry
---

# 6.5 Orthogonal Matrices and Operators

> **講義範圍**
>
> `44_講義_Orthogonal Matrices and Operators`，PDF 第 1-18 頁。

## Norm-Preserving Operators

linear operator $T:\mathbb R^n\to\mathbb R^n$ 稱為 norm-preserving，若

$$
\lVert T(\mathbf u)\rVert=\lVert\mathbf u\rVert
$$

對所有 $\mathbf u\in\mathbb R^n$ 成立。Rotation 與 reflection 都是典型例子。

## Orthogonal Matrices and Operators

Square matrix $Q$ 稱為 orthogonal matrix，若其 columns 構成 $\mathbb R^n$ 的 orthonormal basis。

linear operator 稱為 orthogonal operator，若其 standard matrix 為 orthogonal matrix。

## Theorem 6.9: Equivalent Characterizations

對 $Q\in\mathcal M_{n\times n}$，下列條件等價：

1. $Q$ 是 orthogonal matrix。
2. $Q^TQ=I_n$。
3. $Q$ invertible 且 $Q^{-1}=Q^T$。
4. $Q$ preserves dot products：

$$
(Q\mathbf u)\cdot(Q\mathbf v)=\mathbf u\cdot\mathbf v.
$$

5. $Q$ preserves norms：

$$
\lVert Q\mathbf u\rVert=\lVert\mathbf u\rVert.
$$

Orthogonal matrix 的 rows 也構成 orthonormal basis，因為

$$
QQ^T=I_n.
$$

## Theorem 6.10: Algebraic Properties

若 $P,Q$ 都是 orthogonal matrices，則：

$$
\det Q=\pm1,
$$

$$
PQ\text{ is orthogonal},
$$

$$
Q^{-1}\text{ and }Q^T\text{ are orthogonal}.
$$

因此 orthogonal transformations 在 composition 與 inverse 下封閉。

## Geometric Consequences

Orthogonal operators 同時保留：

- norm；
- distance；
- dot product；
- angle；
- orthogonality。

因為

$$
\lVert Q\mathbf u-Q\mathbf v\rVert
=\lVert Q(\mathbf u-\mathbf v)\rVert
=\lVert\mathbf u-\mathbf v\rVert.
$$

## Orthogonal Matrices in $\mathbb R^2$

每個 $2\times2$ orthogonal matrix 屬於兩類之一。

### Rotation

若 $\det Q=1$，則存在 $\theta$ 使

$$
Q=
\left[
\begin{array}{rr}
\cos\theta&-\sin\theta\cr
\sin\theta&\cos\theta
\end{array}
\right].
$$

### Reflection

若 $\det Q=-1$，則 $Q$ 表示 reflection about a line through the origin。其 eigenvalues 為 $1$ 與 $-1$；eigenvalue $1$ 的 eigenspace 給出 reflection axis。

## Rigid Motions

保持 distances 的 function 稱為 rigid motion。任意 orthogonal operator 都是 rigid motion；translation

$$
F_{\mathbf b}(\mathbf v)=\mathbf v+\mathbf b
$$

也是 rigid motion，但除非 $\mathbf b=\mathbf0$，否則不是 linear。

任意 Euclidean rigid motion 可寫成 orthogonal operator 與 translation 的 composition。

## Complex Case

對 $Q\in\mathcal M_{n\times n}(\mathbb C)$，應以 conjugate transpose $Q^H$ 取代 $Q^T$。若

$$
Q^HQ=QQ^H=I_n,
$$

則稱 $Q$ 為 unitary matrix，且 $Q^{-1}=Q^H$。

## Common Pitfalls

- Orthogonal matrix 的名稱不表示 columns 只有互相 orthogonal；它們還必須是 unit vectors。
- $Q^TQ=I_n$ 已同時保證 invertibility 與 $Q^{-1}=Q^T$。
- Orthogonal matrix 的 determinant 只能是 $1$ 或 $-1$，但 determinant 為 $\pm1$ 並不足以保證 orthogonal。
- Translation preserves distance，但通常不是 linear operator。

## Assigned Exercises

Section 6.5：Problems 2, 4, 5, 8, 37, 38, 45, 47, 53。

---

- 上一篇：[6.4 Least-Squares Approximation and Orthogonal Projection Matrices](./06-04%20Least-Squares%20Approximation%20and%20Orthogonal%20Projection%20Matrices.md)
- 下一篇：[6.6 Symmetric Matrices](./06-06%20Symmetric%20Matrices.md)
- 上層：[線性代數－蘇柏青](../../README.md)
