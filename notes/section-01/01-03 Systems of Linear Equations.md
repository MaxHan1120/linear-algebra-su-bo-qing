---
aliases:
  - 1.3 Systems of Linear Equations
  - 線性方程組
tags:
  - course/linear-algebra
  - linear-algebra/system-of-equations
  - linear-algebra/row-reduction
---

# 1.3 Systems of Linear Equations

> **講義範圍**
>
> `6_講義_System of Linear Equations(1)`，PDF 第 1-27 頁。

## Notation

- 沿用前兩節的約定：vector 皆指 column vector，並以粗體小寫字母表示。
- $A=[a_{ij}]\in\mathcal M_{m\times n}$：coefficient matrix（係數矩陣）。
- $\mathbf x=[x_1,\ldots,x_n]^T\in\mathbb R^n$：variable vector（變數向量）。
- $\mathbf b=[b_1,\ldots,b_m]^T\in\mathbb R^m$：constant vector（常數向量）。
- 本文採「列 = row、行 = column」；第 $i$ 列記為 $R_i$。

## Linear Equations and Systems

關於變數 $x_1,\ldots,x_n$ 的線性方程式（linear equation）具有形式

$$
a_1x_1+a_2x_2+\cdots+a_nx_n=b,
$$

其中 $a_1,\ldots,a_n,b\in\mathbb R$。由 $m$ 個線性方程式組成的系統稱為線性方程組（system of linear equations）：

$$
\begin{aligned}
a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=b_1,\cr
a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=b_2,\cr
&\vdots\cr
a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m.
\end{aligned}
$$

利用 [1.2 Matrix-Vector Product](./01-02%20Linear%20Combinations,%20Matrix-Vector%20Products,%20and%20Special%20Matrices.md) 的定義，此方程組可簡寫為

$$
A\mathbf x=\mathbf b.
$$

### Coefficient Matrix and Augmented Matrix

係數矩陣、變數向量與常數向量分別為

$$
A=
\begin{bmatrix}
a_{11}&a_{12}&\cdots&a_{1n}\cr
a_{21}&a_{22}&\cdots&a_{2n}\cr
\vdots&\vdots&\ddots&\vdots\cr
a_{m1}&a_{m2}&\cdots&a_{mn}
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
x_1\cr x_2\cr \vdots\cr x_n
\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}
b_1\cr b_2\cr \vdots\cr b_m
\end{bmatrix}.
$$

將常數向量附加於 $A$ 的最後一行，可得 $m\times(n+1)$ augmented matrix（增廣矩陣）：

$$
[A\mid\mathbf b]=
\left[
\begin{array}{cccc|c}
a_{11}&a_{12}&\cdots&a_{1n}&b_1\cr
a_{21}&a_{22}&\cdots&a_{2n}&b_2\cr
\vdots&\vdots&\ddots&\vdots&\vdots\cr
a_{m1}&a_{m2}&\cdots&a_{mn}&b_m
\end{array}
\right].
$$

## Solutions and Solution Sets

向量 $\mathbf s=[s_1,\ldots,s_n]^T\in\mathbb R^n$ 若滿足

$$
A\mathbf s=\mathbf b,
$$

則稱 $\mathbf s$ 為此方程組的一個 solution（解）。所有解組成的 solution set（解集合）為

$$
\mathcal S
=\{\mathbf x\in\mathbb R^n:A\mathbf x=\mathbf b\}.
$$

任何線性方程組的解集合恰屬於下列三種情況之一：

- 無解： $\mathcal S=\varnothing$。
- 唯一解： $\mathcal S=\{\mathbf s\}$。
- 無限多解： $\mathcal S$ 含無限多個向量。

若 $\mathcal S\ne\varnothing$，稱方程組為 consistent（相容）；若 $\mathcal S=\varnothing$，則稱為 inconsistent（不相容）。

兩個線性方程組若具有完全相同的解集合，便稱為 equivalent systems（等價方程組）。

## Elementary Row Operations

對一個矩陣進行下列任一操作，稱為 elementary row operation（初等列運算）：

1. **Interchange**：交換兩列， $R_i\leftrightarrow R_j$。
2. **Scaling**：以非零 scalar $c$ 乘某一列， $R_i\leftarrow cR_i$，其中 $c\ne0$。
3. **Row addition**：將另一列的倍數加至某一列， $R_i\leftarrow R_i+cR_j$，其中 $i\ne j$。

每種初等列運算皆可逆：交換的反運算仍是交換；scaling 可乘以 $c^{-1}$ 還原；row addition 可改加 $-cR_j$ 還原。因此，對增廣矩陣進行初等列運算不改變原方程組的解集合：

$$
[A\mid\mathbf b]
\longleftrightarrow
[A'\mid\mathbf b']
\quad\Longrightarrow\quad
A\mathbf x=\mathbf b
\text{ 與 }
A'\mathbf x=\mathbf b'
\text{ 等價}.
$$

若矩陣 $B$ 可由矩陣 $A$ 經有限次初等列運算得到，則稱 $A$ 與 $B$ row equivalent（列等價）。

## Row Echelon Forms

非零列的 leading entry（首項）是該列由左至右第一個非零元素。

### Row Echelon Form

矩陣若符合下列條件，稱為 row echelon form（列梯形）：

1. 所有非零列皆位於所有零列之上。
2. 每一非零列的首項，皆位於上一列首項的右方。
3. 每個首項下方的元素皆為 $0$。

### Reduced Row Echelon Form

矩陣若已為 row echelon form，並進一步符合下列條件，稱為 reduced row echelon form（簡約列梯形，RREF）：

4. 每個首項所在行的其他元素皆為 $0$。
5. 每個非零列的首項皆為 $1$。

RREF 中的首項 $1$ 稱為 pivot（樞紐）；包含 pivot 的行稱為 pivot column。

> **RREF 唯一性**
>
> 每個矩陣皆可經有限次初等列運算化為 RREF，而且所得 RREF 唯一。此定理的證明依講義留待 Sections 1.4 與 2.3。

一般的 row echelon form 不唯一；只有 RREF 對每個矩陣唯一。

## Basic and Free Variables

將增廣矩陣化為 $[R\mid\mathbf c]$ 的 RREF 後：

- $R$ 的 pivot columns 所對應的變數稱為 basic variables（基本變數）。
- $R$ 的 nonpivot columns 所對應的變數稱為 free variables（自由變數）。

若方程組 consistent，則可任意指定 free variables，再由各列求得 basic variables。故：

- 沒有 free variable 時，方程組有唯一解。
- 至少有一個 free variable 時，方程組有無限多解。

### Example: Infinitely Many Solutions

考慮 RREF 增廣矩陣

$$
\left[
\begin{array}{ccccc|c}
1&-3&0&2&0&7\cr
0&0&1&6&0&9\cr
0&0&0&0&1&2\cr
0&0&0&0&0&0
\end{array}
\right].
$$

$x_1,x_3,x_5$ 是 basic variables； $x_2,x_4$ 是 free variables。令 $x_2=s$、 $x_4=t$，則

$$
\begin{aligned}
x_1&=7+3s-2t,\cr
x_2&=s,\cr
x_3&=9-6t,\cr
x_4&=t,\cr
x_5&=2.
\end{aligned}
$$

一般解可寫為

$$
\mathbf x=
\begin{bmatrix}
7\cr 0\cr 9\cr 0\cr 2
\end{bmatrix}
+s
\begin{bmatrix}
3\cr 1\cr 0\cr 0\cr 0
\end{bmatrix}
+t
\begin{bmatrix}
-2\cr 0\cr -6\cr 1\cr 0
\end{bmatrix},
\qquad s,t\in\mathbb R.
$$

## Detecting Inconsistency

若增廣矩陣在列運算後出現

$$
\begin{bmatrix}0&0&\cdots&0\mid d\end{bmatrix},
\qquad d\ne0,
$$

則該列代表矛盾式 $0=d$，故原方程組無解。

例如，增廣矩陣

$$
\left[
\begin{array}{ccc|c}
1&0&-3&0\cr
0&1&2&0\cr
0&0&0&1\cr
0&0&0&0
\end{array}
\right]
$$

的第三列代表 $0=1$，因此此方程組 inconsistent。

## General Procedure for Solving $A\mathbf x=\mathbf b$

1. 寫出增廣矩陣 $[A\mid\mathbf b]$。
2. 以有限次初等列運算求得其 RREF $[R\mid\mathbf c]$。
3. 若出現 $[0\ \cdots\ 0\mid d]$ 且 $d\ne0$，則方程組無解。
4. 否則方程組至少有一解；辨認 basic 與 free variables，並以 free variables 表示 basic variables，即得一般解。

## Section Summary

- 線性方程組可寫成 $A\mathbf x=\mathbf b$，其資料可集中於增廣矩陣 $[A\mid\mathbf b]$。
- 解集合只有無解、唯一解或無限多解三種可能；consistent 表示至少有一解。
- 初等列運算可逆，因此不改變解集合，可用來產生等價方程組。
- 每個矩陣皆有唯一的 RREF；pivot columns 對應 basic variables，nonpivot columns 對應 free variables。
- 矛盾列 $[0\ \cdots\ 0\mid d]$（ $d\ne0$）表示無解；consistent 且含 free variables 時有無限多解。

## Practice

講義指定 Section 1.3 習題：1、3、5、7-22、55、57、59、61、63、65、67、69、71、73、75。

## Navigation

- 上一節：[1.2 Linear Combinations, Matrix-Vector Products, and Special Matrices](./01-02%20Linear%20Combinations,%20Matrix-Vector%20Products,%20and%20Special%20Matrices.md)
- 上層：[線性代數－蘇柏青](../../README.md)
- 下一節：[1.4 Gaussian Elimination](./01-04%20Gaussian%20Elimination.md)
