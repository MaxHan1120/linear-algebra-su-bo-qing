---
aliases:
  - 2.3 Invertibility and Elementary Matrices
  - 可逆性與初等矩陣
tags:
  - course/linear-algebra
  - linear-algebra/invertibility
  - linear-algebra/elementary-matrix
---

# 2.3 Invertibility and Elementary Matrices

> **講義範圍**
>
> `16_講義_Invertibility and Elementary Matrices`，PDF 第 1-23 頁。

## Invertible Matrices

方陣 $A\in\mathcal M_{n\times n}$ 稱為 invertible，若存在 $B\in\mathcal M_{n\times n}$ 使

$$
AB=BA=I_n.
$$

此 $B$ 唯一，稱為 $A$ 的 inverse，記為 $A^{-1}$。若不存在 inverse，則稱 $A$ singular。

若 $B$、 $C$ 都是 $A$ 的 inverse，則

$$
B=BI_n=B(AC)=(BA)C=I_nC=C,
$$

故 inverse 確實唯一。

## Theorem 2.2: Properties of Inverses

令 $A,B\in\mathcal M_{n\times n}$ 均可逆，則：

1. $A^{-1}$ 可逆，且 $(A^{-1})^{-1}=A$。
2. $AB$ 可逆，且 $(AB)^{-1}=B^{-1}A^{-1}$。
3. $A^T$ 可逆，且 $(A^T)^{-1}=(A^{-1})^T$。

有限個可逆矩陣的乘積仍可逆，inverse 的順序與原乘積相反。

## Solving an Invertible System

若 $A$ 可逆，則

$$
A\mathbf x=\mathbf b
\iff
\mathbf x=A^{-1}\mathbf b.
$$

所以此方程組對每個 $\mathbf b\in\mathbb R^n$ 都有唯一解。不過，若只求解單一系統，直接做 Gaussian elimination 通常比先計算 $A^{-1}$ 更有效率。

## Elementary Matrices

elementary matrix 是對 $I_m$ 做一次 elementary row operation 所得到的 $m\times m$ 矩陣。若 $E$ 對應某個 row operation，則左乘 $EA$ 等同於對 $A$ 執行相同的 row operation。

三種類型為：

1. 交換兩列。
2. 將一列乘以非零 scalar。
3. 將一列的 scalar multiple 加到另一列。

每個 elementary matrix 都可逆，其 inverse 對應反向 row operation。

## Row Reduction as Matrix Multiplication

若 row operations 將 $A$ 化為 $R$，相應 elementary matrices 依序為 $E_1,\ldots,E_k$，則

$$
R=E_k\cdots E_2E_1A.
$$

令 $P=E_k\cdots E_1$，則 $P$ 可逆且 $PA=R$。

### Theorem 2.3

若 $A\in\mathcal M_{m\times n}$ 的 RREF 為 $R$，則存在可逆 $P\in\mathcal M_{m\times m}$ 使

$$
PA=R.
$$

若相同 row operations 將 $[A\mid\mathbf b]$ 化為 $[R\mid\mathbf c]$，則

$$
P[A\mid\mathbf b]=[PA\mid P\mathbf b]=[R\mid\mathbf c].
$$

所以 $A\mathbf x=\mathbf b$ 與 $R\mathbf x=\mathbf c$ 有完全相同的解集合。

## Column Relations and RREF

設 $A=[\mathbf a_1\ \cdots\ \mathbf a_n]$、 $R=[\mathbf r_1\ \cdots\ \mathbf r_n]=PA$。因 $P$ 可逆，

$$
c_1\mathbf a_1+\cdots+c_n\mathbf a_n=\mathbf0
\iff
c_1\mathbf r_1+\cdots+c_n\mathbf r_n=\mathbf0.
$$

因此 $A$ 與 $R$ 具有相同的 column dependence relations，但兩者的 columns 本身通常不同。

### Theorem 2.4: Pivot Columns

1. $A$ 中對應 pivot positions 的 columns 線性獨立。
2. 每個 nonpivot column 都是其前方 pivot columns 的線性組合。
3. 這些 coefficients 可直接由 $R$ 的相應 column 讀出。

要建立 $A$ 的 generating set，應選取 **原矩陣 $A$ 的 pivot columns**，不是 $R$ 的 pivot columns。

## Assigned Exercises

Section 2.3：Problems 1, 3, 5, 9, 11, 15, 17, 19, 21, 23, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 49, 51。

---

- 上一篇：[2.1 Matrix Multiplication](./02-01%20Matrix%20Multiplication.md)
- 下一篇：[2.4 The Inverse of a Matrix](./02-04%20The%20Inverse%20of%20a%20Matrix.md)
- 上層：[線性代數－蘇柏青](../../README.md)
