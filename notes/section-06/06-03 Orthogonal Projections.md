---
aliases:
  - 6.3 Orthogonal Projections
  - 正交投影
tags:
  - course/linear-algebra
  - linear-algebra/orthogonal-complement
  - linear-algebra/projection
---

# 6.3 Orthogonal Projections

> **講義範圍**
>
> `42_講義_Orthogonal Projections(1)`，PDF 第 1-22 頁。

## Orthogonal Complement

對 nonempty subset $S\subseteq\mathbb R^n$，定義

$$
S^\perp
=\{\mathbf v\in\mathbb R^n:
\mathbf v\cdot\mathbf u=0
\text{ for every }\mathbf u\in S\}.
$$

$S^\perp$ 是 $\mathbb R^n$ 的 subspace，並有

$$
\{\mathbf0\}^\perp=\mathbb R^n,
\qquad
(\mathbb R^n)^\perp=\{\mathbf0\}.
$$

若 $W$ 是 subspace，且 $\mathcal B$ 是 $W$ 的 basis，則

$$
W^\perp=\mathcal B^\perp,
\qquad
(W^\perp)^\perp=W.
$$

## Matrix Subspaces and Orthogonal Complements

對任意 real matrix $A$：

$$
(\mathrm{Row}(A))^\perp=\mathrm{Null}(A),
$$

$$
(\mathrm{Col}(A))^\perp=\mathrm{Null}(A^T).
$$

第一式源自

$$
A\mathbf x=\mathbf0
$$

恰表示 $\mathbf x$ 與 $A$ 的每一個 row orthogonal。

## Theorem 6.7: Orthogonal Decomposition Theorem

若 $W\subseteq\mathbb R^n$ 是 subspace，則每個 $\mathbf u\in\mathbb R^n$ 都可唯一分解為

$$
\mathbf u=\mathbf w+\mathbf z,
\qquad
\mathbf w\in W,
\quad
\mathbf z\in W^\perp.
$$

若 $\{\mathbf v_1,\ldots,\mathbf v_k\}$ 是 $W$ 的 orthonormal basis，則

$$
\mathbf w
=\sum_{i=1}^k
(\mathbf u\cdot\mathbf v_i)\mathbf v_i,
$$

$$
\mathbf z=\mathbf u-\mathbf w.
$$

唯一性來自

$$
W\cap W^\perp=\{\mathbf0\}.
$$

因此

$$
\mathbb R^n=W\mathbin{\oplus}W^\perp,
\qquad
\dim W+\dim W^\perp=n.
$$

## Orthogonal Projection Operator

$\mathbf u$ onto $W$ 的 orthogonal projection 定義為上述 decomposition 中唯一的 $\mathbf w$，記為

$$
\mathrm{proj}_W(\mathbf u).
$$

Projection operator

$$
U_W:\mathbb R^n\to\mathbb R^n,
\qquad
U_W(\mathbf u)=\mathrm{proj}_W(\mathbf u)
$$

是 linear transformation。

## Projection Matrix

$U_W$ 的 standard matrix 稱為 orthogonal projection matrix，記為 $P_W$。

若 $Q=[\mathbf v_1\ \cdots\ \mathbf v_k]$ 的 columns 是 $W$ 的 orthonormal basis，則

$$
P_W=QQ^T.
$$

## Theorem 6.8

令 $C\in\mathcal M_{n\times k}$ 的 columns 是 $W$ 的任意 basis，則 $C^TC$ invertible，且

$$
P_W=C(C^TC)^{-1}C^T.
$$

**Proof idea.** 因 $\mathbf w=C\mathbf a$ 且 residual $\mathbf u-C\mathbf a\in W^\perp$，故

$$
C^T(\mathbf u-C\mathbf a)=\mathbf0.
$$

所以

$$
C^TC\mathbf a=C^T\mathbf u,
\qquad
\mathbf a=(C^TC)^{-1}C^T\mathbf u.
$$

## Properties of an Orthogonal Projection Matrix

$$
P_W^T=P_W,
\qquad
P_W^2=P_W.
$$

此外，

$$
\mathrm{Col}(P_W)=W,
\qquad
\mathrm{Null}(P_W)=W^\perp.
$$

## Closest Vector Property

在 $W$ 的所有向量中， $\mathrm{proj}_W(\mathbf u)$ 是與 $\mathbf u$ 距離最短的唯一向量。

若 $\mathbf w=\mathrm{proj}_W(\mathbf u)$ 且 $\mathbf w'\in W$，則

$$
\lVert\mathbf u-\mathbf w'\rVert^2
=\lVert\mathbf u-\mathbf w\rVert^2
+\lVert\mathbf w-\mathbf w'\rVert^2.
$$

因此

$$
d(\mathbf u,W)
=\lVert\mathbf u-\mathrm{proj}_W(\mathbf u)\rVert.
$$

## Common Pitfalls

- $W^\perp$ 必須通過原點；外觀上垂直但平移過的 affine set 不是 orthogonal complement。
- $(\mathrm{Row}(A))^\perp$ 對應 $\mathrm{Null}(A)$； $(\mathrm{Col}(A))^\perp$ 對應 $\mathrm{Null}(A^T)$。
- 只有 basis matrix $C$ 具有 L.I. columns 時， $C^TC$ 才保證 invertible。
- Projection vector 位於 $W$；residual 位於 $W^\perp$。

## Assigned Exercises

Section 6.3：Problems 2, 4, 5, 9, 11, 14, 21, 22, 24, 58, 62, 65-67, 71, 72, 75, 79, 82。

---

- 上一篇：[6.2 Orthogonal Vectors](./06-02%20Orthogonal%20Vectors.md)
- 下一篇：[6.4 Least-Squares Approximation and Orthogonal Projection Matrices](./06-04%20Least-Squares%20Approximation%20and%20Orthogonal%20Projection%20Matrices.md)
- 上層：[線性代數－蘇柏青](../../README.md)
