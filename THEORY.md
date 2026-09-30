# Theory

## Sensitivity graph

For a Boolean function
[
f:\{0,1\}^n\to\{0,1\},
]
the sensitivity graph (G_f) has vertex set ({0,1}^n). Two vertices (x) and (x\oplus e_i) are adjacent exactly when
[
f(x)\ne f(x\oplus e_i).
]

Vertices of degree zero are inactive. The graph induced by the non-isolated vertices is the active sensitivity graph. Pointwise sensitivity is exactly graph degree:
[
s(f,x)=\deg_{G_f}(x),
]
and
[
s(f)=\max_x s(f,x).
]

The strengthened summary used by the verified result is
[
S^\dagger(f)=
\bigl(
\operatorname{ess}(f),
|E(G_f)|,
s(f),
H_{\deg}(f),
\mathbf w^\downarrow(f),
\operatorname{Spec}(G_f^{\mathrm{act}}),
\deg_{\mathbb F_2}(f),
\deg_{\mathbb R}(f),
bs(f),
D(f),
C(f),
\{C_0(f),C_1(f)\}
\bigr).
]

The residual geometry examined is
[
G^\star(f)=
\bigl(
\operatorname{Comp}(f),
\nu(f),
\operatorname{Diam}(f)
\bigr),
]
where (operatorname{Comp}) is the sorted active-component-size profile, (
u) is maximum matching size, and (operatorname{Diam}) is the sorted active-component-diameter profile.

## Explicit five-variable separation

Define
[
A=\{00000,01000,10000,11100,11111\},
]
[
B=\{00000,00011,00101,01000,10000\},
]
and let (f_A,f_B) be their indicator functions.

The pair agrees in the following quantities:

| Quantity | (f_A) | (f_B) |
|---|---:|---:|
| Essential variables | 5 | 5 |
| Sensitive edges | 21 | 21 |
| Maximum sensitivity | 5 | 5 |
| Degree histogram | (((0,12),(1,10),(2,4),(3,2),(4,2),(5,2))) | same |
| Sorted directional counts | ((3,3,5,5,5)) | same |
| GF(2) degree | 5 | 5 |
| Real multilinear degree | 5 | 5 |
| Block sensitivity | 5 | 5 |
| Deterministic decision-tree depth | 5 | 5 |
| Worst-case certificate complexity | 5 | 5 |
| Unordered one-sided certificate profile | ({3,5}) | ({3,5}) |
| Maximum matching size | 5 | 5 |

Their active adjacency matrices have the common integer characteristic polynomial
[
\chi(\lambda)
=
\lambda^{10}(\lambda^2-5)(\lambda^2-3)^2
(\lambda^4-10\lambda^2+13),
]
equivalently
[
\lambda^{20}-21\lambda^{18}+162\lambda^{16}
-578\lambda^{14}+957\lambda^{12}-585\lambda^{10}.
]

Thus the active sensitivity graphs are exactly adjacency-cospectral. Their active component geometry differs:
[
\operatorname{Comp}(f_A)=(16,4),
\qquad
\operatorname{Comp}(f_B)=(11,9),
]
and
[
\operatorname{Diam}(f_A)=(6,2),
\qquad
\operatorname{Diam}(f_B)=(4,4).
]

Therefore (S^\dagger) does not determine either active component-size distribution or active diameter profile.

## Exhaustive sparse-layer verification

For (n=5), the complete sparse layers (k=|f^{-1}(1)|=4) and (k=5) are enumerated.

| Layer | Raw sets | Canonical representatives | Cheap buckets | Collision classes | Strong separation classes |
|---|---:|---:|---:|---:|---:|
| (k=4) | 35,960 | 625 | 31 | 26 | 0 |
| (k=5) | 201,376 | 2,674 | 63 | 63 | 1 |

Canonicalization uses input-variable permutations and output complement. The (k=4) result is only a finite negative control for that enumerated layer. The central witness is verified independently using exact integer characteristic-polynomial equality.

## Directional sensitivity in a sparse truth set

Let (S=f^{-1}(1)), with (|S|=k), and let (E_i(S)) be the number of internal edges of (Q_n[S]) in coordinate direction (i). If (w_i(f)) denotes the number of sensitive edges in direction (i), then
[
w_i(f)=k-2|E_i(S)|.
]

Hence, for fixed (k),
[
|E_i(S)|=\frac{k-w_i(f)}{2}.
]

Summing over coordinates gives
[
|E(G_f)|=n|S|-2|E(Q_n[S])|.
]

## Parity-product lift

Let
[
p_r(z)=z_1\oplus\cdots\oplus z_r
]
and define
[
F_r(x,z)=f_A(x)\oplus p_r(z),
\qquad
G_r(x,z)=f_B(x)\oplus p_r(z).
]

For every (r\ge0),
[
G_{F_r}=G_{f_A}\square Q_r,
\qquad
G_{G_r}=G_{f_B}\square Q_r.
]

Because adjacency eigenvalues of a Cartesian product are pairwise sums of factor eigenvalues, exact cospectrality is preserved.

The base full graphs each contain 12 isolated vertices. For (r\ge1), each such vertex produces a component isomorphic to (Q_r). Therefore
[
\operatorname{Comp}(F_r)=
\bigl(
16\cdot2^r,
4\cdot2^r,
\underbrace{2^r,\ldots,2^r}_{12}
\bigr),
]
[
\operatorname{Comp}(G_r)=
\bigl(
11\cdot2^r,
9\cdot2^r,
\underbrace{2^r,\ldots,2^r}_{12}
\bigr),
]
and
[
\operatorname{Diam}(F_r)=
\bigl(
6+r,
2+r,
\underbrace{r,\ldots,r}_{12}
\bigr),
]
[
\operatorname{Diam}(G_r)=
\bigl(
4+r,
4+r,
\underbrace{r,\ldots,r}_{12}
\bigr).
]

At (r=0), omitting isolated vertices recovers the base active profiles.

## Complexity under parity lift

For a nonconstant Boolean function (h), write
[
H_r(x,z)=h(x)\oplus p_r(z).
]

Then
[
s(H_r)=s(h)+r,
\qquad
bs(H_r)=bs(h)+r,
\qquad
D(H_r)=D(h)+r.
]

Pointwise certificate complexity satisfies
[
C(H_r;(x,z))=C(h;x)+r,
]
so
[
C(H_r)=C(h)+r.
]

For (r\ge1),
[
C_0(H_r)=C_1(H_r)=C(h)+r.
]

The block-sensitivity identity follows because an optimal disjoint sensitive-block family for (h) can be augmented by the (r) fresh singleton parity coordinates, while any disjoint sensitive-block family for (H_r) contains at most (bs(h,x)) blocks with even fresh-coordinate parity and at most (r) blocks containing an odd number of fresh coordinates.

For deterministic decision trees, the upper bound is obtained by querying all fresh parity variables and then evaluating (h). For the lower bound, every root-to-leaf path must query every fresh coordinate; fixing their values and deleting those queries leaves a decision tree for (h) or its complement.

Every certificate must likewise fix all fresh coordinates, after which the remaining fixed original coordinates must certify the corresponding value of (h).

For the explicit witnesses,
[
\deg_{\mathbb F_2}(H_r)=5,
\qquad
\deg_{\mathbb R}(H_r)=5+r.
]

The sensitive-edge count is
[
|E(G_{H_r})|
=
21\cdot2^r+32r2^{r-1}.
]

Original directional counts are multiplied by (2^r), each fresh coordinate contributes (16\cdot2^r) sensitive edges, and every base graph degree (d) becomes (d+r) with multiplicity multiplied by (2^r).

## Infinite strengthened separation

For every integer (N\ge5), set (r=N-5). Then (F_r) and (G_r) have identical strengthened summaries
[
S^\dagger(F_r)=S^\dagger(G_r),
]
their active sensitivity graphs are exactly adjacency-cospectral, and their active component-size and diameter profiles differ.

The result is a non-determination theorem for Boolean sensitivity-graph geometry. It does not imply a hardware speedup, a physical lower bound, or a new computational model.

## Citation

Akhtar, M. A. K. (2026). _Cospectral Boolean Sensitivity Graphs Can Have Different Global Geometry: An Exact Separation and Infinite Family_ (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23062628
