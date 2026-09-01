---
aliases:
  - 1.7 Linear Dependence and Linear Independence
  - 線性相依與線性獨立
tags:
  - course/linear-algebra
  - linear-algebra/linear-dependence
  - linear-algebra/linear-independence
---

# 1.7 Linear Dependence and Linear Independence

> **講義範圍**
>
> `12_講義_Linear Dependence and Linear Independence(1)`，PDF 第 1-20 頁。

## Notation

- $S=\{\mathbf u_1,\ldots,\mathbf u_k\}\subseteq\mathbb R^n$ 是有限向量集合。
- $A=[\mathbf u_1\ \cdots\ \mathbf u_k]\in\mathcal M_{n\times k}$ 是以 $S$ 中向量為 columns 的矩陣。
- 線性相依與否可轉換為 homogeneous system $A\mathbf x=\mathbf 0$ 的解是否唯一。

## Linear Dependence

$S$ 稱為 linearly dependent（線性相依，L.D.），若存在不全為零的 scalars $c_1,ldots,c_k$，使

$$
c_1\mathbf u_1+\cdots+c_k\mathbf u_k=\mathbf 0.
$$

此式稱為 $S$ 的 nontrivial linear relation（非平凡線性關係）。

## Linear Independence

$S$ 稱為 linearly independent（線性獨立，L.I.），若

$$
c_1\mathbf u_1+\cdots+c_k\mathbf u_k=\mathbf 0
$$

只可能在

$$
c_1=c_2=\cdots=c_k=0
$$

時成立。也就是說， $S$ 沒有 nontrivial linear relation。

## Matrix Criterion

由 matrix-vector product，

$$
c_1\mathbf u_1+\cdots+c_k\mathbf u_k=\mathbf 0
\iff
A\mathbf c=\mathbf 0,
$$

其中 $\mathbf c=[c_1,\ldots,c_k]^T$。因此：

$$
\begin{aligned}
S\text{ 是 L.D.}
&\iff A\mathbf c=\mathbf 0\text{ 有非零解},\cr
S\text{ 是 L.I.}
&\iff A\mathbf c=\mathbf 0\text{ 只有零解}.
\end{aligned}
$$

若 $A\mathbf c=\mathbf 0$ 的 RREF 含 free variables，則存在非零解，所以 columns 為 L.D.；若沒有 free variables，則 columns 為 L.I.

### Immediate Property

任何含有零向量的有限集合都 L.D.。例如，若 $S=\{\mathbf 0,\mathbf u_1,\ldots,\mathbf u_k\}$，則

$$
1\mathbf 0+0\mathbf u_1+\cdots+0\mathbf u_k=\mathbf 0
$$

是一個 nontrivial linear relation。

## Example: Finding a Redundant Vector

令

$$
\begin{aligned}
\mathbf u_1&=\begin{bmatrix}1\cr2\cr1\end{bmatrix},
&\mathbf u_2&=\begin{bmatrix}1\cr0\cr1\end{bmatrix},
&\mathbf u_3&=\begin{bmatrix}1\cr4\cr1\end{bmatrix},
&\mathbf u_4&=\begin{bmatrix}1\cr2\cr3\end{bmatrix}.
\end{aligned}
$$

以這四個向量為 columns，對 $[A\mid\mathbf 0]$ 做列簡化：

$$
\left[
\begin{array}{cccc|c}
1&1&1&1&0\cr
2&0&4&2&0\cr
1&1&1&3&0
\end{array}
\right]
\sim
\left[
\begin{array}{cccc|c}
1&0&2&0&0\cr
0&1&-1&0&0\cr
0&0&0&1&0
\end{array}
\right].
$$

故

$$
x_1=-2x_3,
\qquad
x_2=x_3,
\qquad
x_3\text{ free},
\qquad
x_4=0.
$$

令 $x_3=1$，可得

$$
-2\mathbf u_1+\mathbf u_2+\mathbf u_3=\mathbf 0.
$$

因此 $S$ 為 L.D.，且 $\mathbf u_3=2\mathbf u_1-\mathbf u_2$； $\mathbf u_3$ 可由其餘向量表示。注意所有解皆有 $x_4=0$，所以此關係不能證明 $\mathbf u_4$ 是其餘向量的線性組合。

## Theorem 1.8: Equivalent Conditions for L.I.

令 $A\in\mathcal M_{m\times n}$。下列敘述彼此等價：

1. $A$ 的 columns 線性獨立。
2. 對每個 $\mathbf b\in\mathbb R^m$， $A\mathbf x=\mathbf b$ 至多有一個解。
3. $\mathrm{nullity}(A)=0$。
4. $\mathrm{rank}(A)=n$，即 rank 等於 $A$ 的行數。
5. $A$ 的 RREF 的各 columns 是 $\mathbb R^m$ 中互不相同的 standard vectors。
6. $A\mathbf x=\mathbf 0$ 只有零解 $\mathbf x=\mathbf 0$。
7. $A$ 的每一行（column）都有 pivot position。

條件 1 與 6 直接來自 L.I. 的定義；條件 3 與 4 由

$$
\mathrm{rank}(A)+\mathrm{nullity}(A)=n
$$

得到。條件 4、5、7 都表示每個 column 都是 pivot column。由於一個 pivot 不能同時位於兩個 columns，要使 $n$ 個 columns 都有 pivots，必有 $n\le m$。

若 $\mathbf u$、 $\mathbf v$ 都是 $A\mathbf x=\mathbf b$ 的解，則

$$
A(\mathbf u-\mathbf v)=A\mathbf u-A\mathbf v=\mathbf b-\mathbf b=\mathbf 0.
$$

所以 $A\mathbf x=\mathbf 0$ 只有零解時，必有 $\mathbf u=\mathbf v$，說明任意 consistent system 都不可能有兩個不同的解。

## Homogeneous Systems

當 $\mathbf b=\mathbf 0$ 時， $A\mathbf x=\mathbf b$ 稱為 homogeneous system（齊次線性方程組）：

$$
A\mathbf x=\mathbf 0.
$$

其基本性質如下：

1. 齊次系統永遠 consistent，因為 $\mathbf x=\mathbf 0$ 必為解。
2. 若齊次系統有非零解，則 $A$ 的 columns 為 L.D.
3. 若 variables 數目大於 equations 數目，即 $n>m$，則必有 free variables，因此必有非零解，columns 必為 L.D.

若將 general solution 寫成 parametric vector form

$$
\mathbf x=t_1\mathbf v_1+\cdots+t_r\mathbf v_r,
$$

則由 Gaussian elimination 所得的 parameter vectors $\mathbf v_1,ldots,\mathbf v_r$ 線性獨立。

## Theorem 1.9: Detecting Dependence Sequentially

有序向量 $\mathbf u_1,ldots,\mathbf u_k\in\mathbb R^n$ 線性相依，當且僅當下列至少一項成立：

1. $\mathbf u_1=\mathbf 0$；或
2. 存在 $i\ge2$，使

$$
\mathbf u_i\in\mathrm{Span}\{\mathbf u_1,ldots,\mathbf u_{i-1}\}.
$$

對 only-if 方向，若

$$
c_1\mathbf u_1+\cdots+c_k\mathbf u_k=\mathbf 0
$$

且 coefficients 不全為零，令

$$
i=\max\{j:c_j\ne0\}.
$$

若 $i=1$，則 $c_1\mathbf u_1=\mathbf 0$ 且 $c_1\ne0$，所以 $\mathbf u_1=\mathbf 0$。若 $i>1$，則

$$
\mathbf u_i
=-\frac{c_1}{c_i}\mathbf u_1-cdots-\frac{c_{i-1}}{c_i}\mathbf u_{i-1},
$$

故 $\mathbf u_i$ 是前面向量的線性組合。

## Useful Consequences

1. 單向量集合 $\{\mathbf u\}$ 為 L.I. 當且僅當 $\mathbf u\ne\mathbf 0$。
2. 兩向量集合 $\{\mathbf u_1,\mathbf u_2\}$ 為 L.D. 當且僅當 $\mathbf u_1=\mathbf 0$，或 $\mathbf u_2$ 是 $\mathbf u_1$ 的 scalar multiple。
3. 若 $S$ 為 L.I. 且 $\mathbf v\notin\mathrm{Span}(S)$，則 $S\cup\{\mathbf v\}$ 仍為 L.I.
4. $\mathbb R^n$ 中含超過 $n$ 個向量的任何有限集合必為 L.D.
5. 有限集合 $S$ 為 L.I. 當且僅當不能移除其中任何向量而保持 $\mathrm{Span}(S)$ 不變。

## Rank, Existence, and Uniqueness

對 $A\in\mathcal M_{m\times n}$：

- $\mathrm{rank}(A)=m$：每個 row 有 pivot；columns 生成 $\mathbb R^m$；對每個 $\mathbf b\in\mathbb R^m$， $A\mathbf x=\mathbf b$ 至少有一解。
- $\mathrm{rank}(A)=n$：每個 column 有 pivot；columns 線性獨立；對每個 $\mathbf b\in\mathbb R^m$， $A\mathbf x=\mathbf b$ 至多有一解。

若 $A$ 是方陣且 $\mathrm{rank}(A)=m=n$，則對每個 $\mathbf b$， $A\mathbf x=\mathbf b$ 恰有一解。

## Section Summary

- L.D. 表示存在不全為零的 coefficients 使線性組合為 $\mathbf 0$；L.I. 表示只有 trivial coefficients 能做到。
- Columns 是否 L.I. 等價於 $A\mathbf x=\mathbf 0$ 是否只有零解，也等價於每個 column 是否都有 pivot。
- $\mathrm{nullity}(A)=0$ 當且僅當 $\mathrm{rank}(A)=n$，此時 columns 為 L.I.
- 齊次系統永遠有零解；若出現 free variables，便有非零解，columns 因而 L.D.
- L.D. 集合中，依給定順序必有第一個零向量，或某個向量能由其前面的向量線性表示。

## Practice

講義指定 Section 1.7 習題：1、3、7、9、13、17、21、23、25、27、29、31、39、43、49、51、53、59、61、63、69、71、75、79。

## Navigation

- 上一節：[1.6 The Span of a Set of Vectors](./01-06%20The%20Span%20of%20a%20Set%20of%20Vectors.md)
- 上層：[線性代數－蘇柏青](../../README.md)
- 下一章：[2.1 Matrix Multiplication](../section-02/02-01%20Matrix%20Multiplication.md)
