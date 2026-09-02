---
aliases:
  - 5.1 Eigenvalues and Eigenvectors
  - 特徵值與特徵向量
tags:
  - course/linear-algebra
  - linear-algebra/eigenvalue
  - linear-algebra/eigenspace
---

# 5.1 Eigenvalues and Eigenvectors

> **講義範圍**
>
> `32_講義_Eigenvalues, Eigenvectors, and Diagonalization`，PDF 第 1-8 頁。

## Eigenvalues and Eigenvectors of an Operator

令 $T:\mathbb R^n\to\mathbb R^n$ 為 linear operator。若 nonzero vector $\mathbf v$ 滿足

$$
T(\mathbf v)=\lambda\mathbf v
$$

其中 $\lambda\in\mathbb R$，則稱 $\mathbf v$ 是 $T$ 對應於 $\lambda$ 的 eigenvector， $\lambda$ 是對應的 eigenvalue。

Eigenvector 經 $T$ 作用後方向不變，只會被縮放；若 $\lambda<0$，方向同時反轉。定義中必須要求 $\mathbf v\neq\mathbf0$，否則 zero vector 對任意 $\lambda$ 都成立。

在某些問題中需將 scalars 與 vectors 擴充至 $\mathbb C$，因為 real matrix 不一定具有 real eigenvalues。

## Eigenvalues and Eigenvectors of a Matrix

令 $A\in\mathcal M_{n\times n}$。若 nonzero vector $\mathbf v$ 滿足

$$
A\mathbf v=\lambda\mathbf v,
$$

則稱 $\mathbf v$ 是 $A$ 對應於 $\lambda$ 的 eigenvector。

若 $A$ 是 $T$ 的 standard matrix，則

$$
T(\mathbf v)=\lambda\mathbf v
\iff
A\mathbf v=\lambda\mathbf v.
$$

因此 operator 與其 standard matrix 具有相同的 eigenvalues 與 eigenvectors。

## The Eigenvalue Equation

將 $A\mathbf v=\lambda\mathbf v$ 改寫為

$$
(A-\lambda I_n)\mathbf v=\mathbf0.
$$

所以 $\lambda$ 是 eigenvalue，恰好等價於 homogeneous system

$$
(A-\lambda I_n)\mathbf x=\mathbf0
$$

具有 nontrivial solution。

對固定的 eigenvector，其 eigenvalue 唯一；但固定的 eigenvalue 通常對應無限多個 eigenvectors，因為 eigenvector 的任意 nonzero scalar multiple 仍是 eigenvector。

## Eigenspace

$A$ 對應於 eigenvalue $\lambda$ 的 eigenspace 定義為

$$
E_\lambda(A)
=\mathrm{Null}(A-\lambda I_n).
$$

它包含 zero vector，以及所有對應於 $\lambda$ 的 eigenvectors。因為 null space 是 subspace， $E_\lambda(A)$ 也是 $\mathbb R^n$ 的 subspace。

## How to Verify an Eigenvalue and Find Its Eigenspace

給定候選值 $\lambda$：

1. 建立 $A-\lambda I_n$。
2. Row reduce $A-\lambda I_n$。
3. 若其 null space 非 zero space，則 $\lambda$ 是 eigenvalue。
4. 解 $(A-\lambda I_n)\mathbf x=\mathbf0$，並從 parametric vector form 取得 eigenspace 的 basis。

### Example

令

$$
B=
\left[
\begin{array}{rrr}
3&0&0\cr
0&1&2\cr
0&2&1
\end{array}
\right].
$$

解 $(B-3I_3)\mathbf x=\mathbf0$ 可得

$$
E_3(B)
=\mathrm{Span}
\left\{
\left[
\begin{array}{c}1\cr0\cr0\end{array}
\right],
\left[
\begin{array}{c}0\cr1\cr1\end{array}
\right]
\right\}.
$$

因此 $3$ 是 $B$ 的 eigenvalue，且 $\dim E_3(B)=2$。

## Geometric Interpretation

例如 reflection about a line $L$：

- 平行於 $L$ 的 nonzero vectors 對應 eigenvalue $1$；
- 垂直於 $L$ 的 nonzero vectors 對應 eigenvalue $-1$。

相對地， $90^\circ$ rotation 在 $\mathbb R^2$ 中沒有 real eigenvectors，因為沒有 nonzero real vector 在旋轉後仍與原向量平行。

## Common Pitfalls

- Zero vector 不是 eigenvector，但它屬於每個 eigenspace。
- 只有 square matrix 才討論 eigenvalues。
- 驗證 eigenvalue 時應檢查 $A-\lambda I_n$ 是否 singular，而不是只代入一個任意向量。
- 不同 eigenvalues 的 eigenspaces 可能維度不同。

## Assigned Exercises

Section 5.1：Problems 1, 3, 7, 9, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59。

---

- 上一篇：[4.5 Matrix Representations of Linear Operators](../section-04/04-05%20Matrix%20Representations%20of%20Linear%20Operators.md)
- 下一篇：[5.2 The Characteristic Polynomial](./05-02%20The%20Characteristic%20Polynomial.md)
- 上層：[線性代數－蘇柏青](../../README.md)
