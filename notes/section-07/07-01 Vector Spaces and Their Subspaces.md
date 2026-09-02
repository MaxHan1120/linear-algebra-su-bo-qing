---
aliases:
  - 7.1 Vector Spaces and Their Subspaces
  - 向量空間及其子空間
tags:
  - course/linear-algebra
  - linear-algebra/vector-space
  - linear-algebra/abstract-subspace
---

# 7.1 Vector Spaces and Their Subspaces

> **講義範圍**
>
> `54_講義_Vector Spaces and Their Subspaces(1)`，PDF 第 1-23 頁。

## Vector Space

令 $V$ 是集合， $\mathbb F$ 是 scalar field，通常為 $\mathbb R$ 或 $\mathbb C$。若在 $V$ 上定義 vector addition 與 scalar multiplication，且對所有 $\mathbf u,\mathbf v,\mathbf w\in V$、 $a,b\in\mathbb F$ 滿足：

1. $\mathbf u+\mathbf v\in V$。
2. $\mathbf u+\mathbf v=\mathbf v+\mathbf u$。
3. $(\mathbf u+\mathbf v)+\mathbf w=\mathbf u+(\mathbf v+\mathbf w)$。
4. 存在 $\mathbf0\in V$ 使 $\mathbf u+\mathbf0=\mathbf u$。
5. 每個 $\mathbf u$ 有 additive inverse $-\mathbf u$。
6. $a\mathbf u\in V$。
7. $a(\mathbf u+\mathbf v)=a\mathbf u+a\mathbf v$。
8. $(a+b)\mathbf u=a\mathbf u+b\mathbf u$。
9. $a(b\mathbf u)=(ab)\mathbf u$。
10. $1\mathbf u=\mathbf u$。

則稱 $V$ 是 vector space over $\mathbb F$。

## Basic Examples

- $\mathbb R^n$ over $\mathbb R$。
- Matrix space $\mathcal M_{m\times n}$。
- Polynomial space $\mathcal P$ 與 $\mathcal P_n$。
- Linear-transformation space $\mathcal L(V,W)$。
- Function space $\mathcal F(S)$：所有 functions $S\to\mathbb R$。

在不同 vector spaces 中，vectors 可以是 arrays、matrices、polynomials、functions 或 transformations。

## Theorem 7.1: Function Spaces

以 pointwise operations

$$
(f+g)(t)=f(t)+g(t),
\qquad
(af)(t)=af(t)
$$

定義 addition 與 scalar multiplication，則 $\mathcal F(S)$ 是 vector space。

例如 continuous functions $C(\mathbb R)$ 是 $\mathcal F(\mathbb R)$ 的 subspace。

## Theorem 7.2: Derived Properties

Vector-space axioms 可推出：

$$
\mathbf u+\mathbf v=\mathbf w+\mathbf v
\implies
\mathbf u=\mathbf w,
$$

$$
0\mathbf v=\mathbf0,
\qquad
a\mathbf0=\mathbf0,
$$

$$
(-1)\mathbf v=-\mathbf v,
\qquad
(-a)\mathbf v=-(a\mathbf v).
$$

此外 zero vector 與 additive inverse 都是唯一的。

## Subspaces

Subset $W\subseteq V$ 稱為 subspace，若：

1. $\mathbf0\in W$；
2. 對 $\mathbf u,\mathbf v\in W$，有 $\mathbf u+\mathbf v\in W$；
3. 對 $a\in\mathbb F$ 與 $\mathbf u\in W$，有 $a\mathbf u\in W$。

Subspace 沿用 $V$ 的 operations，本身也是 vector space。

### Examples

- Trace-zero matrices：

$$
W=\{A\in\mathcal M_{n\times n}:\mathrm{tr}(A)=0\}.
$$

- $C(\mathbb R)\subseteq\mathcal F(\mathbb R)$。
- $\mathcal P_n\subseteq\mathcal P$。

恰為 degree $n$ 的 polynomials 不構成 subspace，因為不包含 zero polynomial，且 leading terms 可能相消。

## Linear Combinations and Span

即使 $S$ 是 infinite subset，linear combination 仍只允許使用有限個 vectors：

$$
\mathbf v=c_1\mathbf v_1+\cdots+c_k\mathbf v_k.
$$

$S$ 的所有有限 linear combinations 構成

$$
\mathrm{Span}(S).
$$

## Theorem 7.3

Vector space $V$ 中任意 nonempty subset $S$ 的 span 都是 $V$ 的 subspace，且是包含 $S$ 的最小 subspace。

例如

$$
\mathcal P_n=\mathrm{Span}\{1,x,\ldots,x^n\},
$$

而所有 trigonometric polynomials 由

$$
\{1,\cos t,\sin t,\cos2t,\sin2t,\ldots\}
$$

所生成。

## Common Pitfalls

- Vector-space structure 不只取決於集合，也取決於 scalar field 與兩種 operations。
- Abstract vector 不一定是 column vector。
- Infinite set 的 linear combination 仍只能包含有限個 nonzero coefficients。
- Degree 恰為 $n$ 的 polynomial set 不含 zero vector，因此不是 subspace。

## Assigned Exercises

Section 7.1：Problems 28, 30, 32, 55-59, 79-82, 91, 92。

---

- 上一篇：[6.6 Symmetric Matrices](../section-06/06-06%20Symmetric%20Matrices.md)
- 下一篇：[7.2 Linear Transformations](./07-02%20Linear%20Transformations.md)
- 上層：[線性代數－蘇柏青](../../README.md)
