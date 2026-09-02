---
aliases:
  - 4.4 Coordinate Systems
  - 座標系統
tags:
  - course/linear-algebra
  - linear-algebra/coordinates
  - linear-algebra/basis
  - linear-algebra/change-of-basis
---

# 4.4 Coordinate Systems

> **講義範圍**
>
> `30_講義_Coordinate Systems`，PDF 第 1-11 頁。

## Theorem 4.10: Unique Representation Relative to a Basis

令

$$
\mathcal B=\{\mathbf b_1,\ldots,\mathbf b_k\}
$$

是 subspace $V\subseteq\mathbb R^n$ 的 basis。對每個 $\mathbf v\in V$，存在唯一的 scalars $c_1,\ldots,c_k$，使得

$$
\mathbf v
=c_1\mathbf b_1+\cdots+c_k\mathbf b_k.
$$

**Proof.** 因為 $\mathcal B$ spans $V$，representation 必存在。若同時有

$$
\mathbf v
=c_1\mathbf b_1+\cdots+c_k\mathbf b_k
=d_1\mathbf b_1+\cdots+d_k\mathbf b_k,
$$

則

$$
(c_1-d_1)\mathbf b_1+\cdots+(c_k-d_k)\mathbf b_k=\mathbf0.
$$

由 $\mathcal B$ 為 L.I.，可得 $c_i=d_i$ 對所有 $i$ 成立，因此 representation 唯一。

## Ordered Basis and Coordinate Vector

使用座標時，basis 中向量的順序不可忽略。以下將

$$
\mathcal B=(\mathbf b_1,\ldots,\mathbf b_k)
$$

視為 ordered basis。

若

$$
\mathbf v=c_1\mathbf b_1+\cdots+c_k\mathbf b_k,
$$

則 $\mathbf v$ relative to $\mathcal B$ 的 coordinate vector 定義為

$$
[\mathbf v]_{\mathcal B}=
\left[
\begin{array}{c}
c_1\cr
\vdots\cr
c_k
\end{array}
\right]
\in\mathbb R^k.
$$

改變 basis 的排列順序，coordinate vector 的 entries 也會跟著改變。

## Standard Coordinates

對 $\mathbb R^n$ 的 standard basis

$$
\mathcal E=(\mathbf e_1,\ldots,\mathbf e_n),
$$

任意 $\mathbf v\in\mathbb R^n$ 滿足

$$
[\mathbf v]_{\mathcal E}=\mathbf v.
$$

而 basis vector 本身的 $\mathcal B$-coordinates 為

$$
[\mathbf b_i]_{\mathcal B}=\mathbf e_i.
$$

## Basis Matrix

令 $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$ 是 $\mathbb R^n$ 的 ordered basis，定義 basis matrix

$$
B=[\mathbf b_1\ \mathbf b_2\ \cdots\ \mathbf b_n].
$$

因為 $B$ 的 columns 為 L.I.，所以 $B$ 可逆。

由 coordinate vector 的定義，

$$
\mathbf v=B[\mathbf v]_{\mathcal B}.
$$

這個公式把 $\mathcal B$-coordinates 轉回 standard coordinates。

## Theorem 4.11: Computing Coordinates

對每個 $\mathbf v\in\mathbb R^n$，

$$
[\mathbf v]_{\mathcal B}=B^{-1}\mathbf v.
$$

因此：

- $B$：由 $\mathcal B$-coordinates 轉為 standard coordinates；
- $B^{-1}$：由 standard coordinates 轉為 $\mathcal B$-coordinates。

### Example

令

$$
B=
\left[
\begin{array}{rrr}
1&1&1\cr
1&-1&2\cr
1&1&2
\end{array}
\right],
\qquad
\mathbf v=
\left[
\begin{array}{r}
1\cr-4\cr4
\end{array}
\right].
$$

解

$$
B\mathbf c=\mathbf v
$$

可得

$$
[\mathbf v]_{\mathcal B}
=\mathbf c=
\left[
\begin{array}{r}
-6\cr4\cr3
\end{array}
\right].
$$

## Orthonormal Basis as a Special Case

若 $\mathcal B$ 是 orthonormal basis，則 basis matrix $B$ 為 orthogonal matrix，故

$$
B^{-1}=B^T.
$$

此時

$$
[\mathbf v]_{\mathcal B}=B^T\mathbf v.
$$

這常用於旋轉座標軸，把傾斜圖形在新座標系中寫成較簡單的方程式。

## Coordinate Map

固定 ordered basis $\mathcal B$ 後，定義

$$
C_{\mathcal B}:V\to\mathbb R^k,
\qquad
C_{\mathcal B}(\mathbf v)=[\mathbf v]_{\mathcal B}.
$$

由 coordinate representation 的唯一性， $C_{\mathcal B}$ 是 one-to-one 且 onto；並且

$$
[a\mathbf u+b\mathbf v]_{\mathcal B}
=a[\mathbf u]_{\mathcal B}+b[\mathbf v]_{\mathcal B}.
$$

所以選定 basis 後， $V$ 中的向量運算可等價地轉成 $\mathbb R^k$ 中的 coordinate 運算。

## Common Pitfalls

- $\mathbf v$ 與 $[\mathbf v]_{\mathcal B}$ 表示同一抽象向量，但屬於不同的 coordinate descriptions，不應直接混用。
- $B$ 的 columns 必須依 ordered basis 的順序排列。
- $B\mathbf v$ 通常不是 $[\mathbf v]_{\mathcal B}$；正確公式是 $B^{-1}\mathbf v$。
- 只有當 $B$ 為 orthogonal matrix 時，才可用 $B^T$ 取代 $B^{-1}$。

## Assigned Exercises

Section 4.4：Problems 1, 5, 7, 9, 11, 13, 15, 19, 23, 27, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49。

---

- 上一篇：[4.3 The Dimension of Subspaces Associated with a Matrix](./04-03%20The%20Dimension%20of%20Subspaces%20Associated%20with%20a%20Matrix.md)
- 下一篇：[4.5 Matrix Representations of Linear Operators](./04-05%20Matrix%20Representations%20of%20Linear%20Operators.md)
- 上層：[線性代數－蘇柏青](../../README.md)
