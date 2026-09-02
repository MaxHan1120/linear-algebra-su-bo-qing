---
aliases:
  - 4.5 Matrix Representations of Linear Operators
  - 線性算子的矩陣表示
tags:
  - course/linear-algebra
  - linear-algebra/linear-operator
  - linear-algebra/matrix-representation
  - linear-algebra/similarity
---

# 4.5 Matrix Representations of Linear Operators

> **講義範圍**
>
> `31_講義_Matrix Representations of Linear OperatorsⅠ`，PDF 第 1-10 頁。

## Linear Operators

linear operator on $\mathbb R^n$ 是 domain 與 codomain 相同的 linear transformation：

$$
T:\mathbb R^n\to\mathbb R^n.
$$

standard matrix 使用 standard basis 描述 $T$。本節則固定任意 ordered basis

$$
\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)
$$

並以 relative to $\mathcal B$ 的 coordinates 表示 $T$。

## Matrix Representation Relative to a Basis

$T$ relative to $\mathcal B$ 的 matrix representation，定義為

$$
[T]_{\mathcal B}=
\left[
[T(\mathbf b_1)]_{\mathcal B}\quad
[T(\mathbf b_2)]_{\mathcal B}\quad
\cdots\quad
[T(\mathbf b_n)]_{\mathcal B}
\right].
$$

也就是說，第 $j$ 個 column 是 $T(\mathbf b_j)$ relative to $\mathcal B$ 的 coordinate vector。

若 $\mathcal B=\mathcal E$ 是 standard basis，則

$$
[T]_{\mathcal E}=
[T(\mathbf e_1)\quad T(\mathbf e_2)\quad\cdots\quad T(\mathbf e_n)],
$$

這正是 $T$ 的 standard matrix。

## Coordinate Action of the Matrix

對任意 $\mathbf v\in\mathbb R^n$，

$$
[T(\mathbf v)]_{\mathcal B}
=[T]_{\mathcal B}[\mathbf v]_{\mathcal B}.
$$

因此 $[T]_{\mathcal B}$ 的作用對象是 relative to $\mathcal B$ 的 coordinate vectors，而不是未經轉換的 standard-coordinate vectors。

## Direct Computation of the Matrix Representation

若已知 $T$ 與 basis $\mathcal B$，可依下列步驟計算：

1. 對每個 basis vector 求 $T(\mathbf b_j)$。
2. 解出 $T(\mathbf b_j)$ relative to $\mathcal B$ 的 coordinates。
3. 依序把這些 coordinate vectors 排成 columns。

令

$$
B=[\mathbf b_1\ \mathbf b_2\ \cdots\ \mathbf b_n].
$$

則第二步可寫成

$$
[T(\mathbf b_j)]_{\mathcal B}=B^{-1}T(\mathbf b_j).
$$

## Theorem 4.12: Change of Basis for an Operator

令 $A$ 是 $T$ 的 standard matrix， $B$ 是 ordered basis $\mathcal B$ 的 basis matrix，則

$$
[T]_{\mathcal B}=B^{-1}AB.
$$

等價地，

$$
A=B[T]_{\mathcal B}B^{-1}.
$$

**Proof.** 因為 $T(\mathbf b_j)=A\mathbf b_j$，所以

$$
[T]_{\mathcal B}=
\left[
B^{-1}A\mathbf b_1\quad
\cdots\quad
B^{-1}A\mathbf b_n
\right]
=B^{-1}AB.
$$

這表示 $A$ 與 $[T]_{\mathcal B}$ 描述的是同一個 linear operator，只是採用不同的 coordinate systems。

## Similar Matrices

對 $A,C\in\mathcal M_{n\times n}$，若存在 invertible matrix $P$ 使得

$$
C=P^{-1}AP,
$$

則稱 $A$ 與 $C$ similar。

Similarity 是對稱關係：若 $C=P^{-1}AP$，則

$$
A=PCP^{-1}.
$$

因此，同一 linear operator 在不同 bases 下的 matrix representations 彼此 similar。

## Images of a Basis Determine the Operator

若 $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$ 是 $\mathbb R^n$ 的 basis，則指定

$$
T(\mathbf b_1),\ldots,T(\mathbf b_n)
$$

即可唯一決定 linear operator $T$。

因為任意向量都可唯一寫成

$$
\mathbf v=c_1\mathbf b_1+\cdots+c_n\mathbf b_n,
$$

利用 linearity，必有

$$
T(\mathbf v)
=c_1T(\mathbf b_1)+\cdots+c_nT(\mathbf b_n).
$$

## Example: Reflection About a Line

考慮 $\mathbb R^2$ 中通過原點的直線 $L$。取 $\mathbf b_1$ 沿著 $L$， $\mathbf b_2$ 垂直於 $L$，則 reflection operator $T$ 滿足

$$
T(\mathbf b_1)=\mathbf b_1,
\qquad
T(\mathbf b_2)=-\mathbf b_2.
$$

因此

$$
[T]_{\mathcal B}=
\left[
\begin{array}{rr}
1&0\cr
0&-1
\end{array}
\right].
$$

若 $L$ 為 $y=\frac12x$，可取

$$
B=
\left[
\begin{array}{rr}
2&-1\cr
1&2
\end{array}
\right].
$$

則 standard matrix 為

$$
A
=B[T]_{\mathcal B}B^{-1}=
\left[
\begin{array}{rr}
\frac35&\frac45\cr
\frac45&-\frac35
\end{array}
\right].
$$

在適合幾何結構的 basis 中，operator 的 matrix 往往比 standard matrix 更簡單。

## Common Pitfalls

- Matrix representation 的第 $j$ 個 column 是 $[T(\mathbf b_j)]_{\mathcal B}$，不是 $T(\mathbf e_j)$。
- Matrix representation 應乘上 coordinate vector $[\mathbf v]_{\mathcal B}$，不能直接與不同 coordinate system 的向量混用。
- 公式順序不可交換： $[T]_{\mathcal B}=B^{-1}AB$，不是 $BAB^{-1}$。
- Similar matrices 通常不相等，但代表同一 operator 在不同 bases 下的描述。
- Basis 的排列順序改變時，basis matrix 與 matrix representation 都會改變。

## Assigned Exercises

Section 4.5：Problems 1, 3, 7, 9, 13, 15, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37。

---

- 上一篇：[4.4 Coordinate Systems](./04-04%20Coordinate%20Systems.md)
- 上層：[線性代數－蘇柏青](../../README.md)
