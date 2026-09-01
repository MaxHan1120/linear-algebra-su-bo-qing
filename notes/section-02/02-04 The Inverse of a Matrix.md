---
aliases:
  - 2.4 The Inverse of a Matrix
  - 反矩陣
tags:
  - course/linear-algebra
  - linear-algebra/inverse-matrix
  - linear-algebra/invertible-matrix-theorem
---

# 2.4 The Inverse of a Matrix

> **講義範圍**
>
> `18_講義_The Inverse of a Matrix(1)`，PDF 第 1-14 頁。

## Theorem 2.5: RREF Criterion

令 $A\in\mathcal M_{n\times n}$。則

$$
A\text{ is invertible}
\iff
\mathrm{rref}(A)=I_n.
$$

row reduction 可寫成左乘可逆 elementary matrices。若 $PA=I_n$，則 $P=A^{-1}$；反之，若 $A$ 可逆， $A\mathbf x=\mathbf0$ 只有 trivial solution，故每個 column 都有 pivot。

## Computing the Inverse

對增廣矩陣做 row reduction：

$$
[A\mid I_n]\longrightarrow[R\mid B].
$$

- 若 $R=I_n$，則 $B=A^{-1}$。
- 若 $R\ne I_n$，則 $A$ 不可逆。

因為相同 row operations 等同於左乘某個可逆矩陣 $P$：

$$
P[A\mid I_n]=[PA\mid P]=[I_n\mid A^{-1}].
$$

### Example

令

$$
A=
\left[
\begin{array}{ccc}
1&2&3\cr
2&5&6\cr
3&4&8
\end{array}
\right].
$$

將 $[A\mid I_3]$ 化為 RREF 可得

$$
A^{-1}=
\left[
\begin{array}{rrr}
-16&4&3\cr
-2&1&0\cr
7&-2&-1
\end{array}
\right].
$$

最後應以 $AA^{-1}=I_3$ 或 $A^{-1}A=I_3$ 檢查。

## Computing $A^{-1}B$ Directly

若只需要 $A^{-1}B$，不必先求完整的 $A^{-1}$。直接計算

$$
[A\mid B]\longrightarrow[I_n\mid A^{-1}B].
$$

這等同於同時解多個右端向量的線性系統。

## Theorem 2.6: Invertible Matrix Theorem

令 $A\in\mathcal M_{n\times n}$。下列敘述彼此等價：

1. $A$ 可逆。
2. $\mathrm{rref}(A)=I_n$。
3. $\mathrm{rank}(A)=n$。
4. $A$ 的 columns 生成 $\mathbb R^n$。
5. 對每個 $\mathbf b\in\mathbb R^n$， $A\mathbf x=\mathbf b$ 都 consistent。
6. $\mathrm{nullity}(A)=0$。
7. $A$ 的 columns 線性獨立。
8. $A\mathbf x=\mathbf0$ 只有 trivial solution。
9. 存在 $B\in\mathcal M_{n\times n}$ 使 $BA=I_n$。
10. 存在 $C\in\mathcal M_{n\times n}$ 使 $AC=I_n$。
11. $A$ 可寫成 elementary matrices 的乘積。

這些條件的共同核心是：方陣 $A$ 的每一 row 與每一 column 都具有 pivot。

## One-Sided Inverses

對方陣而言，left inverse 或 right inverse 單獨存在便足以推出可逆：

$$
BA=I_n
\quad\text{或}\quad
AC=I_n
\implies
A\text{ is invertible}.
$$

此結論依賴 $A$ 是方陣；對 rectangular matrices 不可直接套用。

## Assigned Exercises

Section 2.4：Problems 1, 8, 14, 19, 21, 22, 27, 28, 29, 31, 32。

---

- 上一篇：[2.3 Invertibility and Elementary Matrices](./02-03%20Invertibility%20and%20Elementary%20Matrices.md)
- 下一篇：[2.7 Linear Transformations and Matrices](./02-07%20Linear%20Transformations%20and%20Matrices.md)
- 上層：[線性代數－蘇柏青](../../README.md)
