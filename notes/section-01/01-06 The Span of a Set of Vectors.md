---
aliases:
  - 1.6 The Span of a Set of Vectors
  - 向量集合的生成空間
tags:
  - course/linear-algebra
  - linear-algebra/span
  - linear-algebra/generating-set
---

# 1.6 The Span of a Set of Vectors

> **講義範圍**
>
> `10_講義_Span of a Set of Vectors(1)`，PDF 第 1-16 頁。

## Notation

- $S=\{\mathbf u_1,\ldots,\mathbf u_k\}\subseteq\mathbb R^n$ 是有限且非空的向量集合。
- $A=[\mathbf u_1\ \cdots\ \mathbf u_k]\in\mathcal M_{n\times k}$ 是以 $S$ 中向量為 columns 的矩陣。
- 沿用 [1.4 Gaussian Elimination](./01-04%20Gaussian%20Elimination.md) 的 notation，矩陣的 rank 記為 $\mathrm{rank}(A)$。

## Definition of Span

$S$ 的 span（生成空間）是 $S$ 中向量所有可能的線性組合所成的集合：

$$
\mathrm{Span}(S)
=\{c_1\mathbf u_1+\cdots+c_k\mathbf u_k:c_1,\ldots,c_k\in\mathbb R\}.
$$

因此，敘述「 $\mathbf v$ 是 $\mathbf u_1,\ldots,\mathbf u_k$ 的線性組合」可簡寫為

$$
\mathbf v\in\mathrm{Span}\{\mathbf u_1,\ldots,\mathbf u_k\}.
$$

利用 matrix-vector product，可將 span 改寫為

$$
\mathrm{Span}(S)
=\{A\mathbf c:\mathbf c\in\mathbb R^k\}.
$$

故 membership problem 可轉換為線性方程組：

$$
\mathbf v\in\mathrm{Span}(S)
\iff
A\mathbf c=\mathbf v\text{ 對某個 }\mathbf c\in\mathbb R^k\text{ 有解}.
$$

實際判斷時，只需對增廣矩陣 $[A\mid\mathbf v]$ 做 Gaussian elimination；若沒有矛盾列，則 $\mathbf v\in\mathrm{Span}(S)$。

## Basic Properties

1. $\mathrm{Span}\{\mathbf 0\}=\{\mathbf 0\}$。
2. $\mathrm{Span}\{\mathbf u\}=\{c\mathbf u:c\in\mathbb R\}$，即 $\mathbf u$ 的所有 scalar multiples。
3. 若 $S$ 含有非零向量，則 $\mathrm{Span}(S)$ 含有無限多個向量。
4. $S\subseteq\mathrm{Span}(S)$，因為每個 $\mathbf u_i$ 都可令其 coefficient 為 $1$、其餘 coefficients 為 $0$ 得到。

### Geometric Interpretation

- 在 $\mathbb R^2$ 中，一個非零向量的 span 是通過原點的直線。
- 在 $\mathbb R^2$ 中，兩個不平行向量的 span 是整個 $\mathbb R^2$。
- 在 $\mathbb R^3$ 中， $\mathrm{Span}\{\mathbf e_3\}$ 是 $z$-axis。
- 在 $\mathbb R^3$ 中， $\mathrm{Span}\{\mathbf e_1,\mathbf e_2\}$ 是 $xy$-plane。
- 在 $\mathbb R^3$ 中，兩個不平行向量通常生成一個通過原點的平面。

## Generating Sets

若 $S\subseteq V\subseteq\mathbb R^n$ 且

$$
\mathrm{Span}(S)=V,
$$

則稱 $S$ 是 $V$ 的 generating set（生成集合），或稱 $S$ generates $V$。

要判斷 $S=\{\mathbf u_1,\ldots,\mathbf u_k\}$ 是否生成 $\mathbb R^n$，等價於判斷每個 $\mathbf b\in\mathbb R^n$ 是否都能寫成

$$
\mathbf b=A\mathbf x.
$$

## Theorem 1.6: Generating $\mathbb R^m$

令 $A\in\mathcal M_{m\times n}$。下列敘述彼此等價：

1. $A$ 的 columns 生成 $\mathbb R^m$。
2. 對每個 $\mathbf b\in\mathbb R^m$， $A\mathbf x=\mathbf b$ 都 consistent。
3. $\mathrm{rank}(A)=m$，即 rank 等於 $A$ 的列數。
4. $A$ 的 RREF 沒有零列。
5. $A$ 的每一列（row）都有一個 pivot position。

其中 1 與 2 直接來自 span 的定義；3、4、5 則由 rank 與 RREF 的定義得到。此定理也說明：要讓 columns 生成整個 $\mathbb R^m$，必須有足夠的 pivots 覆蓋每一列，因此必有 $n\ge m$。

## Redundant Vectors

若從 generating set 移除某個向量後 span 不變，該向量對此 span 而言是 redundant（冗餘）的。

### Theorem 1.7

令 $S=\{\mathbf u_1,ldots,\mathbf u_k\}\subseteq\mathbb R^n$，且 $\mathbf v\in\mathbb R^n$。則

$$
\mathrm{Span}(S\cup\{\mathbf v\})=\mathrm{Span}(S)
\iff
\mathbf v\in\mathrm{Span}(S).
$$

**Proof.** 因為 $S\subseteq S\cup\{\mathbf v\}$，所以必有

$$
\mathrm{Span}(S)\subseteq\mathrm{Span}(S\cup\{\mathbf v\}).
$$

若 $\mathbf v\in\mathrm{Span}(S)$，則可寫成

$$
\mathbf v=a_1\mathbf u_1+\cdots+a_k\mathbf u_k.
$$

任取 $\mathbf w\in\mathrm{Span}(S\cup\{\mathbf v\})$，存在 scalars $c_1,ldots,c_k,b$ 使

$$
\begin{aligned}
\mathbf w
&=c_1\mathbf u_1+\cdots+c_k\mathbf u_k+b\mathbf v\cr
&=(c_1+ba_1)\mathbf u_1+\cdots+(c_k+ba_k)\mathbf u_k.
\end{aligned}
$$

因此 $\mathbf w\in\mathrm{Span}(S)$，兩個 spans 相等。反之，若兩個 spans 相等，因為 $\mathbf v\in\mathrm{Span}(S\cup\{\mathbf v\})$，故必有 $\mathbf v\in\mathrm{Span}(S)$。 $\square$

所以，移除一個能由其餘向量線性組合而成的向量，不會改變集合的 span。

## Section Summary

- $\mathrm{Span}(S)$ 是 $S$ 中向量所有線性組合的集合。
- 若 $A$ 的 columns 是 $S$，則 $\mathrm{Span}(S)=\{A\mathbf c:\mathbf c\in\mathbb R^k\}$。
- $\mathbf v\in\mathrm{Span}(S)$ 當且僅當 $A\mathbf c=\mathbf v$ consistent。
- $A$ 的 columns 生成 $\mathbb R^m$ 當且僅當 $\mathrm{rank}(A)=m$，亦即 RREF 的每一列都有 pivot。
- 新增 $\mathbf v$ 不改變 span 當且僅當 $\mathbf v$ 已位於原本的 span 中。

## Practice

講義指定 Section 1.6 習題：1、3、9、11、17、21、25、27、31、33、35、37、39、41、45、49、53、57、61、63、69、71。

## Navigation

- 上一節：[1.4 Gaussian Elimination](./01-04%20Gaussian%20Elimination.md)
- 上層：[線性代數－蘇柏青](../../README.md)
- 下一節：[1.7 Linear Dependence and Linear Independence](./01-07%20Linear%20Dependence%20and%20Linear%20Independence.md)
