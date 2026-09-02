---
aliases:
  - 6.2 Orthogonal Vectors
  - 正交向量
tags:
  - course/linear-algebra
  - linear-algebra/orthogonal-set
  - linear-algebra/gram-schmidt
---

# 6.2 Orthogonal Vectors

> **講義範圍**
>
> `39_講義_Orthogonal Vectors(1)`，PDF 第 1-17 頁。

## Orthogonal Sets

集合

$$
S=\{\mathbf v_1,\ldots,\mathbf v_k\}\subseteq\mathbb R^n
$$

稱為 orthogonal set，若所有 distinct vectors 兩兩 orthogonal：

$$
\mathbf v_i\cdot\mathbf v_j=0,
\qquad i\neq j.
$$

只含一個向量的集合依定義也是 orthogonal set。

## Theorem 6.5

不含 zero vector 的 orthogonal set 必為 linearly independent。

**Proof.** 若

$$
c_1\mathbf v_1+\cdots+c_k\mathbf v_k=\mathbf0,
$$

兩側與 $\mathbf v_i$ 做 dot product，得到

$$
c_i\lVert\mathbf v_i\rVert^2=0.
$$

因 $\mathbf v_i\neq\mathbf0$，故 $c_i=0$ 對所有 $i$ 成立。

## Orthogonal Basis and Coordinates

若 basis 同時是 orthogonal set，則稱為 orthogonal basis。若

$$
\mathcal B=\{\mathbf v_1,\ldots,\mathbf v_k\}
$$

是 subspace $V$ 的 orthogonal basis，則對任意 $\mathbf u\in V$，

$$
\mathbf u
=\sum_{i=1}^k
\frac{\mathbf u\cdot\mathbf v_i}
{\lVert\mathbf v_i\rVert^2}\mathbf v_i.
$$

因此 coordinate coefficients 可直接由 dot products 取得，不必解一般 linear system。

## Gram-Schmidt Process

令 $\{\mathbf u_1,\ldots,\mathbf u_k\}$ 是 subspace $W$ 的 basis。定義

$$
\mathbf v_1=\mathbf u_1,
$$

以及對 $j\geq2$，

$$
\mathbf v_j
=\mathbf u_j
-\sum_{i=1}^{j-1}
\frac{\mathbf u_j\cdot\mathbf v_i}
{\lVert\mathbf v_i\rVert^2}\mathbf v_i.
$$

則 $\{\mathbf v_1,\ldots,\mathbf v_k\}$ 是 $W$ 的 orthogonal basis，且對每個 $j$，

$$
\mathrm{Span}\{\mathbf v_1,\ldots,\mathbf v_j\}
=\mathrm{Span}\{\mathbf u_1,\ldots,\mathbf u_j\}.
$$

每一步都是從 $\mathbf u_j$ 減去它在既有 orthogonal directions 上的 projections。

## Orthonormal Basis

Unit vector 滿足 $\lVert\mathbf w\rVert=1$。把 orthogonal basis 中每個向量 normalize：

$$
\mathbf w_i=\frac{\mathbf v_i}{\lVert\mathbf v_i\rVert},
$$

即可得到 orthonormal basis。

若 $\mathcal B=\{\mathbf w_1,\ldots,\mathbf w_k\}$ 是 $V$ 的 orthonormal basis，則

$$
\mathbf u
=\sum_{i=1}^k(\mathbf u\cdot\mathbf w_i)\mathbf w_i,
\qquad \mathbf u\in V,
$$

且

$$
[\mathbf u]_{\mathcal B}=
\left[
\begin{array}{c}
\mathbf u\cdot\mathbf w_1\cr
\vdots\cr
\mathbf u\cdot\mathbf w_k
\end{array}
\right].
$$

## Practical Workflow

1. 先確認輸入向量是 L.I.。
2. 依既定順序執行 Gram-Schmidt。
3. 必要時乘 nonzero scalars 簡化 entries。
4. 最後 normalize 得到 orthonormal basis。
5. 以 pairwise dot products 與 unit norms 驗證結果。

## Common Pitfalls

- Orthogonal set 若包含 zero vector，不一定 L.I.。
- Gram-Schmidt 的 projection denominator 是前一步 $\mathbf v_i$ 的 squared norm。
- 改變輸入 basis 的順序通常會得到不同的 orthogonal basis，但 span 相同。
- Orthonormal 同時要求 pairwise orthogonal 與 unit norm。

## Assigned Exercises

Section 6.2：Problems 5, 8, 9, 14, 16, 53, 54, 55。

---

- 上一篇：[6.1 The Geometry of Vectors](./06-01%20The%20Geometry%20of%20Vectors.md)
- 下一篇：[6.3 Orthogonal Projections](./06-03%20Orthogonal%20Projections.md)
- 上層：[線性代數－蘇柏青](../../README.md)
