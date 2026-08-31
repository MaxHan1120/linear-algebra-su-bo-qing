---
aliases:
  - 1.1 Matrices and Vectors
  - 矩陣與向量
tags:
  - course/linear-algebra
  - linear-algebra/matrix
  - linear-algebra/vector
---

# 1.1 Matrices and Vectors

> [!info] 講義範圍
> `1_講義_Basic Concepts on Matrices and Vectors(1)(2)`，PDF 第 1–19 頁。

## Notation

- 本課程的 scalar（純量）皆屬於實數集合 $\mathbb R$。
- $\mathcal M_{m\times n}(\mathbb R)$：所有 $m\times n$ 實矩陣所成的集合；以下簡記為 $\mathcal M_{m\times n}$。
- 矩陣以大寫字母 $A,B,C$ 表示；向量以粗體小寫字母 $\mathbf u,\mathbf v$ 表示；scalar 以小寫字母 $s,t$ 表示。
- 若 $A\in\mathcal M_{m\times n}$，則

  $$
  A=[a_{ij}]_{m\times n}
  =\begin{bmatrix}
  a_{11}&\cdots&a_{1n}\\
  \vdots&\ddots&\vdots\\
  a_{m1}&\cdots&a_{mn}
  \end{bmatrix},
  $$

  其中 $a_{ij}$ 是第 $i$ 列、第 $j$ 行的元素（$(i,j)$-entry）。本文採「列 = row、行 = column」。

## Matrix

矩陣（matrix）是由 scalars 排成的矩形陣列。具有 $m$ 列、$n$ 行的矩陣，其 size 為 $m\times n$；若 $m=n$，則稱為方陣（square matrix）。

### Equality

兩矩陣相等，必須同時滿足尺寸相同且所有對應元素相等。對 $A,B\in\mathcal M_{m\times n}$，

$$
A=B
\iff
a_{ij}=b_{ij}, \quad \forall
\ i=1,\ldots,m,
\ j=1,\ldots,n.
$$

尺寸不同的矩陣不可能相等。

### Submatrix

從矩陣中刪除完整的一列或多列、完整的一行或多行，所得矩陣稱為原矩陣的子矩陣（submatrix）。

例如，刪除 $B$ 的第一列可得 $E$：

$$
B=\begin{bmatrix}6&8\\15&20\\45&64\end{bmatrix},
\qquad
E=\begin{bmatrix}15&20\\45&64\end{bmatrix}.
$$
故 $E$ 是 $B$ 的子矩陣。
## Entrywise Operations

以下運算皆以矩陣元素逐項定義。

### Addition

只有尺寸相同的矩陣才能相加。若 $A,B\in\mathcal M_{m\times n}$，則

$$
A+B=[a_{ij}+b_{ij}]_{m\times n}.
$$

### Scalar Multiplication

若 $s\in\mathbb R$ 且 $A\in\mathcal M_{m\times n}$，則

$$
sA=[sa_{ij}]_{m\times n}.
$$

### Zero Matrix and Subtraction

零矩陣 $O_{m\times n}$ 的所有元素皆為 $0$。尺寸已由上下文確定時可簡寫為 $O$，但不同尺寸的零矩陣不相等。

$$
A+O_{m\times n}=A,
\qquad
0A=O_{m\times n}.
$$

矩陣 $A$ 的加法反元素定義為 $-A=(-1)A$，因此

$$
A-B\coloneqq A+(-B).
$$

矩陣減法同樣只對尺寸相同的矩陣定義。

### Properties

若 $A,B,C\in\mathcal M_{m\times n}$，且 $s,t\in\mathbb R$，則

$$
\begin{aligned}
A+B&=B+A,\\
(A+B)+C&=A+(B+C),\\
A+O&=A,\\
A+(-A)&=O,\\
(st)A&=s(tA),\\
s(A+B)&=sA+sB,\\
(s+t)A&=sA+tA.
\end{aligned}
$$

這些性質由實數的算術律逐項成立，因此此處省略證明。

## Transpose

若 $A\in\mathcal M_{m\times n}$，其轉置（transpose）$A^T\in\mathcal M_{n\times m}$ 定義為

$$
(A^T)_{ij}=a_{ji}.
$$

也就是交換矩陣的列與行。若 $A,B\in\mathcal M_{m\times n}$ 且 $s\in\mathbb R$，則

$$
\begin{aligned}
(A+B)^T&=A^T+B^T,\\
(sA)^T&=sA^T,\\
(A^T)^T&=A.
\end{aligned}
$$

只有方陣才可能滿足 $A=A^T$；滿足此式的方陣稱為對稱矩陣（symmetric matrix）。

## Vector

- Row vector（列向量）是只有一列的矩陣，即 $1\times n$ 矩陣。
- Column vector（行向量）是只有一行的矩陣，即 $n\times1$ 矩陣。
- 除非特別說明，本課程的 vector 一律指 column vector。

所有具有 $n$ 個實數分量的 column vectors 所成的集合記為

$$
\mathbb R^n=\mathcal M_{n\times1}(\mathbb R).
$$

若 $\mathbf v\in\mathbb R^n$，則

$$
\mathbf v=
\begin{bmatrix}
v_1\\v_2\\\vdots\\v_n
\end{bmatrix},
$$

其中 $v_i$ 稱為 $\mathbf v$ 的第 $i$ 個分量（component）。向量加法與 scalar multiplication 沿用矩陣的逐項定義；零向量記為 $\mathbf 0\in\mathbb R^n$。

$$
\mathbf u+\mathbf 0=\mathbf u,
\qquad
0\mathbf u=\mathbf 0.
$$

## Matrix as a Collection of Vectors

任意 $C=[c_{ij}]\in\mathcal M_{m\times n}$ 可視為由 $n$ 個 column vectors 排成：

$$
C=\begin{bmatrix}\mathbf c_1&\cdots&\mathbf c_j&\cdots&\mathbf c_n\end{bmatrix},
\qquad
\mathbf c_j=
\begin{bmatrix}
c_{1j}\\c_{2j}\\\vdots\\c_{mj}
\end{bmatrix}
\in\mathbb R^m.
$$

同理，矩陣也可視為 $m$ 個 row vectors 疊成。

## Geometrical Interpretation

在 $\mathbb R^2$ 與 $\mathbb R^3$ 中，向量可由原點指向座標點來表示：

- $\mathbf u+\mathbf v$：依平行四邊形法則取得合向量。
- $s\mathbf v$：方向在 $s>0$ 時不變、在 $s<0$ 時反向，長度縮放為原來的 $|s|$ 倍。

## Section Summary

- 矩陣由 size 與 entries 描述；矩陣相等必須尺寸與所有對應元素皆相同。
- 加法、減法與 scalar multiplication 均逐項進行，其中加減法要求矩陣尺寸相同。
- 轉置會交換列與行，因此將 $m\times n$ 矩陣變為 $n\times m$ 矩陣。
- 本課程預設向量為 column vector，$\mathbb R^n=\mathcal M_{n\times1}(\mathbb R)$。

## Navigation

- 上層：[[README|線性代數－蘇柏青]]
- 下一節：[[01-02 Linear Combinations, Matrix-Vector Products, and Special Matrices|1.2 Linear Combinations, Matrix-Vector Products, and Special Matrices]]
