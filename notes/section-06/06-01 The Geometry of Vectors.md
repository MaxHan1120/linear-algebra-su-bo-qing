---
aliases:
  - 6.1 The Geometry of Vectors
  - 向量的幾何
tags:
  - course/linear-algebra
  - linear-algebra/dot-product
  - linear-algebra/norm
---

# 6.1 The Geometry of Vectors

> **講義範圍**
>
> `37_講義_The Geometry of Vectors Dot Product(1)`，PDF 第 1-26 頁。

## Norm and Distance

對 $\mathbf v\in\mathbb R^n$，定義 Euclidean norm

$$
\lVert\mathbf v\rVert
=\sqrt{v_1^2+\cdots+v_n^2}.
$$

兩向量 $\mathbf u,\mathbf v$ 的 distance 定義為

$$
d(\mathbf u,\mathbf v)=\lVert\mathbf u-\mathbf v\rVert.
$$

## Dot Product and Orthogonality

對 $\mathbf u,\mathbf v\in\mathbb R^n$，定義

$$
\mathbf u\cdot\mathbf v
=\mathbf u^T\mathbf v
=u_1v_1+\cdots+u_nv_n.
$$

若

$$
\mathbf u\cdot\mathbf v=0,
$$

則稱 $\mathbf u$ 與 $\mathbf v$ orthogonal。Zero vector 與所有向量 orthogonal。

## Theorem 6.1: Basic Properties

對 $\mathbf u,\mathbf v,\mathbf w\in\mathbb R^n$ 與 $c\in\mathbb R$：

$$
\mathbf u\cdot\mathbf u=\lVert\mathbf u\rVert^2,
$$

$$
\mathbf u\cdot\mathbf u=0\iff\mathbf u=\mathbf0,
$$

$$
\mathbf u\cdot\mathbf v=\mathbf v\cdot\mathbf u,
$$

$$
\mathbf u\cdot(\mathbf v+\mathbf w)
=\mathbf u\cdot\mathbf v+\mathbf u\cdot\mathbf w,
$$

$$
(c\mathbf u)\cdot\mathbf v
=c(\mathbf u\cdot\mathbf v)
=\mathbf u\cdot(c\mathbf v),
$$

$$
\lVert c\mathbf u\rVert=|c|\lVert\mathbf u\rVert.
$$

## Theorem 6.2: Pythagorean Theorem

$\mathbf u$ 與 $\mathbf v$ orthogonal，若且唯若

$$
\lVert\mathbf u+\mathbf v\rVert^2
=\lVert\mathbf u\rVert^2+\lVert\mathbf v\rVert^2.
$$

因為

$$
\lVert\mathbf u+\mathbf v\rVert^2
=\lVert\mathbf u\rVert^2
+2\mathbf u\cdot\mathbf v
+\lVert\mathbf v\rVert^2.
$$

## Projection onto a Line

令 $L=\mathrm{Span}\{\mathbf u\}$，其中 $\mathbf u\neq\mathbf0$。向量 $\mathbf v$ 投影至 $L$ 的 orthogonal projection 為

$$
\mathrm{proj}_{\mathbf u}(\mathbf v)
=\frac{\mathbf v\cdot\mathbf u}{\lVert\mathbf u\rVert^2}\mathbf u.
$$

Residual

$$
\mathbf v-\mathrm{proj}_{\mathbf u}(\mathbf v)
$$

與 $\mathbf u$ orthogonal；其 norm 是 $\mathbf v$ 的端點至 $L$ 的 distance。

## Theorem 6.3: Cauchy-Schwarz Inequality

對所有 $\mathbf u,\mathbf v\in\mathbb R^n$，

$$
|\mathbf u\cdot\mathbf v|
\leq\lVert\mathbf u\rVert\lVert\mathbf v\rVert.
$$

當且僅當 $\mathbf u$ 與 $\mathbf v$ linearly dependent 時取等號。

若兩向量皆 nonzero，可定義夾角 $\theta$：

$$
\cos\theta
=\frac{\mathbf u\cdot\mathbf v}
{\lVert\mathbf u\rVert\lVert\mathbf v\rVert}.
$$

## Theorem 6.4: Triangle Inequality

$$
\lVert\mathbf u+\mathbf v\rVert
\leq\lVert\mathbf u\rVert+\lVert\mathbf v\rVert.
$$

它由展開 $\lVert\mathbf u+\mathbf v\rVert^2$ 並套用 Cauchy-Schwarz inequality 得到。

## Complex Inner Product

對 $\mathbf u,\mathbf v\in\mathbb C^n$，dot product 必須改為 Hermitian inner product：

$$
\mathbf u^H\mathbf v
=\overline{u_1}v_1+\cdots+\overline{u_n}v_n.
$$

此時

$$
\lVert\mathbf v\rVert
=\sqrt{|v_1|^2+\cdots+|v_n|^2},
$$

且

$$
\mathbf u^H\mathbf v
=\overline{\mathbf v^H\mathbf u}.
$$

## Common Pitfalls

- $\lVert\mathbf u+\mathbf v\rVert$ 通常不等於 $\lVert\mathbf u\rVert+\lVert\mathbf v\rVert$。
- Orthogonal 不代表兩向量都是 nonzero；zero vector 與所有向量 orthogonal。
- Projection formula 的 denominator 是 $\lVert\mathbf u\rVert^2$。
- 在 $\mathbb C^n$ 必須使用 complex conjugate。

## Assigned Exercises

Section 6.1：Problems 7, 15, 81-89, 92, 95。

---

- 上一篇：[5.3 Diagonalization of Matrices](../section-05/05-03%20Diagonalization%20of%20Matrices.md)
- 下一篇：[6.2 Orthogonal Vectors](./06-02%20Orthogonal%20Vectors.md)
- 上層：[線性代數－蘇柏青](../../README.md)
