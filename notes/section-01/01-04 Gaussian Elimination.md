---
aliases:
  - 1.4 Gaussian Elimination
  - 高斯消去法
tags:
  - course/linear-algebra
  - linear-algebra/gaussian-elimination
  - linear-algebra/row-reduction
---

# 1.4 Gaussian Elimination

> **講義範圍**
>
> `7_講義_Gaussian Elimination(1)`，PDF 第 1-20 頁。

## Notation

- 沿用 [1.3 Systems of Linear Equations](./01-03%20Systems%20of%20Linear%20Equations.md)： $A\in\mathcal M_{m\times n}$、 $\mathbf x\in\mathbb R^n$、 $\mathbf b\in\mathbb R^m$。
- 線性方程組寫為 $A\mathbf x=\mathbf b$，其增廣矩陣寫為 $[A\mid\mathbf b]$。
- 本文採「列 = row、行 = column」；第 $i$ 列記為 $R_i$。
- Gaussian elimination 的目標是將矩陣化為 row echelon form（REF），再化為 reduced row echelon form（RREF）。

## Gaussian Elimination

Gaussian elimination（高斯消去法）是一套使用初等列運算，將矩陣化為 RREF 的演算法。對增廣矩陣執行此演算法，即可系統化求解 $A\mathbf x=\mathbf b$。

演算法分為兩個階段：

- **Forward pass（前向消去）**：Steps 1-4，將矩陣化為 REF。
- **Backward pass（反向消去）**：Steps 5-6，將 REF 化為 RREF。

### Pivot Terminology

在尚未被忽略的子矩陣中，最左側且含非零元素的行（column）稱為 pivot column；該行中選定的首項位置稱為 pivot position。完成消去後，每個 pivot position 包含該列的 leading entry（首項）。

## Six Steps of the Algorithm

### Forward Pass: Steps 1-4

1. **選擇 pivot column**：在尚未忽略的子矩陣中，找出最左側且含非零元素的行；此行為 pivot column，其最上方的可用位置為 pivot position。
2. **移入非零 pivot**：在 pivot column 的未忽略列中選取任一非零元素，必要時交換列，使其位於 pivot position。
3. **消去下方元素**：將 pivot 所在列的適當倍數加到各下方列，使 pivot 下方同一行的元素全為 $0$。
4. **縮小子矩陣**：忽略包含 pivot position 的列，對右下方剩餘子矩陣重複 Steps 1-4；若沒有非零列，前向消去結束。

完成 Steps 1-4 後，矩陣為 REF。

### Backward Pass: Steps 5-6

5. **標準化並向上消去**：若目前列的首項不是 $1$，先以 scaling 將其化為 $1$；再將此列的適當倍數加到所有上方列，使 pivot 上方同一行的元素全為 $0$。
6. **移至上一個 pivot**：若 Step 5 處理的不是第一列，便對上一個 pivot 重複 Step 5；處理完最上方的 pivot 後停止。

完成 Steps 5-6 後，矩陣即為 RREF。

## Worked Example

考慮增廣矩陣

$$
[A\mid\mathbf b]=
\left[
\begin{array}{ccc|c}
1&-2&-1&3\cr
3&-6&-5&3\cr
2&-1&1&0
\end{array}
\right].
$$

前向消去並整理列順序，可得 REF：

$$
\left[
\begin{array}{ccc|c}
1&-2&-1&3\cr
0&3&3&-6\cr
0&0&-2&-6
\end{array}
\right]
\sim
\left[
\begin{array}{ccc|c}
1&-2&-1&3\cr
0&3&3&-6\cr
0&0&1&3
\end{array}
\right].
$$

再進行 backward pass，得到唯一的 RREF：

$$
\operatorname{rref}[A\mid\mathbf b]=
\left[
\begin{array}{ccc|c}
1&0&0&-4\cr
0&1&0&-5\cr
0&0&1&3
\end{array}
\right].
$$

因此方程組的唯一解為

$$
\mathbf x=
\begin{bmatrix}
-4\cr -5\cr 3
\end{bmatrix}.
$$

## Rank and Nullity

令 $A\in\mathcal M_{m\times n}$，並令 $R$ 為 $A$ 的 RREF。

- **Rank**： $A$ 的 rank（秩）定義為 $R$ 的非零列數，記為 $\operatorname{rank}(A)$。
- **Nullity**： $A$ 的 nullity（零度）定義為

$$
\operatorname{nullity}(A)=n-\operatorname{rank}(A).
$$

其中 $n$ 是 $A$ 的行數（column 數）。由 RREF 的結構， $\operatorname{rank}(A)$ 等於 pivot 的數目，也等於 basic variables 的數目； $\operatorname{nullity}(A)$ 等於 free variables 的數目。

若 $A\mathbf x=\mathbf b$ 為 consistent system，則

$$
\begin{aligned}
\text{basic variables 的數目}&=\operatorname{rank}(A),\cr
\text{free variables 的數目}&=\operatorname{nullity}(A).
\end{aligned}
$$

若 $[A\mid\mathbf b]$ 的 RREF 為 $[R\mid\mathbf c]$，則 $R$ 也是 $A$ 的 RREF，因此

$$
\operatorname{rank}(A)=\operatorname{rank}(R),
\qquad
\operatorname{nullity}(A)=\operatorname{nullity}(R).
$$

但 $\operatorname{rank}([A\mid\mathbf b])$ 不一定等於 $\operatorname{rank}(A)$；兩者的關係正是 consistency test 的內容。

## Test of Consistency

令 $A\in\mathcal M_{m\times n}$、 $\mathbf b\in\mathbb R^m$。以下四個條件彼此等價：

1. $A\mathbf x=\mathbf b$ 是 consistent。
2. $\mathbf b$ 可寫成 $A$ 的 columns 的線性組合。若 $A=[\mathbf a_1\ \cdots\ \mathbf a_n]$，則存在 $v_1,ldots,v_n\in\mathbb R$ 使

$$
\mathbf b=v_1\mathbf a_1+\cdots+v_n\mathbf a_n.
$$

3. $[A\mid\mathbf b]$ 的 RREF 沒有任何形式為

$$
\begin{bmatrix}0&0&\cdots&0\mid d\end{bmatrix},
\qquad d\ne0,
$$

的列。
4. 係數矩陣與增廣矩陣的 rank 相同：

$$
\operatorname{rank}(A)=\operatorname{rank}([A\mid\mathbf b]).
$$

條件 3 的矛盾列代表 $0=d$，因此直接表示無解。條件 2 則說明 $\mathbf b$ 是否位於 $A$ 的 column space；若位於其中，便存在某個 $\mathbf x$ 使 $A\mathbf x=\mathbf b$。

## Solving a System in RREF

對 $[A\mid\mathbf b]$ 執行 Gaussian elimination 後：

- 若出現矛盾列，系統 inconsistent，無解。
- 若沒有矛盾列，系統 consistent；將 pivot columns 對應的 basic variables 寫成 free variables 的函數，即得 general solution。
- 沒有 free variables 時，解唯一；有至少一個 free variable 時，解有無限多個。

例如，若 RREF 為 $[I_n\mid\mathbf c]$，則

$$
\mathbf x=\mathbf c
$$

且解唯一。

## Section Summary

- Gaussian elimination 的 Steps 1-4 是 forward pass，將矩陣化為 REF；Steps 5-6 是 backward pass，將 REF 化為 RREF。
- 每一步只使用可逆的初等列運算，因此不改變增廣矩陣所代表的解集合。
- RREF 的 pivot 數目等於 rank；行數減去 rank 等於 nullity，也就是 free variables 的數目。
- $A\mathbf x=\mathbf b$ consistent 當且僅當 $\mathbf b$ 是 $A$ 的 columns 的線性組合，等價於 $\operatorname{rank}(A)=\operatorname{rank}([A\mid\mathbf b])$。
- RREF 中的矛盾列 $[0\ \cdots\ 0\mid d]$（ $d\ne0$）是無解的判準。

## Practice

講義指定 Section 1.4 習題：3、7、11、15、21、25、29、37、41、53、55、57、59、63、67、71。

## Navigation

- 上一節：[1.3 Systems of Linear Equations](./01-03%20Systems%20of%20Linear%20Equations.md)
- 上層：[線性代數－蘇柏青](../../README.md)
- 下一節：[1.6 The Span of a Set of Vectors](./01-06%20The%20Span%20of%20a%20Set%20of%20Vectors.md)
