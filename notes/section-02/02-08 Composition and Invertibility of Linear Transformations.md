---
aliases:
  - 2.8 Composition and Invertibility of Linear Transformations
  - 線性轉換的合成與可逆性
tags:
  - course/linear-algebra
  - linear-algebra/composition
  - linear-algebra/invertible-transformation
---

# 2.8 Composition and Invertibility of Linear Transformations

> **講義範圍**
>
> `24_講義_Composition and Invertibility of Linear Transformations(1)`，PDF 第 1-17 頁。

## Range from the Standard Matrix

令 $T:\mathbb R^n\to\mathbb R^m$ 為 linear transformation，standard matrix 為

$$
A=[T(\mathbf e_1)\ \cdots\ T(\mathbf e_n)].
$$

因為 $T(\mathbf x)=A\mathbf x$，所以

$$
\mathrm{range}(T)
=\{A\mathbf x:\mathbf x\in\mathbb R^n\}
=\mathrm{Span}\{\mathbf a_1,\ldots,\mathbf a_n\}.
$$

因此 $A$ 的 columns 構成 $\mathrm{range}(T)$ 的 generating set。

## Onto Transformations

$T:\mathbb R^n\to\mathbb R^m$ 稱為 onto，若

$$
\mathrm{range}(T)=\mathbb R^m.
$$

亦即對每個 $\mathbf b\in\mathbb R^m$，至少存在一個 $\mathbf x\in\mathbb R^n$ 使 $T(\mathbf x)=\mathbf b$。

### Theorem 2.10

令 $A$ 是 $T$ 的 standard matrix。下列敘述彼此等價：

1. $T$ onto。
2. $A$ 的 columns 生成 $\mathbb R^m$。
3. $\mathrm{rank}(A)=m$。

等價地， $A\mathbf x=\mathbf b$ 對每個 $\mathbf b\in\mathbb R^m$ 至少有一個解。由 $\mathrm{rank}(A)\le n$ 可知，onto 必須滿足 $n\ge m$。

## One-to-One Transformations and Null Space

$T:\mathbb R^n\to\mathbb R^m$ 稱為 one-to-one，若

$$
T(\mathbf u)=T(\mathbf v)
\implies
\mathbf u=\mathbf v.
$$

$T$ 的 null space 定義為

$$
\mathcal N(T)=\{\mathbf x\in\mathbb R^n:T(\mathbf x)=\mathbf0\}.
$$

若 $A$ 是 standard matrix，則 $\mathcal N(T)$ 是 $A\mathbf x=\mathbf0$ 的解集合。

### Theorem 2.11

下列敘述彼此等價：

1. $T$ one-to-one。
2. $\mathcal N(T)=\{\mathbf0\}$。
3. $A$ 的 columns 線性獨立。
4. $\mathrm{rank}(A)=n$。

所以，若 $T$ one-to-one，則 $A\mathbf x=\mathbf b$ 對每個 $\mathbf b$ 至多有一個解。由 $\mathrm{rank}(A)\le m$ 可知，one-to-one 必須滿足 $n\le m$。

## Composition

給定 $T:\mathbb R^n\to\mathbb R^m$ 與 $U:\mathbb R^m\to\mathbb R^p$，composition $U\circ T$ 定義為

$$
(U\circ T)(\mathbf x)=U(T(\mathbf x)).
$$

### Theorem 2.12

若 $T$、 $U$ 的 standard matrices 分別為 $A$、 $B$，則 $U\circ T$ 仍為 linear transformation，standard matrix 為

$$
BA.
$$

順序不可顛倒，因為

$$
(U\circ T)(\mathbf x)=B(A\mathbf x)=(BA)\mathbf x.
$$

因此 $BA$ 表示「先作用 $A$，再作用 $B$」。

## Invertible Transformations

函數 $T:S_1\to S_2$ 稱為 invertible，若存在 $T^{-1}:S_2\to S_1$ 使

$$
T^{-1}\circ T=I_{S_1},
\qquad
T\circ T^{-1}=I_{S_2}.
$$

inverse function 若存在則唯一；可逆函數必須同時 one-to-one 且 onto。

### Theorem 2.13

令 $T:\mathbb R^n\to\mathbb R^n$ 的 standard matrix 為 $A$。則

$$
T\text{ is invertible}
\iff
A\text{ is invertible}.
$$

若成立，則 $T^{-1}$ 仍為 linear transformation，且

$$
T^{-1}=T_{A^{-1}},
\qquad
T^{-1}(\mathbf y)=A^{-1}\mathbf y.
$$

## Summary of Rank Criteria

對 $T:\mathbb R^n\to\mathbb R^m$，standard matrix $A\in\mathcal M_{m\times n}$：

| Property of $T$ | Rank criterion | $A\mathbf x=\mathbf b$ |
|---|---:|---|
| onto | $\mathrm{rank}(A)=m$ | 對每個 $\mathbf b$ 至少一解 |
| one-to-one | $\mathrm{rank}(A)=n$ | 對每個 $\mathbf b$ 至多一解 |
| invertible | $m=n=\mathrm{rank}(A)$ | 對每個 $\mathbf b$ 唯一解 |

因此 linear transformation 可逆恰好等價於同時 onto 與 one-to-one。

## Assigned Exercises

Section 2.8：Problems 1, 5, 13, 17, 19, 25, 29, 33, 37。

---

- 上一篇：[2.7 Linear Transformations and Matrices](./02-07%20Linear%20Transformations%20and%20Matrices.md)
- 上層：[線性代數－蘇柏青](../../README.md)
