---
aliases:
  - 2.1 Matrix Multiplication
  - 矩陣乘法
tags:
  - course/linear-algebra
  - linear-algebra/matrix-multiplication
---

# 2.1 Matrix Multiplication

> **講義範圍**
>
> `14_講義_Matrix Multiplication`，PDF 第 1-12 頁。

## Notation

- $A=[a_{ij}]\in\mathcal M_{m\times n}$、 $B=[b_{ij}]\in\mathcal M_{n\times p}$。
- $B=[\mathbf b_1\ \cdots\ \mathbf b_p]$，其中 $\mathbf b_j\in\mathbb R^n$ 是 $B$ 的第 $j$ 個 column。
- $AB$ 只有在 $A$ 的 column 數等於 $B$ 的 row 數時才有定義。

## Definition of Matrix Multiplication

矩陣乘積定義為

$$
AB=[A\mathbf b_1\ \cdots\ A\mathbf b_p]\in\mathcal M_{m\times p}.
$$

因此 $AB$ 的第 $j$ 個 column 是 $A\mathbf b_j$。逐 entry 表示即為 row-column rule：

$$
(AB)_{ij}=\sum_{k=1}^{n}a_{ik}b_{kj}.
$$

乘積的尺寸由外側維度決定：

$$
(m\times n)(n\times p)=m\times p.
$$

對任意 $\mathbf v\in\mathbb R^p$，

$$
(AB)\mathbf v=A(B\mathbf v).
$$

這表示先以 $B$ 作用於 $\mathbf v$，再以 $A$ 作用，等同於直接以 $AB$ 作用。

## Theorem 2.1: Algebraic Properties

令 $A,B\in\mathcal M_{k\times m}$、 $C\in\mathcal M_{m\times n}$、 $P,Q\in\mathcal M_{n\times p}$，且 $s\in\mathbb R$。在尺寸相容時：

1. $s(AC)=(sA)C=A(sC)$。
2. $A(CP)=(AC)P$。
3. $(A+B)C=AC+BC$。
4. $C(P+Q)=CP+CQ$。
5. $I_kA=A=AI_m$。
6. 適當尺寸的零矩陣滿足 $A0=0$ 與 $0A=0$。
7. $(AC)^T=C^TA^T$。

上述性質皆可由 entry 定義直接驗證。特別注意，轉置會反轉乘法順序。

## Noncommutativity

一般而言，矩陣乘法不滿足交換律：

$$
AB\ne BA.
$$

甚至可能只有其中一個乘積有定義。即使 $A,B$ 都是同階方陣且兩個乘積皆存在，也不保證相等。

## Powers and Special Matrices

若 $A\in\mathcal M_{n\times n}$，定義

$$
A^0=I_n,
\qquad
A^r=\underbrace{A\cdots A}_{r\text{ factors}}\quad(r\ge1).
$$

由結合律可得 $A^rA^s=A^{r+s}$。

若 block matrix 的尺寸相容，則

$$
P[A\ B]=[PA\ PB].
$$

若 $D=\mathrm{diag}(d_1,\ldots,d_n)$、 $E=\mathrm{diag}(e_1,\ldots,e_n)$，則

$$
DE=\mathrm{diag}(d_1e_1,\ldots,d_ne_n).
$$

矩陣 $S$ 稱為 symmetric，若 $S^T=S$。對任意實矩陣 $A$，

$$
(AA^T)^T=AA^T,
\qquad
(A^TA)^T=A^TA,
$$

故 $AA^T$ 與 $A^TA$ 都是 symmetric matrices。

## Common Pitfalls

- $AB$ 不是逐 entry 相乘。
- 一般不可由 $AB=AC$ 推出 $B=C$。
- $(AB)^T=B^TA^T$，不是 $A^TB^T$。
- $(A+B)^2=A^2+AB+BA+B^2$；除非 $AB=BA$，否則不能合併中間兩項。

## Assigned Exercises

Section 2.1：Problems 1, 3, 7, 9, 13, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 41, 47, 49。

---

- 上一篇：[1.7 Linear Dependence and Linear Independence](../section-01/01-07%20Linear%20Dependence%20and%20Linear%20Independence.md)
- 下一篇：[2.3 Invertibility and Elementary Matrices](./02-03%20Invertibility%20and%20Elementary%20Matrices.md)
- 上層：[線性代數－蘇柏青](../../README.md)
