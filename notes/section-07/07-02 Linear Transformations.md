---
aliases:
  - 7.2 Linear Transformations
  - 抽象向量空間的線性轉換
tags:
  - course/linear-algebra
  - linear-algebra/abstract-linear-transformation
  - linear-algebra/isomorphism
---

# 7.2 Linear Transformations

> **講義範圍**
>
> `53_講義_Linear Transformation(1)`，PDF 第 1-22 頁。

## Linear Transformations on General Vector Spaces

令 $V,W$ 是 over the same field $\mathbb F$ 的 vector spaces。Function

$$
T:V\to W
$$

稱為 linear transformation，若

$$
T(\mathbf u+\mathbf v)=T(\mathbf u)+T(\mathbf v),
$$

$$
T(c\mathbf u)=cT(\mathbf u).
$$

若 domain 與 codomain 相同，即 $T:V\to V$，則稱為 linear operator。

### Examples

- Transpose map $U:\mathcal M_{m\times n}\to\mathcal M_{n\times m}$， $U(A)=A^T$。
- Differentiation $D:C^\infty\to C^\infty$， $D(f)=f'$。
- Integration functional

$$
T:C([a,b])\to\mathbb R,
\qquad
T(f)=\int_a^b f(t)\,dt.
$$

## Theorem 7.4

對 linear transformation $T:V\to W$：

$$
T(\mathbf0_V)=\mathbf0_W,
$$

$$
T(-\mathbf u)=-T(\mathbf u),
$$

$$
T(\mathbf u-\mathbf v)=T(\mathbf u)-T(\mathbf v),
$$

$$
T(a\mathbf u+b\mathbf v)=aT(\mathbf u)+bT(\mathbf v).
$$

更一般地， $T$ preserves every finite linear combination。

## Null Space and Range

定義

$$
\mathcal N(T)
=\{\mathbf v\in V:T(\mathbf v)=\mathbf0_W\},
$$

$$
\mathrm{range}(T)
=\{T(\mathbf v):\mathbf v\in V\}.
$$

$\mathcal N(T)$ 是 $V$ 的 subspace， $\mathrm{range}(T)$ 是 $W$ 的 subspace。

例如 differentiation operator 的 null space 是 constant functions；在 $C^\infty$ 上，其 range 仍為 $C^\infty$。

## Onto and One-to-One

$T$ onto 若

$$
\mathrm{range}(T)=W.
$$

$T$ one-to-one 若

$$
T(\mathbf u)=T(\mathbf v)
\implies
\mathbf u=\mathbf v.
$$

## Theorem 7.5

Linear transformation $T$ one-to-one，若且唯若

$$
\mathcal N(T)=\{\mathbf0_V\}.
$$

因為 $T(\mathbf u)=T(\mathbf v)$ 等價於 $T(\mathbf u-\mathbf v)=\mathbf0_W$。

## Isomorphisms

若 $T:V\to W$ 同時 one-to-one 且 onto，則稱 $T$ 為 isomorphism，並稱 $V$ 與 $W$ isomorphic。

Isomorphism 保留所有 linear structure。Transpose map

$$
U:\mathcal M_{m\times n}\to\mathcal M_{n\times m}
$$

就是 isomorphism。

## Theorem 7.6

若 $T:V\to W$ 是 isomorphism，則 inverse

$$
T^{-1}:W\to V
$$

也是 isomorphism，特別是 linear transformation。

## Composition

若 $T:V\to W$ 與 $U:W\to Z$ linear，定義

$$
(U\circ T)(\mathbf v)=U(T(\mathbf v)).
$$

## Theorem 7.7

$U\circ T:V\to Z$ 仍是 linear transformation。若 $T,U$ 都 invertible，則

$$
(U\circ T)^{-1}=T^{-1}\circ U^{-1}.
$$

若兩者都是 isomorphisms，composition 也是 isomorphism。

## Common Pitfalls

- Domain 與 codomain 的 zero vectors 可能屬於不同 spaces，應寫成 $\mathbf0_V$ 與 $\mathbf0_W$。
- Onto 取決於指定 codomain；相同 formula 配上不同 codomain，結果可能不同。
- One-to-one 可由 null space 判斷；onto 則由 range 判斷。
- Differentiation 在 $C^\infty$ 上 onto，但在 $\mathcal P_n\to\mathcal P_n$ 上不是 onto。

## Assigned Exercises

Section 7.2：Problems 1, 2, 30, 31, 38, 49, 51, 53。

---

- 上一篇：[7.1 Vector Spaces and Their Subspaces](./07-01%20Vector%20Spaces%20and%20Their%20Subspaces.md)
- 下一篇：[7.3 Basis and Dimension](./07-03%20Basis%20and%20Dimension.md)
- 上層：[線性代數－蘇柏青](../../README.md)
