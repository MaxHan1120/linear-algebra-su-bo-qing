---
aliases:
  - 1.2 Linear Combinations, Matrix-Vector Products, and Special Matrices
  - 線性組合、矩陣向量乘積與特殊矩陣
tags:
  - course/linear-algebra
  - linear-algebra/linear-combination
  - linear-algebra/matrix-vector-product
---

# 1.2 Linear Combinations, Matrix-Vector Products, and Special Matrices

> [!info] 講義範圍
> `1_講義_Basic Concepts on Matrices and Vectors(1)(2)`，PDF 第 20–33 頁。

## Notation

- 沿用 [[01-01 Matrices and Vectors|1.1 Matrices and Vectors]]：vector 一律指 column vector，並以粗體小寫字母表示。
- 若 $A\in\mathcal M_{m\times n}$，將其 columns 記為 $\mathbf a_1,\ldots,\mathbf a_n\in\mathbb R^m$：
  $$
  A=\begin{bmatrix}\mathbf a_1&\mathbf a_2&\cdots&\mathbf a_n\end{bmatrix}.
  $$

- $\mathbf e_j\in\mathbb R^n$ 表示第 $j$ 個 standard vector。
- $\mathbf 0_n$、$\mathbf 0_m$ 分別表示 $\mathbb R^n$、$\mathbb R^m$ 中的 zero vector。

## Linear Combination

給定 $\mathbf u_1,\ldots,\mathbf u_k\in\mathbb R^n$ 與 scalars $c_1,\ldots,c_k\in\mathbb R$，形如

$$
c_1\mathbf u_1+c_2\mathbf u_2+\cdots+c_k\mathbf u_k
$$

的向量稱為 $\mathbf u_1,\ldots,\mathbf u_k$ 的線性組合（linear combination），其中 $c_1,\ldots,c_k$ 稱為 coefficients。

例如，

$$
\begin{bmatrix}2\\8\end{bmatrix}
=-3\begin{bmatrix}1\\1\end{bmatrix}
+4\begin{bmatrix}1\\3\end{bmatrix}
+\begin{bmatrix}1\\-1\end{bmatrix}.
$$

已知 coefficients 時，只需進行 scalar multiplication 與 vector addition。反過來，若要判斷 $\mathbf b$ 能否寫成給定向量的線性組合，便須求解

$$
\mathbf b=x_1\mathbf u_1+\cdots+x_k\mathbf u_k.
$$

此問題等價於一組 linear equations，可能有以下三種結果：

- 唯一解：$\mathbf b$ 有唯一一種線性組合表示。
- 無限多解：$\mathbf b$ 有多種線性組合表示。
- 無解：$\mathbf b$ 不是這些向量的線性組合。

### Example: Unique Representation

$$
\begin{bmatrix}4\\-1\end{bmatrix}
=x_1\begin{bmatrix}2\\3\end{bmatrix}
+x_2\begin{bmatrix}3\\1\end{bmatrix}
$$

對應方程組有唯一解 $x_1=-1$、$x_2=2$，因此

$$
\begin{bmatrix}4\\-1\end{bmatrix}
=-\begin{bmatrix}2\\3\end{bmatrix}
+2\begin{bmatrix}3\\1\end{bmatrix}.
$$

### Geometrical Interpretation in $\mathbb R^2$

若 $\mathbf u,\mathbf v\in\mathbb R^2$ 皆非零且不平行，亦即不存在 $c\in\mathbb R$ 使 $\mathbf u=c\mathbf v$，則每個 $\mathbf w\in\mathbb R^2$ 都能唯一寫成

$$
\mathbf w=a\mathbf u+b\mathbf v.
$$

幾何上，$a\mathbf u$ 與 $b\mathbf v$ 構成以 $\mathbf w$ 為對角線的平行四邊形。若 $\mathbf u$ 與 $\mathbf v$ 平行，則它們只能產生同一直線上的向量；此時表示可能不存在，也可能不唯一。

## Standard Vectors

$\mathbb R^n$ 的 standard vectors 定義為

$$
\mathbf e_1=
\begin{bmatrix}1\\0\\\vdots\\0\end{bmatrix},
\quad
\mathbf e_2=
\begin{bmatrix}0\\1\\\vdots\\0\end{bmatrix},
\quad\ldots\quad,
\mathbf e_n=
\begin{bmatrix}0\\0\\\vdots\\1\end{bmatrix}.
$$

等價地，$\mathbf e_j$ 的第 $i$ 個 component 為

$$
(\mathbf e_j)_i=\delta_{ij}
=\begin{cases}
1,&i=j,\\
0,&i\ne j.
\end{cases}
$$

任意 $\mathbf v=[v_1,\ldots,v_n]^T\in\mathbb R^n$ 均有唯一表示

$$
\mathbf v=v_1\mathbf e_1+v_2\mathbf e_2+\cdots+v_n\mathbf e_n.
$$

## Matrix-Vector Product

令

$$
A=\begin{bmatrix}\mathbf a_1&\cdots&\mathbf a_n\end{bmatrix}
\in\mathcal M_{m\times n},
\qquad
\mathbf v=
\begin{bmatrix}v_1\\\vdots\\v_n\end{bmatrix}
\in\mathbb R^n.
$$

矩陣向量乘積（matrix-vector product）定義為 $A$ 的 columns 以 $\mathbf v$ 的 components 為 coefficients 所形成的線性組合：

$$
A\mathbf v
\coloneqq
v_1\mathbf a_1+v_2\mathbf a_2+\cdots+v_n\mathbf a_n
\in\mathbb R^m.
$$

因此，$A\mathbf v$ 有定義的必要條件是 $A$ 的 column 數等於 $\mathbf v$ 的 component 數。

### Entrywise Formula

若 $A=[a_{ij}]\in\mathcal M_{m\times n}$，則

$$
A\mathbf v=
\begin{bmatrix}
\sum_{j=1}^n a_{1j}v_j\\
\sum_{j=1}^n a_{2j}v_j\\
\vdots\\
\sum_{j=1}^n a_{mj}v_j
\end{bmatrix}.
$$

換言之，$A\mathbf v$ 的第 $i$ 個 component 是 $A$ 的第 $i$ 列與 $\mathbf v$ 的逐項乘積和：

$$
(A\mathbf v)_i=\sum_{j=1}^n a_{ij}v_j,
\qquad i=1,\ldots,m.
$$

### Example

令

$$
A=\begin{bmatrix}1&2\\3&4\\5&6\end{bmatrix},
\qquad
\mathbf v=\begin{bmatrix}7\\8\end{bmatrix}.
$$

則

$$
A\mathbf v
=7\begin{bmatrix}1\\3\\5\end{bmatrix}
+8\begin{bmatrix}2\\4\\6\end{bmatrix}
=\begin{bmatrix}23\\53\\83\end{bmatrix}.
$$

## Special Matrices

### Identity Matrix

對每個正整數 $n$，$n\times n$ identity matrix 定義為

$$
I_n=
\begin{bmatrix}
1&0&\cdots&0\\
0&1&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&1
\end{bmatrix}
=\begin{bmatrix}\mathbf e_1&\mathbf e_2&\cdots&\mathbf e_n\end{bmatrix}.
$$

因此，對所有 $\mathbf v\in\mathbb R^n$，

$$
I_n\mathbf v=\mathbf v.
$$

尺寸由上下文唯一決定時，可將 $I_n$ 簡寫為 $I$。

### Stochastic Matrix

若 $A=[a_{ij}]\in\mathcal M_{n\times n}$ 滿足

$$
a_{ij}\ge 0,
\qquad
\sum_{i=1}^n a_{ij}=1
\quad (j=1,\ldots,n),
$$

則稱 $A$ 為 stochastic matrix。此講義採用 column-stochastic convention：每一個 column 的元素總和皆為 $1$。

例如，

$$
A=\begin{bmatrix}
0.85&0.03\\
0.15&0.97
\end{bmatrix}
$$

是 stochastic matrix。若

$$
\mathbf p=\begin{bmatrix}500\\700\end{bmatrix}
$$

表示目前 city 與 suburbs 的人口（千人），則下一期人口分布為

$$
A\mathbf p
=\begin{bmatrix}
0.85(500)+0.03(700)\\
0.15(500)+0.97(700)
\end{bmatrix}
=\begin{bmatrix}446\\754\end{bmatrix}.
$$

再下一期則為 $A(A\mathbf p)$。

### Rotation Matrix

在 $\mathbb R^2$ 中，將向量逆時針旋轉 $\theta$ 的 rotation matrix 為

$$
A_\theta=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
$$

若 $\mathbf p=[x,y]^T$，則

$$
A_\theta\mathbf p
=\begin{bmatrix}
x\cos\theta-y\sin\theta\\
x\sin\theta+y\cos\theta
\end{bmatrix}.
$$

![[Pasted image 20260831161500.png|center|]]
$A_\theta$ 的 columns 是標準基底旋轉 $\theta$ 後的向量 $\mathbf w_1,\mathbf w_2$。因此，旋轉後的向量 $\mathbf p'=A_\theta\mathbf p$ 可寫成 $\mathbf p'=x\mathbf w_1+y\mathbf w_2$。
$$
A_{\theta}\mathbf{p}
=
x
\begin{bmatrix}
\cos\theta \\
\sin\theta
\end{bmatrix}
+
y
\begin{bmatrix}
-\sin\theta \\
\cos\theta
\end{bmatrix}
=x\ \mathbf{w_{1}}+y\ \mathbf{w_{2}}
$$



## Properties of Matrix-Vector Products

令 $A,B\in\mathcal M_{m\times n}$、$\mathbf u,\mathbf v,\mathbf w\in\mathbb R^n$，且 $c\in\mathbb R$。則：

$$
\begin{aligned}
A(\mathbf u+\mathbf v)&=A\mathbf u+A\mathbf v,\\
A(c\mathbf u)&=c(A\mathbf u)=(cA)\mathbf u,\\
(A+B)\mathbf u&=A\mathbf u+B\mathbf u,\\
A\mathbf e_j&=\mathbf a_j,\qquad j=1,\ldots,n.
\end{aligned}
$$

其中最後一式表示：右乘第 $j$ 個 standard vector 會選出 $A$ 的第 $j$ 個 column。

此外：

$$
\begin{aligned}
B\mathbf w=A\mathbf w\ \text{for all }\mathbf w\in\mathbb R^n
&\implies B=A,\\
A\mathbf 0_n&=\mathbf 0_m,\\
O_{m\times n}\mathbf v&=\mathbf 0_m,\\
I_n\mathbf v&=\mathbf v.
\end{aligned}
$$

上述等式皆可直接由 matrix-vector product 的定義逐項驗證。命題 $B\mathbf w=A\mathbf w$ 對所有 $\mathbf w\in\mathbb R^n$ 成立時，可取 $\mathbf w=\mathbf e_j$：此時 $B\mathbf e_j=A\mathbf e_j$ 對每個 $j$ 都成立，所以 $A$ 與 $B$ 的每個 column 皆相同，故 $A=B$。

## Section Summary

- Linear combination 是以 scalars 加權後相加；求 coefficients 等價於求解 linear equations。
- Standard vectors 可唯一表示 $\mathbb R^n$ 中的任意向量。
- $A\mathbf v$ 是 $A$ 的 columns 以 $\mathbf v$ 的 components 為 coefficients 所形成的線性組合。
- $A\mathbf e_j=\mathbf a_j$，因此矩陣對所有向量的作用能唯一決定該矩陣。
- Identity、stochastic 與 rotation matrices 分別描述不變映射、狀態轉移與平面旋轉。

## Practice

講義指定 Section 1.2 習題：3、5、8、9、15、34、42、44、83-87。

## Navigation

- 上一節：[[01-01 Matrices and Vectors|1.1 Matrices and Vectors]]
- 上層：[[README|線性代數－蘇柏青]]
- 下一節：[[01-03 Systems of Linear Equations|1.3 Systems of Linear Equations]]
