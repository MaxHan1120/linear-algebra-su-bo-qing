---
aliases:
  - 7.3 Basis and Dimension
  - 抽象向量空間的基底與維度
tags:
  - course/linear-algebra
  - linear-algebra/abstract-basis
  - linear-algebra/dimension
---

# 7.3 Basis and Dimension

> **講義範圍**
>
> `56_講義_Basis and DimensionⅡ(1)`，PDF 第 1-13 頁。

## Linear Independence in General Vector Spaces

Finite subset $S=\{\mathbf v_1,\ldots,\mathbf v_k\}$ 是 L.I.，若

$$
c_1\mathbf v_1+\cdots+c_k\mathbf v_k=\mathbf0
$$

只具有 trivial solution。否則 $S$ 是 L.D.。

Infinite subset $S$ 稱為 L.I.，若其每一個 finite subset 都是 L.I.；只要含有一個 L.D. finite subset， $S$ 就是 L.D.。

例如

$$
\{1,x,x^2,\ldots\}
$$

是 polynomial space $\mathcal P$ 的 infinite L.I. subset。

## Theorem 7.8: Isomorphisms Preserve Independence

若 $T:V\to W$ 是 isomorphism，且 $\{\mathbf v_1,\ldots,\mathbf v_k\}$ 在 $V$ 中 L.I.，則

$$
\{T(\mathbf v_1),\ldots,T(\mathbf v_k)\}
$$

在 $W$ 中亦為 L.I.。

這是因為 $T$ one-to-one：

$$
\sum_{i=1}^k c_iT(\mathbf v_i)=\mathbf0
\implies
T\left(\sum_{i=1}^k c_i\mathbf v_i\right)=\mathbf0
\implies
\sum_{i=1}^k c_i\mathbf v_i=\mathbf0.
$$

Isomorphism 同樣 preserves spanning sets 與 bases。

## Basis

Subset $\mathcal B\subseteq V$ 稱為 basis，若：

1. $\mathcal B$ 是 L.I.；
2. $\mathrm{Span}(\mathcal B)=V$。

例如

$$
\{1,x,x^2,\ldots\}
$$

是 $\mathcal P$ 的 infinite basis，而

$$
\{1,x,\ldots,x^n\}
$$

是 $\mathcal P_n$ 的 finite basis。

## Theorem 7.9

若 vector space $V$ 有一組 finite basis，則 $V$ 的每一組 basis 都是 finite，且含有相同數目的 vectors。

**Proof idea.** 對一組含 $n$ 個 vectors 的 basis $\mathcal B$，coordinate map

$$
\Phi_{\mathcal B}:V\to\mathbb F^n
$$

是 isomorphism。若另一組 basis 含超過 $n$ 個 vectors，其 images 會在 $\mathbb F^n$ 中形成超過 $n$ 個 vectors 的 L.I. set，矛盾。交換兩組 bases 的角色即可得到相同 cardinality。

## Dimension

若 $V$ 有 finite basis，其 basis vectors 的數量稱為 dimension，記為 $\dim V$。若沒有 finite basis，則稱 $V$ infinite-dimensional。

Isomorphic vector spaces 具有相同 dimension。

## Finite-Dimensional Consequences

若 $\dim V=n$，則：

1. 任一 L.I. subset 至多含 $n$ 個 vectors。
2. 含恰好 $n$ 個 vectors 的 L.I. subset 是 basis。
3. 任一 generating set 至少含 $n$ 個 vectors。
4. 含恰好 $n$ 個 vectors 的 generating set 是 basis。

## Standard Examples

$$
\dim\mathcal P_n=n+1,
$$

basis 可取 $\{1,x,\ldots,x^n\}$。

$$
\dim\mathcal M_{m\times n}=mn,
$$

basis 可取 matrix units $E_{ij}$。

$$
\dim\mathcal L(\mathbb R^n,\mathbb R^m)=mn,
$$

因為 map

$$
A\longmapsto T_A,
\qquad
T_A(\mathbf x)=A\mathbf x
$$

是 $\mathcal M_{m\times n}$ 與 $\mathcal L(\mathbb R^n,\mathbb R^m)$ 之間的 isomorphism。

## Common Pitfalls

- Infinite set 的 independence 以所有 finite subsets 判定，不使用無限和。
- $\mathcal P_n$ 的 dimension 是 $n+1$，因為包含 constant term。
- Isomorphic spaces 的 vectors 形式可以完全不同，但其 linear structure 與 dimension 相同。
- Basis 必須同時 L.I. 且 spanning。

## Assigned Exercises

Section 7.3：Problems 1, 9, 19, 21, 26, 29, 39, 45, 50, 51, 54, 55, 60, 62, 63。

---

- 上一篇：[7.2 Linear Transformations](./07-02%20Linear%20Transformations.md)
- 下一篇：[7.4 Matrix Representation of Linear Operators](./07-04%20Matrix%20Representation%20of%20Linear%20Operators.md)
- 上層：[線性代數－蘇柏青](../../README.md)
