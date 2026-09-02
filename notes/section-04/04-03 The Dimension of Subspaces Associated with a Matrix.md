---
aliases:
  - 4.3 The Dimension of Subspaces Associated with a Matrix
  - 矩陣相關子空間的維度
tags:
  - course/linear-algebra
  - linear-algebra/rank
  - linear-algebra/nullity
  - linear-algebra/row-space
---

# 4.3 The Dimension of Subspaces Associated with a Matrix

> **講義範圍**
>
> `29_講義_The Dimension of Subspaces associated with a Matrix`，PDF 第 1-10 頁。

## Three Subspaces Associated with a Matrix

對

$$
A\in\mathcal M_{m\times n},
$$

本節考慮三個 subspaces：

$$
\mathrm{Col}(A)\subseteq\mathbb R^m,
\qquad
\mathrm{Null}(A)\subseteq\mathbb R^n,
\qquad
\mathrm{Row}(A)\subseteq\mathbb R^n.
$$

它們的 dimensions 可由 row reduction 與 pivot positions 決定。

## Dimension of the Column Space

$$
\dim\mathrm{Col}(A)=\mathrm{rank}(A).
$$

因為原矩陣 $A$ 的 pivot columns 構成 $\mathrm{Col}(A)$ 的 basis，而 pivot columns 的數量就是 $\mathrm{rank}(A)$。

### Procedure

1. 將 $A$ row reduce 至 echelon form。
2. 找出 pivot positions。
3. 回到原矩陣 $A$ 取對應 columns。
4. 這些 columns 構成 $\mathrm{Col}(A)$ 的 basis，其數量為 $\mathrm{rank}(A)$。

## Dimension of the Null Space

$$
\dim\mathrm{Null}(A)=\mathrm{nullity}(A).
$$

$\mathrm{nullity}(A)$ 是 homogeneous system

$$
A\mathbf x=\mathbf0
$$

中 free variables 的數量。把 general solution 寫成 free variables 的 linear combination，所得 coefficient vectors 構成 $\mathrm{Null}(A)$ 的 basis。

若 $A$ 有 $n$ 個 columns，則每一個 variable 恰為 pivot variable 或 free variable，因此

$$
\mathrm{rank}(A)+\mathrm{nullity}(A)=n.
$$

這就是矩陣形式的 rank-nullity relation。

## Row Space Is Preserved by Row Operations

若 $E$ 是 elementary matrix，則

$$
\mathrm{Row}(EA)=\mathrm{Row}(A).
$$

**Proof.** $EA$ 的每一個 row 都是 $A$ 的 rows 的 linear combination，因此

$$
\mathrm{Row}(EA)\subseteq\mathrm{Row}(A).
$$

又因 $A=E^{-1}(EA)$，反向包含關係也成立，故兩個 row spaces 相等。

相對地，一般而言

$$
\mathrm{Col}(EA)\neq\mathrm{Col}(A).
$$

因此 row reduction 保留 row space，但通常不保留 column space。

## Theorem 4.8: Basis for the Row Space

令 $R$ 是 $A$ 的 reduced row echelon form，則 $R$ 的所有 nonzero rows 構成 $\mathrm{Row}(A)$ 的 basis。

**Proof.** Row operations 保留 row space，所以

$$
\mathrm{Row}(R)=\mathrm{Row}(A).
$$

$R$ 的 nonzero rows 顯然生成 $\mathrm{Row}(R)$；此外，每個 nonzero row 都有位於不同 column 的 leading $1$，故這些 rows 為 L.I.。

因此

$$
\dim\mathrm{Row}(A)=\mathrm{rank}(A).
$$

## Equality of Row Rank and Column Rank

綜合前述結果：

$$
\dim\mathrm{Row}(A)
=\mathrm{rank}(A)
=\dim\mathrm{Col}(A).
$$

也就是 row rank 與 column rank 相等。

由於

$$
\mathrm{Row}(A)=\mathrm{Col}(A^T),
$$

可得

$$
\mathrm{rank}(A)=\mathrm{rank}(A^T).
$$

## Theorem 4.9: Dimension and Inclusion

若 $V$ 與 $W$ 都是 $\mathbb R^n$ 的 subspaces，且

$$
V\subseteq W,
$$

則

$$
\dim V\leq\dim W.
$$

此外，若 $V$ 與 $W$ 具有相同的 dimension，則

$$
V=W.
$$

**Proof idea.** $V$ 的 basis 是 $W$ 中的 L.I. set，可由 Extension Theorem 擴充成 $W$ 的 basis，因此 $\dim V\leq\dim W$。若 dimensions 相同，就無須加入任何向量，原 basis 已生成 $W$。

## Connection with Linear Transformations

若 $T:\mathbb R^n\to\mathbb R^m$ 的 standard matrix 為 $A$，則

$$
\mathrm{range}(T)=\mathrm{Col}(A),
\qquad
\mathcal N(T)=\mathrm{Null}(A).
$$

因此

$$
\dim\mathrm{range}(T)=\mathrm{rank}(A),
\qquad
\dim\mathcal N(T)=\mathrm{nullity}(A),
$$

並有

$$
\dim\mathrm{range}(T)+\dim\mathcal N(T)=n.
$$

## Summary Table

| Subspace | Ambient space | Basis 的取得方式 | Dimension |
|---|---:|---|---:|
| $\mathrm{Col}(A)$ | $\mathbb R^m$ | 原矩陣的 pivot columns | $\mathrm{rank}(A)$ |
| $\mathrm{Row}(A)$ | $\mathbb R^n$ | RREF 的 nonzero rows | $\mathrm{rank}(A)$ |
| $\mathrm{Null}(A)$ | $\mathbb R^n$ | general solution 的 parameter vectors | $\mathrm{nullity}(A)$ |

## Common Pitfalls

- RREF 的 pivot columns 不一定生成原矩陣的 column space；應回到原矩陣取 columns。
- RREF 的 nonzero rows 可以直接作為原矩陣 row space 的 basis。
- $\mathrm{rank}(A)$ 是 pivot 數； $\mathrm{nullity}(A)$ 是 free variable 數。
- Rank-nullity 中的 $n$ 是 $A$ 的 column 數，不是 row 數。

## Assigned Exercises

Section 4.3：Problems 1, 4, 6, 9, 15, 61, 64, 73, 81。

---

- 上一篇：[4.2 Basis and Dimension](./04-02%20Basis%20and%20Dimension.md)
- 下一篇：[4.4 Coordinate Systems](./04-04%20Coordinate%20Systems.md)
- 上層：[線性代數－蘇柏青](../../README.md)
