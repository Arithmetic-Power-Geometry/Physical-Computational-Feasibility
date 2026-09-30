# Software

This repository provides the exact small-instance Boolean-function analysis and reproducible search code supporting the cospectral sensitivity-graph separation.

## Modules

- `pcf.boolean_geometry`: sensitivity graphs, active components, component diameters, matchings, directional sensitivity counts, and exact adjacency characteristic polynomials.
- `pcf.measures`: exact small-instance Boolean complexity measures including block sensitivity, certificate complexity, deterministic decision-tree depth, GF(2) degree, and real multilinear degree.
- `scripts.search_sparse_n5`: exhaustive (n=5) sparse-layer search for (k=4) and (k=5).
- `scripts.search_n5`: targeted (n=5) search with progressive refinement.
- `tests`: regression checks for the explicit witness and supporting invariants.

## Exact witness

The verified truth sets are

[
A=\{00000,01000,10000,11100,11111\},
qquad
B=\{00000,00011,00101,01000,10000\}.
]

For the active sensitivity graphs, exact cospectrality is verified by equality of the integer characteristic polynomial

[
\lambda^{10}(\lambda^2-5)(\lambda^2-3)^2(\lambda^4-10\lambda^2+13).
]

The graphs have active component-size profiles ((16,4)) and ((11,9)), with diameter profiles ((6,2)) and ((4,4)), respectively.

## Exhaustive scope

The sparse-layer search exhaustively enumerates:

- all (inom{32}{4}=35{,}960) five-variable truth sets with four positive inputs;
- all (inom{32}{5}=201{,}376) five-variable truth sets with five positive inputs.

The (k=4) layer has no surviving strong separation under the implemented refinement. The (k=5) layer has one surviving strengthened separation class under the repository's stated canonicalization and refinement procedure.

Full enumeration of all (2^{32}) five-variable Boolean functions is not performed.

## Parity lift

For (H_r(x,z)=h(x)\oplus p_r(z)),

[
G_{H_r}=G_h\square Q_r.
]

The exact transformation laws used by the associated result include

[
s(H_r)=s(h)+r,quad
bs(H_r)=bs(h)+r,quad
D(H_r)=D(h)+r,quad
C(H_r)=C(h)+r.
]

For (r\ge1), both one-sided certificate maxima equal (C(h)+r). For the displayed witnesses, GF(2) degree remains 5 and real multilinear degree becomes (5+r).

## Verification

The workflow compiles the Python sources, runs regression tests, and executes the configured searches. Combinatorial quantities used for the reported witness are computed exactly. Numerical spectral radius is used only as a search refinement; exact integer characteristic-polynomial equality establishes the cospectrality claim.

## Environment

Python 3.10 or later.

## Citation

Akhtar, M. A. K. (2026). _Cospectral Boolean Sensitivity Graphs Can Have Different Global Geometry: An Exact Separation and Infinite Family_ (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23062628
