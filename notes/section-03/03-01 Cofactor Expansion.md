---
aliases:
  - 3.1 Cofactor Expansion
  - 餘因子展開
tags:
  - course/linear-algebra
  - linear-algebra/determinant
  - linear-algebra/cofactor-expansion
---

# 3.1 Cofactor Expansion

> **講義範圍**
>
> `24_講義_Determinants(1)(1)`，PDF 第 1-15 頁。

## Notation

- 本節只考慮方陣 $A=[a_{ij}]\in\mathcal M_{n\times n}$。
- $\det(A)$ 表示 $A$ 的 determinant（行列式），其值為 scalar。
- $A_{ij}$ 表示從 $A$ 刪除第 $i$ row 與第 $j$ column 後得到的 $(n-1)\times(n-1)$ submatrix。
- $c_{ij}$ 表示 entry $a_{ij}$ 的 cofactor。

determinant 可用來判斷方陣是否 invertible，之後也會用於 characteristic polynomial 與 eigenvalues。

## Minor and Cofactor

entry $a_{ij}$ 的 minor 是

$$
M_{ij}=\det(A_{ij}).
$$

其 cofactor 定義為

$$
c_{ij}=(-1)^{i+j}M_{ij}=(-1)^{i+j}\det(A_{ij}).
$$

cofactor 的正負號依 checkerboard pattern 排列：

$$
\left[
\begin{array}{rrrrr}
+&-&+&-&\cdots\cr
-&+&-&+&\cdots\cr
+&-&+&-&\cdots\cr
\vdots&\vdots&\vdots&\vdots&\ddots
\end{array}
\right].
$$

## Recursive Definition of the Determinant

若 $n=1$，則

$$
\det([a_{11}])=a_{11}.
$$

若 $n>1$，沿第一列展開定義

$$
\det(A)
=a_{11}c_{11}+a_{12}c_{12}+\cdots+a_{1n}c_{1n}.
$$

對 $2\times2$ 矩陣，

$$
\det
\left(
\left[
\begin{array}{cc}
a&b\cr
c&d
\end{array}
\right]
\right)
=ad-bc.
$$

對 $2\times2$ 矩陣而言，

$$
\det(A)=0
$$

恰好表示 $A$ 不可逆；一般 $n\times n$ 方陣的完整等價關係會在 [3.2 Properties of Determinants](./03-02%20Properties%20of%20Determinants.md) 建立。

## Example: A $3\times3$ Determinant

令

$$
A=
\left[
\begin{array}{ccc}
a_{11}&a_{12}&a_{13}\cr
a_{21}&a_{22}&a_{23}\cr
a_{31}&a_{32}&a_{33}
\end{array}
\right].
$$

沿第一列展開：

$$
\det(A)
=a_{11}
\left|
\begin{array}{cc}
a_{22}&a_{23}\cr
a_{32}&a_{33}
\end{array}
\right|
-a_{12}
\left|
\begin{array}{cc}
a_{21}&a_{23}\cr
a_{31}&a_{33}
\end{array}
\right|
+a_{13}
\left|
\begin{array}{cc}
a_{21}&a_{22}\cr
a_{31}&a_{32}
\end{array}
\right|.
$$

展開後共有六項，其中三項為正、三項為負。

## Theorem 3.1: Cofactor Expansion Along Any Row

對任意 $i\in\{1,\ldots,n\}$，

$$
\det(A)=a_{i1}c_{i1}+a_{i2}c_{i2}+\cdots+a_{in}c_{in}.
$$

因此可以沿任意 row 做 cofactor expansion；計算時應優先選擇含最多 zeros 的 row，以減少需要計算的 minors。

**Proof idea.** 對矩陣大小 $n$ 做 induction。將每個 $c_{ij}$ 再沿固定 row 展開，重新整理後可還原第一列展開的定義，因此不同 rows 的展開結果相同。

## Sparse Expansion Strategy

若某個 row 只有一個 nonzero entry $a_{ij}$，則

$$
\det(A)=a_{ij}c_{ij}
=(-1)^{i+j}a_{ij}\det(A_{ij}).
$$

此時 $n\times n$ determinant 可直接降為一個 $(n-1)\times(n-1)$ determinant。若矩陣本身不稀疏，可先利用 [3.2](./03-02%20Properties%20of%20Determinants.md) 的 row operations 製造 zeros，再展開。

## Computational Complexity

直接對一般 dense matrix 反覆做 cofactor expansion，運算量至少以 factorial order 成長：

$$
\text{work}(n)=\Theta(n!).
$$

所以 cofactor expansion 適合：

- 小型矩陣。
- 含大量 zeros 的矩陣。
- 理論推導與 symbolic computation。

對大型 dense matrices，Gaussian elimination 更有效率。

## Triangular Matrices

$A$ 稱為 upper triangular，若

$$
a_{ij}=0\qquad(i>j).
$$

$A$ 稱為 lower triangular，若

$$
a_{ij}=0\qquad(i<j).
$$

### Theorem 3.2

若 $A$ 是 upper triangular 或 lower triangular，則

$$
\det(A)=a_{11}a_{22}\cdots a_{nn}.
$$

**Proof idea.** 沿含有最多 zeros 的第一 column 或第一 row 展開，將問題遞迴降階，最後只留下 diagonal entries 的乘積。

### Corollaries

1. $\det(I_n)=1$。
2. triangular matrix $A$ 可逆，若且唯若所有 diagonal entries 皆非零：

$$
A\text{ is invertible}
\iff
a_{11}a_{22}\cdots a_{nn}\ne0.
$$

## Common Pitfalls

- $A_{ij}$ 是刪除 row $i$ 與 column $j$ 後的 submatrix，不包含 $a_{ij}$。
- minor $M_{ij}$ 與 cofactor $c_{ij}$ 相差 sign factor $(-1)^{i+j}$。
- cofactor expansion 的 signs 必須依 entry 的位置決定，不是固定從正號開始。
- 一般矩陣的 determinant 不是 diagonal entries 的乘積；此結論只直接適用於 triangular matrices。

## Assigned Exercises

Section 3.1：Problems 1, 2, 9, 12, 14, 15, 37, 44。

---

- 上一篇：[2.8 Composition and Invertibility of Linear Transformations](../section-02/02-08%20Composition%20and%20Invertibility%20of%20Linear%20Transformations.md)
- 下一篇：[3.2 Properties of Determinants](./03-02%20Properties%20of%20Determinants.md)
- 上層：[線性代數－蘇柏青](../../README.md)
