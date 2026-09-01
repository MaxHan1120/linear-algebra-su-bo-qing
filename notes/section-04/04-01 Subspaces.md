---
aliases:
  - 4.1 Subspaces
  - 子空間
tags:
  - course/linear-algebra
  - linear-algebra/subspace
  - linear-algebra/null-space
  - linear-algebra/column-space
---

# 4.1 Subspaces

> **講義範圍**
>
> `29_講義_Subspaces and their properties`，PDF 第 1-13 頁。

## Notation

- $W\subseteq\mathbb R^n$ 表示 $W$ 是 $\mathbb R^n$ 的 subset。
- $\mathrm{Span}(S)$ 沿用 [1.6 The Span of a Set of Vectors](../section-01/01-06%20The%20Span%20of%20a%20Set%20of%20Vectors.md) 的定義。
- 對 $A\in\mathcal M_{m\times n}$，分別以 $\mathrm{Null}(A)$、 $\mathrm{Col}(A)$、 $\mathrm{Row}(A)$ 表示 null space、column space 與 row space。

## Definition of a Subspace

subset $W\subseteq\mathbb R^n$ 稱為 $\mathbb R^n$ 的 subspace，若滿足：

1. $\mathbf0\in W$。
2. 對所有 $\mathbf u,\mathbf v\in W$，有 $\mathbf u+\mathbf v\in W$。
3. 對所有 $\mathbf u\in W$ 與 $c\in\mathbb R$，有 $c\mathbf u\in W$。

條件 2 稱為 closed under addition；條件 3 稱為 closed under scalar multiplication。

由這三個條件可得：若 $\mathbf u_1,\ldots,\mathbf u_k\in W$，則任意線性組合

$$
c_1\mathbf u_1+\cdots+c_k\mathbf u_k
$$

仍屬於 $W$。

## Basic Examples

- $\{\mathbf0\}$ 與 $\mathbb R^n$ 都是 $\mathbb R^n$ 的 subspaces。
- $\{\mathbf0\}$ 稱為 zero subspace；其餘 subspaces 稱為 nonzero subspaces。
- 通過原點的直線與平面分別是 $\mathbb R^2$ 或 $\mathbb R^3$ 的 subspaces。
- 不通過原點的 affine line 或 affine plane 不是 subspace。

例如

$$
W=
\left\{
\left[
\begin{array}{c}
w_1\cr w_2\cr w_3
\end{array}
\right]
\in\mathbb R^3:
6w_1-5w_2+4w_3=0
\right\}
$$

是 subspace。因為 homogeneous linear equation 對 zero vector 成立，且在 addition 與 scalar multiplication 下保持成立。

## How to Disprove a Subspace

只要找到一項失敗即可：

- $\mathbf0\notin W$。
- 存在 $\mathbf u,\mathbf v\in W$，但 $\mathbf u+\mathbf v\notin W$。
- 存在 $\mathbf u\in W$ 與 $c\in\mathbb R$，但 $c\mathbf u\notin W$。

例如，只包含第一象限向量的集合不對 negative scalar multiplication 封閉，因此不是 subspace。

## Theorem 4.1: Span Is a Subspace

若 $S=\{\mathbf w_1,\ldots,\mathbf w_k\}$ 是 $\mathbb R^n$ 的有限非空 subset，則

$$
\mathrm{Span}(S)
$$

是 $\mathbb R^n$ 的 subspace。

**Proof.** 令 $W=\mathrm{Span}(S)$。

1. 取所有 coefficients 為 $0$，可得 $\mathbf0\in W$。
2. 兩個 linear combinations 相加後仍是 $S$ 中向量的 linear combination。
3. linear combination 乘以 scalar 後仍是 $S$ 中向量的 linear combination。

因此 $W$ 滿足 subspace 的三個條件。

### Example

若

$$
W=
\left\{
\left[
\begin{array}{c}
2a-3b\cr
b\cr
-a+4b
\end{array}
\right]:a,b\in\mathbb R
\right\},
$$

則

$$
W=\mathrm{Span}
\left\{
\left[
\begin{array}{r}
2\cr0\cr-1
\end{array}
\right],
\left[
\begin{array}{r}
-3\cr1\cr4
\end{array}
\right]
\right\},
$$

故 $W$ 是 $\mathbb R^3$ 的 subspace。

## Null Space

對 $A\in\mathcal M_{m\times n}$，null space 定義為

$$
\mathrm{Null}(A)
=\{\mathbf x\in\mathbb R^n:A\mathbf x=\mathbf0\}.
$$

它是 homogeneous system $A\mathbf x=\mathbf0$ 的完整解集合。

### Theorem 4.2

若 $A\in\mathcal M_{m\times n}$，則 $\mathrm{Null}(A)$ 是 $\mathbb R^n$ 的 subspace。

**Proof.** 因為 $A\mathbf0=\mathbf0$。若 $A\mathbf u=A\mathbf v=\mathbf0$，則

$$
A(\mathbf u+\mathbf v)=A\mathbf u+A\mathbf v=\mathbf0.
$$

對任意 $c\in\mathbb R$，

$$
A(c\mathbf u)=cA\mathbf u=\mathbf0.
$$

所以三個 subspace conditions 均成立。

實際求 $\mathrm{Null}(A)$ 時，先解 $A\mathbf x=\mathbf0$，再將 general solution 寫成 free variables 的 linear combination；各 coefficient vectors 即構成 null space 的 generating set。

## Column Space and Row Space

若 $A=[\mathbf a_1\ \cdots\ \mathbf a_n]\in\mathcal M_{m\times n}$，定義

$$
\mathrm{Col}(A)
=\mathrm{Span}\{\mathbf a_1,\ldots,\mathbf a_n\}
\subseteq\mathbb R^m.
$$

row space 定義為 $A$ 的 rows 所生成的 subspace：

$$
\mathrm{Row}(A)\subseteq\mathbb R^n.
$$

因為 $A^T$ 的 columns 正是 $A$ 的 rows，

$$
\mathrm{Row}(A)=\mathrm{Col}(A^T).
$$

## Membership in the Column Space

對 $\mathbf b\in\mathbb R^m$，

$$
\mathbf b\in\mathrm{Col}(A)
\iff
A\mathbf x=\mathbf b\text{ is consistent}.
$$

因此可對 $[A\mid\mathbf b]$ 做 Gaussian elimination；若沒有 contradiction row，則 $\mathbf b\in\mathrm{Col}(A)$。

## Connection with Linear Transformations

若 $T:\mathbb R^n\to\mathbb R^m$ 的 standard matrix 為 $A$，則

$$
\mathrm{range}(T)=\mathrm{Col}(A).
$$

因為 $T(\mathbf x)=A\mathbf x$ 是 $A$ 的 columns 的 linear combination。

同時，沿用 [2.8](../section-02/02-08%20Composition%20and%20Invertibility%20of%20Linear%20Transformations.md) 的 notation，

$$
\mathcal N(T)=\mathrm{Null}(A).
$$

所以 linear transformation 的 range 與 null space 可完全轉換成其 standard matrix 的 column space 與 null space 問題。

## Common Pitfalls

- subset 不一定是 subspace；必須逐一檢查三個 closure conditions。
- 只檢查 addition 與 scalar multiplication 不夠，仍應明確確認 $\mathbf0\in W$。
- $\mathrm{Null}(A)\subseteq\mathbb R^n$，由 $A$ 的 column 數決定 ambient space。
- $\mathrm{Col}(A)\subseteq\mathbb R^m$，由 $A$ 的 row 數決定 ambient space。
- row reduction 保留解集合，但通常會改變 column space；求 $\mathrm{Col}(A)$ 的 generators 時應回到原矩陣的 pivot columns。

## Assigned Exercises

Section 4.1：Problems 2, 8, 11, 19, 27, 29, 35, 37, 77, 78, 80。

---

- 上一篇：[3.2 Properties of Determinants](../section-03/03-02%20Properties%20of%20Determinants.md)
- 下一篇：[4.2 Basis and Dimension](./04-02%20Basis%20and%20Dimension.md)
- 上層：[線性代數－蘇柏青](../../README.md)
