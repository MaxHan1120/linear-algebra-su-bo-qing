---
aliases:
  - 7.4 Matrix Representation of Linear Operators
  - 抽象線性算子的矩陣表示
tags:
  - course/linear-algebra
  - linear-algebra/abstract-matrix-representation
  - linear-algebra/coordinate-map
---

# 7.4 Matrix Representation of Linear Operators

> **講義範圍**
>
> `59_講義_Matrix Representations of Linear OperatorsⅡ(1)`，PDF 第 1-19 頁。

## Coordinate Map

令 $V$ 是 dimension 為 $n$ 的 vector space，且

$$
\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)
$$

是 ordered basis。若

$$
\mathbf v=c_1\mathbf b_1+\cdots+c_n\mathbf b_n,
$$

定義

$$
[\mathbf v]_{\mathcal B}=
\left[
\begin{array}{c}
c_1\cr
\vdots\cr
c_n
\end{array}
\right],
$$

以及 coordinate map

$$
\Phi_{\mathcal B}:V\to\mathbb F^n,
\qquad
\Phi_{\mathcal B}(\mathbf v)=[\mathbf v]_{\mathcal B}.
$$

$\Phi_{\mathcal B}$ 是 isomorphism，且

$$
[\mathbf u+\mathbf v]_{\mathcal B}
=[\mathbf u]_{\mathcal B}+[\mathbf v]_{\mathcal B},
$$

$$
[c\mathbf u]_{\mathcal B}=c[\mathbf u]_{\mathcal B}.
$$

## Matrix Representation of an Operator

令 $T:V\to V$ 是 linear operator。Relative to $\mathcal B$ 的 matrix representation 定義為 coordinate-space operator

$$
\Phi_{\mathcal B}\circ T\circ\Phi_{\mathcal B}^{-1}
$$

的 standard matrix，記為 $[T]_{\mathcal B}$。

## Column Formula

$$
[T]_{\mathcal B}=
\left[
[T(\mathbf b_1)]_{\mathcal B}\quad
\cdots\quad
[T(\mathbf b_n)]_{\mathcal B}
\right].
$$

也就是先對 basis vectors 作用 $T$，再把結果寫成 relative to $\mathcal B$ 的 coordinates。

### Example: Differentiation on the Polynomial Space

對 $D:\mathcal P_2\to\mathcal P_2$， $D(p)=p^{\prime}$，取

$$
\mathcal B=(1,x,x^2),
$$

則

$$
[D]_{\mathcal B}=
\left[
\begin{array}{ccc}
0&1&0\cr
0&0&2\cr
0&0&0
\end{array}
\right].
$$

## Theorem 7.10

對所有 $\mathbf v\in V$，

$$
[T(\mathbf v)]_{\mathcal B}
=[T]_{\mathcal B}[\mathbf v]_{\mathcal B}.
$$

這使抽象 operator 的計算轉化為 ordinary matrix multiplication。

## Invertibility

$T$ invertible，若且唯若 $[T]_{\mathcal B}$ invertible。此時

$$
[T^{-1}]_{\mathcal B}
=([T]_{\mathcal B})^{-1}.
$$

## Eigenvalues and Eigenvectors

Nonzero vector $\mathbf v\in V$ 稱為 $T$ 的 eigenvector，若

$$
T(\mathbf v)=\lambda\mathbf v.
$$

令 $A=[T]_{\mathcal B}$，則

$$
T(\mathbf v)=\lambda\mathbf v
\iff
A[\mathbf v]_{\mathcal B}
=\lambda[\mathbf v]_{\mathcal B}.
$$

因此 $T$ 與任一 matrix representation 具有相同 eigenvalues；operator eigenspace 經 coordinate map 對應至 matrix eigenspace。

例如 transpose operator

$$
U:\mathcal M_{n\times n}\to\mathcal M_{n\times n},
\qquad
U(A)=A^T
$$

的 eigenvalue $1$ eigenspace 是 symmetric matrices，eigenvalue $-1$ eigenspace 是 skew-symmetric matrices。

## Common Pitfalls

- $[T]_{\mathcal B}$ 的 columns 是 output coordinates，不是抽象 vectors 本身。
- Basis 必須 ordered；改變順序會改變 matrix representation。
- Output coordinate vector $[T(\mathbf v)]_{\mathcal B}$ 與直接把 $T$ 作用於 coordinate vector 不同；後者通常沒有定義。
- Operator 與 matrix 的 eigenvectors 透過 coordinate map 對應，而不是字面上相同物件。

## Assigned Exercises

Section 7.4：Problems 1, 5, 9, 11, 19, 21, 23, 28, 32, 36, 39, 40, 43, 44, 46。

---

- 上一篇：[7.3 Basis and Dimension](./07-03%20Basis%20and%20Dimension.md)
- 下一篇：[7.5 Inner Product Spaces](./07-05%20Inner%20Product%20Spaces.md)
- 上層：[線性代數－蘇柏青](../../README.md)
