---
aliases:
  - 4.2 Basis and Dimension
  - 基底與維度
tags:
  - course/linear-algebra
  - linear-algebra/basis
  - linear-algebra/dimension
---

# 4.2 Basis and Dimension

> **講義範圍**
>
> `27_講義_Basis and DimensionⅠ(1)`，PDF 第 1-15 頁。

## Notation

- 本節所有 subspaces 均視為有限維空間，且包含於某個 $\mathbb R^n$。
- $\mathrm{Span}(S)$ 表示集合 $S$ 所生成的 subspace。
- L.I. 與 L.D. 分別表示 linearly independent 與 linearly dependent。
- $|S|$ 表示有限集合 $S$ 中的向量個數。

## Basis

令 $V$ 是 $\mathbb R^n$ 的 nonzero subspace。若集合

$$
\mathcal B=\{\mathbf b_1,\ldots,\mathbf b_k\}\subseteq V
$$

同時滿足：

1. $\mathcal B$ 是 linearly independent；
2. $\mathrm{Span}(\mathcal B)=V$，

則稱 $\mathcal B$ 為 $V$ 的 basis。

因此，basis 同時具有兩種極值意義：

- 它是生成 $V$ 所需的最小 generating set；
- 它是 $V$ 中無法再加入新向量而保持 L.I. 的 maximal L.I. set。

標準基底

$$
\mathcal E=\{\mathbf e_1,\ldots,\mathbf e_n\}
$$

是 $\mathbb R^n$ 的 basis。依慣例，zero subspace $\{\mathbf0\}$ 的 basis 是 empty set。

## Pivot Columns and a Basis for the Column Space

若 $A$ 經 row reduction 得到 echelon form，則 $A$ 的**原始 pivot columns** 構成 $\mathrm{Col}(A)$ 的 basis。

理由是 pivot columns：

- linearly independent；
- 能生成 $A$ 的所有 columns。

> Row reduction 通常會改變 column space，因此必須從原矩陣 $A$ 取 pivot columns，而不是從 echelon form 取對應 columns。

## Theorem 4.3: Reduction Theorem

令 $S$ 是 nonzero subspace $V\subseteq\mathbb R^n$ 的有限 generating set，則可從 $S$ 中刪除冗餘向量，得到 $V$ 的 basis。

**Proof.** 設

$$
S=\{\mathbf u_1,\ldots,\mathbf u_k\},
\qquad
A=[\mathbf u_1\ \mathbf u_2\ \cdots\ \mathbf u_k].
$$

因為 $\mathrm{Col}(A)=\mathrm{Span}(S)=V$，取 $A$ 的原始 pivot columns，便得到包含於 $S$ 且能生成 $V$ 的 L.I. subset。

### Consequences for $\mathbb R^n$

- $\mathbb R^n$ 的任一有限 generating set 都含有一個 basis。
- 任一生成 $\mathbb R^n$ 的集合至少含有 $n$ 個向量。
- $\mathbb R^n$ 中超過 $n$ 個向量的集合必為 L.D.。
- 因此， $\mathbb R^n$ 的每一組 basis 都恰有 $n$ 個向量。

## Theorem 4.4: Extension Theorem

令 $S$ 是 nonzero subspace $V\subseteq\mathbb R^n$ 中的 L.I. subset，則可加入有限個 $V$ 中的向量，把 $S$ 擴充成 $V$ 的 basis。

**Proof idea.** 若 $\mathrm{Span}(S)\neq V$，取

$$
\mathbf v_1\in V\setminus\mathrm{Span}(S).
$$

則 $S\cup\{\mathbf v_1\}$ 仍為 L.I.。重複此步驟；由於 $\mathbb R^n$ 中的 L.I. set 最多只有 $n$ 個向量，過程必在有限步後停止並生成 $V$。

Reduction Theorem 與 Extension Theorem 可整理為：

- generating set 可以**縮減**為 basis；
- L.I. set 可以**擴充**為 basis。

## Theorem 4.5: Invariance of the Number of Basis Vectors

nonzero subspace $V\subseteq\mathbb R^n$ 的任意兩組 bases 都含有相同數目的向量。

**Proof idea.** 若

$$
\mathcal B=\{\mathbf u_1,\ldots,\mathbf u_k\},
\qquad
\mathcal C=\{\mathbf v_1,\ldots,\mathbf v_p\}
$$

都是 $V$ 的 bases。因 $\mathcal B$ 生成 $V$，每個 $\mathbf v_i$ 都可由 $\mathcal B$ 線性表示；又因 $\mathcal C$ 為 L.I.，相應的 $p$ 個 coefficient vectors 在 $\mathbb R^k$ 中亦為 L.I.，故 $p\leq k$。交換兩組 bases 的角色可得 $k\leq p$，因此 $k=p$。

## Dimension

$V$ 的任一組 basis 所含的向量個數稱為 $V$ 的 dimension，記為

$$
\dim V=k.
$$

對 zero subspace 定義

$$
\dim\{\mathbf0\}=0.
$$

例如，若 homogeneous equation 的 general solution 可寫為

$$
\mathbf x
=s\mathbf u_1+t\mathbf u_2+r\mathbf u_3
$$

且 $\{\mathbf u_1,\mathbf u_2,\mathbf u_3\}$ 為 L.I.，則它們形成 solution space 的 basis，該空間的 dimension 為 $3$。

## Theorem 4.6

若 $\dim V=k$，則：

- $V$ 中任一 L.I. subset 最多含有 $k$ 個向量；
- 等價地， $V$ 中超過 $k$ 個向量的集合必為 L.D.。

這是 Extension Theorem 的直接結果：L.I. subset 可擴充為含有 $k$ 個向量的 basis，因此原集合不可能超過 $k$ 個向量。

## Theorem 4.7: Basis Criterion Using Dimension

若 $\dim V=k$，且 $S\subseteq V$ 恰含有 $k$ 個向量，則下列條件等價：

1. $S$ 是 $V$ 的 basis；
2. $S$ 是 L.I.；
3. $S$ generates $V$。

因此，在已知 dimension 與向量個數相同時，只需驗證 linear independence 或 spanning 其中一項。

## Practical Basis Tests

要判斷 $S=\{\mathbf v_1,\ldots,\mathbf v_k\}$ 是否為 $V$ 的 basis，可依序確認：

1. **Membership**：每個 $\mathbf v_i\in V$。
2. **Independence**：解

$$
c_1\mathbf v_1+\cdots+c_k\mathbf v_k=\mathbf0
$$

只有 trivial solution。
3. **Spanning**：證明 $\mathrm{Span}(S)=V$。

若已知 $\dim V=k$，完成 membership 後，只需再檢查 independence 或 spanning 其中之一。

## Common Pitfalls

- generating set 不一定是 basis，其中可能含有 redundant vectors。
- L.I. set 不一定生成整個 $V$，除非其向量個數已等於 $\dim V$。
- basis 是集合，因此不含重複向量；coordinate system 則還需要指定順序。
- 求 $\mathrm{Col}(A)$ 的 basis 時，要選原矩陣的 pivot columns。

## Assigned Exercises

Section 4.2：Problems 7, 13, 22, 36, 39-44。

---

- 上一篇：[4.1 Subspaces](./04-01%20Subspaces.md)
- 下一篇：[4.3 The Dimension of Subspaces Associated with a Matrix](./04-03%20The%20Dimension%20of%20Subspaces%20Associated%20with%20a%20Matrix.md)
- 上層：[線性代數－蘇柏青](../../README.md)
