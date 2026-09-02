---
aliases:
  - 6.4 Least-Squares Approximation and Orthogonal Projection Matrices
  - 最小平方法與正交投影矩陣
tags:
  - course/linear-algebra
  - linear-algebra/least-squares
  - linear-algebra/normal-equations
---

# 6.4 Least-Squares Approximation and Orthogonal Projection Matrices

> **講義範圍**
>
> `43_講義_Least Squares Approximations and Orthogonal Projection Matrices`，PDF 第 1-10 頁。

## Least-Squares Problem

給定 $C\in\mathcal M_{n\times k}$ 與 $\mathbf y\in\mathbb R^n$，least-squares problem 是尋找 $\widehat{\mathbf a}$，使

$$
\lVert\mathbf y-C\mathbf a\rVert
$$

最小。

幾何上， $C\mathbf a$ 位於 $W=\mathrm{Col}(C)$；最佳近似就是

$$
C\widehat{\mathbf a}
=\mathrm{proj}_W(\mathbf y).
$$

Residual

$$
\mathbf e=\mathbf y-C\widehat{\mathbf a}
$$

必須與 $W$ orthogonal。

## Normal Equations

由 $\mathbf e\in(\mathrm{Col}(C))^\perp$，得到

$$
C^T(\mathbf y-C\widehat{\mathbf a})=\mathbf0,
$$

亦即 normal equations

$$
C^TC\widehat{\mathbf a}=C^T\mathbf y.
$$

若 $C$ 具有 L.I. columns，則 $C^TC$ invertible，least-squares solution 唯一：

$$
\widehat{\mathbf a}
=(C^TC)^{-1}C^T\mathbf y.
$$

對應的 fitted vector 為

$$
\widehat{\mathbf y}
=C\widehat{\mathbf a}
=C(C^TC)^{-1}C^T\mathbf y.
$$

因此 projection matrix 是

$$
P_C=C(C^TC)^{-1}C^T.
$$

## Least-Squares Line

對 data pairs $(x_i,y_i)$，使用 model

$$
y=a_0+a_1x.
$$

令

$$
C=
\left[
\begin{array}{cc}
1&x_1\cr
\vdots&\vdots\cr
1&x_n
\end{array}
\right],
\qquad
\mathbf y=
\left[
\begin{array}{c}
y_1\cr
\vdots\cr
y_n
\end{array}
\right].
$$

則

$$
\widehat{\mathbf a}=
\left[
\begin{array}{c}
\widehat a_0\cr
\widehat a_1
\end{array}
\right]
=(C^TC)^{-1}C^T\mathbf y
$$

最小化 error sum of squares

$$
E=\sum_{i=1}^n
\bigl[y_i-(a_0+a_1x_i)\bigr]^2.
$$

## Polynomial Fitting

要 fit degree $m$ polynomial

$$
y=a_0+a_1x+\cdots+a_mx^m,
$$

使用 design matrix

$$
C=
\left[
\begin{array}{ccccc}
1&x_1&x_1^2&\cdots&x_1^m\cr
1&x_2&x_2^2&\cdots&x_2^m\cr
\vdots&\vdots&\vdots&&\vdots\cr
1&x_n&x_n^2&\cdots&x_n^m
\end{array}
\right]
$$

並解相同的 normal equations。

## Inconsistent Linear Systems

若 $A\mathbf x=\mathbf b$ inconsistent，則 least-squares solution $\widehat{\mathbf x}$ 使

$$
A\widehat{\mathbf x}
=\mathrm{proj}_{\mathrm{Col}(A)}(\mathbf b),
$$

並滿足

$$
A^TA\widehat{\mathbf x}=A^T\mathbf b.
$$

若 $A$ 的 columns 不是 L.I.，normal equations 仍描述所有 least-squares solutions，但 $A^TA$ 不可逆且 solution 可能不唯一。

## Least-Norm Solution

若 $A\mathbf x=\mathbf c$ consistent，任一 solution 可寫為

$$
\mathbf x=\mathbf x_0+\mathbf z,
\qquad
\mathbf z\in\mathrm{Null}(A).
$$

其中 norm 最小的 solution 是 $\mathbf x_0$ 在 $(\mathrm{Null}(A))^\perp$ 上的 component。

## Common Pitfalls

- Least-squares solution 最小化的是 residual norm，不一定使 residual 為 zero。
- Normal equations 是 $C^TC\widehat{\mathbf a}=C^T\mathbf y$，不可漏掉 transpose。
- $(C^TC)^{-1}$ 只在 $C$ full column rank 時存在。
- Fitted vector $C\widehat{\mathbf a}$ 唯一，但 coefficients 在 columns dependent 時可能不唯一。

## Assigned Exercises

Section 6.4：Problems 1, 2, 16, 17。

---

- 上一篇：[6.3 Orthogonal Projections](./06-03%20Orthogonal%20Projections.md)
- 下一篇：[6.5 Orthogonal Matrices and Operators](./06-05%20Orthogonal%20Matrices%20and%20Operators.md)
- 上層：[線性代數－蘇柏青](../../README.md)
