---
aliases:
  - 2.7 Linear Transformations and Matrices
  - 線性轉換與矩陣
tags:
  - course/linear-algebra
  - linear-algebra/linear-transformation
  - linear-algebra/standard-matrix
---

# 2.7 Linear Transformations and Matrices

> **講義範圍**
>
> `20_講義_Linear Transformations and Matrices(1)`，PDF 第 1-25 頁。

## Functions and Range

函數 $T:\mathbb R^n\to\mathbb R^m$ 將每個 $\mathbf x\in\mathbb R^n$ 指派到唯一的 $T(\mathbf x)\in\mathbb R^m$。

- $\mathbb R^n$ 是 domain。
- $\mathbb R^m$ 是 codomain。
- $T(\mathbf x)$ 是 $\mathbf x$ 的 image。
- 所有 images 所成的集合稱為 range：

$$
\mathrm{range}(T)=\{T(\mathbf x):\mathbf x\in\mathbb R^n\}\subseteq\mathbb R^m.
$$

## Matrix Transformations

對 $A\in\mathcal M_{m\times n}$，定義

$$
T_A:\mathbb R^n\to\mathbb R^m,
\qquad
T_A(\mathbf x)=A\mathbf x.
$$

例如， $\mathbb R^3$ 到 $xy$-plane 的投影矩陣為

$$
\left[
\begin{array}{ccc}
1&0&0\cr
0&1&0\cr
0&0&0
\end{array}
\right].
$$

## Theorem 2.7: Linearity of Matrix Transformations

對任意 $\mathbf u,\mathbf v\in\mathbb R^n$ 與 $c\in\mathbb R$，

$$
T_A(\mathbf u+\mathbf v)=T_A(\mathbf u)+T_A(\mathbf v),
$$

$$
T_A(c\mathbf u)=cT_A(\mathbf u).
$$

兩式分別稱為 additivity 與 homogeneity。

## Linear Transformations

$T:\mathbb R^n\to\mathbb R^m$ 稱為 linear transformation，若對所有 $\mathbf u,\mathbf v$、 $c\in\mathbb R$ 均滿足上述兩式。

### Theorem 2.8: Immediate Consequences

若 $T$ 為 linear，則：

1. $T(\mathbf0)=\mathbf0$。
2. $T(-\mathbf u)=-T(\mathbf u)$。
3. $T(\mathbf u-\mathbf v)=T(\mathbf u)-T(\mathbf v)$。
4. $T(a\mathbf u+b\mathbf v)=aT(\mathbf u)+bT(\mathbf v)$。

更一般地， $T$ 保留任意有限線性組合：

$$
T\left(\sum_{i=1}^k c_i\mathbf u_i\right)
=\sum_{i=1}^k c_iT(\mathbf u_i).
$$

所以若 $T(\mathbf0)\ne\mathbf0$，便可立即判定 $T$ 不是 linear。例如 $T(x)=2x+3$ 不是 linear；identity transformation 與 zero transformation 則都是 linear。

## Theorem 2.9: Standard Matrix

每個 linear transformation $T:\mathbb R^n\to\mathbb R^m$ 都存在唯一 $A\in\mathcal M_{m\times n}$，使

$$
T(\mathbf x)=A\mathbf x.
$$

此 $A$ 稱為 $T$ 的 standard matrix，且

$$
A=[T(\mathbf e_1)\ \cdots\ T(\mathbf e_n)].
$$

因為 $\mathbf x=x_1\mathbf e_1+\cdots+x_n\mathbf e_n$，

$$
T(\mathbf x)=x_1T(\mathbf e_1)+\cdots+x_nT(\mathbf e_n)=A\mathbf x.
$$

### Example

若

$$
T\left(
\left[
\begin{array}{c}
x_1\cr x_2\cr x_3
\end{array}
\right]
\right)=
\left[
\begin{array}{c}
3x_1-4x_2\cr
2x_1+x_3
\end{array}
\right],
$$

則

$$
A=
\left[
\begin{array}{rrr}
3&-4&0\cr
2&0&1
\end{array}
\right].
$$

也可逐一計算 $T(\mathbf e_1)$、 $T(\mathbf e_2)$、 $T(\mathbf e_3)$，再依序作為 $A$ 的 columns。

## Geometric Example

對 $x$-axis 的 reflection 滿足 $T(x_1,x_2)=(x_1,-x_2)$，standard matrix 為

$$
\left[
\begin{array}{rr}
1&0\cr
0&-1
\end{array}
\right].
$$

## Assigned Exercises

Section 2.7：Problems 1-6, 10-12, 21-23, 26, 29, 32-34。

---

- 上一篇：[2.4 The Inverse of a Matrix](./02-04%20The%20Inverse%20of%20a%20Matrix.md)
- 下一篇：[2.8 Composition and Invertibility of Linear Transformations](./02-08%20Composition%20and%20Invertibility%20of%20Linear%20Transformations.md)
- 上層：[線性代數－蘇柏青](../../README.md)
