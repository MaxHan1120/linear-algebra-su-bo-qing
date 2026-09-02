---
aliases:
  - 7.5 Inner Product Spaces
  - 內積空間
tags:
  - course/linear-algebra
  - linear-algebra/inner-product-space
  - linear-algebra/least-squares-approximation
---

# 7.5 Inner Product Spaces

> **講義範圍**
>
> `64_講義_Inner Product Spaces(1)`，PDF 第 1-24 頁。

## Inner Product

令 $V$ 是 real vector space。Function

$$
\langle\cdot,\cdot\rangle:V\times V\to\mathbb R
$$

稱為 inner product，若對所有 $\mathbf u,\mathbf v,\mathbf w\in V$ 與 $c\in\mathbb R$ 滿足：

1. Positive definiteness：

$$
\langle\mathbf u,\mathbf u\rangle\geq0,
\qquad
\langle\mathbf u,\mathbf u\rangle=0
\iff\mathbf u=\mathbf0.
$$

2. Symmetry：

$$
\langle\mathbf u,\mathbf v\rangle
=\langle\mathbf v,\mathbf u\rangle.
$$

3. Additivity：

$$
\langle\mathbf u+\mathbf v,\mathbf w\rangle
=\langle\mathbf u,\mathbf w\rangle
+\langle\mathbf v,\mathbf w\rangle.
$$

4. Homogeneity：

$$
\langle c\mathbf u,\mathbf v\rangle
=c\langle\mathbf u,\mathbf v\rangle.
$$

具有指定 inner product 的 vector space 稱為 inner product space。同一 vector space 可以定義多種 inner products。

## Examples

### Euclidean Inner Product

在 $\mathbb R^n$：

$$
\langle\mathbf u,\mathbf v\rangle
=\mathbf u^T\mathbf v.
$$

### Integral Inner Product

在 $C([a,b])$：

$$
\langle f,g\rangle
=\int_a^b f(t)g(t)\,dt.
$$

### Frobenius Inner Product

對同尺寸 real matrices：

$$
\langle A,B\rangle_F
=\mathrm{tr}(AB^T)
=\sum_{i,j}a_{ij}b_{ij}.
$$

## Norm and Distance

由 inner product induced 的 norm 與 distance 為

$$
\lVert\mathbf v\rVert
=\sqrt{\langle\mathbf v,\mathbf v\rangle},
$$

$$
d(\mathbf u,\mathbf v)
=\lVert\mathbf u-\mathbf v\rVert.
$$

Frobenius norm 因此為

$$
\lVert A\rVert_F
=\sqrt{\sum_{i,j}a_{ij}^2}.
$$

## Fundamental Inequalities

所有 inner product spaces 都滿足 Pythagorean theorem：若

$$
\langle\mathbf u,\mathbf v\rangle=0,
$$

則

$$
\lVert\mathbf u+\mathbf v\rVert^2
=\lVert\mathbf u\rVert^2+\lVert\mathbf v\rVert^2.
$$

Cauchy-Schwarz inequality：

$$
|\langle\mathbf u,\mathbf v\rangle|
\leq\lVert\mathbf u\rVert\lVert\mathbf v\rVert.
$$

Triangle inequality：

$$
\lVert\mathbf u+\mathbf v\rVert
\leq\lVert\mathbf u\rVert+\lVert\mathbf v\rVert.
$$

## Orthogonality

$\mathbf u$ 與 $\mathbf v$ orthogonal，若

$$
\langle\mathbf u,\mathbf v\rangle=0.
$$

Orthogonal set 中所有 distinct vectors 兩兩 orthogonal；若再要求每個 vector 的 norm 為 $1$，則稱為 orthonormal set。

不含 zero vector 的 orthogonal set 必為 L.I.，此結果也適用於 infinite sets。

## Gram-Schmidt in an Inner Product Space

對 basis $\{\mathbf u_1,ldots,\mathbf u_k\}$，定義

$$
\mathbf v_1=\mathbf u_1,
$$

$$
\mathbf v_j
=\mathbf u_j
-\sum_{i=1}^{j-1}
\frac{\langle\mathbf u_j,\mathbf v_i\rangle}
{\lVert\mathbf v_i\rVert^2}\mathbf v_i.
$$

即可得到 orthogonal basis；再 normalize 可得 orthonormal basis。因此每個 finite-dimensional inner product space 都有 orthonormal basis。

例如在 $\mathcal P_2$ 上定義

$$
\langle f,g\rangle
=\int_{-1}^{1}f(x)g(x)\,dx,
$$

對 $\{1,x,x^2\}$ 執行 Gram-Schmidt，可得到 Legendre-polynomial 型的 orthogonal basis。

## Orthogonal Projection

令 $W$ 是 finite-dimensional subspace，且 $\{\mathbf w_1,ldots,\mathbf w_k\}$ 是其 orthonormal basis。對每個 $\mathbf v\in V$，存在唯一分解

$$
\mathbf v=\mathbf w+\mathbf z,
\qquad
\mathbf w\in W,
\quad
\mathbf z\in W^\perp,
$$

其中

$$
\mathbf w
=\mathrm{proj}_W(\mathbf v)
=\sum_{i=1}^k
\langle\mathbf v,\mathbf w_i\rangle\mathbf w_i.
$$

$\mathbf w$ 是 $W$ 中距離 $\mathbf v$ 最近的唯一向量，因此也稱為 least-squares approximation。

## Trigonometric Approximation

在 $C([0,2\pi])$ 上使用 integral inner product，trigonometric system

$$
1,\cos t,\sin t,\cos2t,\sin2t,\ldots
$$

是 orthogonal set。將 periodic function 投影到

$$
W_n
=\mathrm{Span}\{1,\cos t,\sin t,\ldots,\cos nt,\sin nt\}
$$

可得到 degree $n$ 的 trigonometric least-squares approximation，亦即有限 Fourier approximation。

## Complex Inner Product Spaces

在 complex vector space 中，inner product 應為 conjugate symmetric：

$$
\langle\mathbf u,\mathbf v\rangle
=\overline{\langle\mathbf v,\mathbf u\rangle},
$$

並在其中一個 argument 上 conjugate-linear。對 $\mathbb C^n$ 的標準選擇為 $\mathbf u^H\mathbf v$。

## Common Pitfalls

- Inner product 是額外指定的 structure；同一 vector space 可有不同的 notions of length 與 orthogonality。
- Integral inner product 的 integration interval 是定義的一部分。
- Projection formula 使用 orthonormal basis 時才沒有 squared-norm denominators。
- 在 complex spaces 中不能使用 ordinary transpose 取代 conjugate transpose。

## Assigned Exercises

Section 7.5：Problems 1, 4, 9, 13, 17, 45, 46, 51, 53, 60, 62, 63, 64, 71, 75。

---

- 上一篇：[7.4 Matrix Representation of Linear Operators](./07-04%20Matrix%20Representation%20of%20Linear%20Operators.md)
- 上層：[線性代數－蘇柏青](../../README.md)
