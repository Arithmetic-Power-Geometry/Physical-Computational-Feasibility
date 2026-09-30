# Cospectral Boolean Sensitivity Graphs Can Have Different Global Geometry

Research software and exact verification for the Boolean sensitivity-graph separation described in:

**Mohammad Amir Khusru Akhtar (2026). _Cospectral Boolean Sensitivity Graphs Can Have Different Global Geometry: An Exact Separation and Infinite Family_. Version V1. Zenodo. https://doi.org/10.5281/zenodo.23062628**

## Result

For Boolean functions (f:{0,1}^n\to{0,1}), the sensitivity graph joins Hamming-neighbor inputs exactly when flipping the corresponding coordinate changes the output.

The repository verifies an explicit five-variable pair

[
A=\{00000,01000,10000,11100,11111\},
]

[
B=\{00000,00011,00101,01000,10000\},
]

with indicator functions (f_A) and (f_B).

The pair agrees in:

- essential-variable count;
- sensitive-edge count;
- maximum sensitivity;
- sensitivity-degree histogram;
- sorted directional sensitivity counts;
- block sensitivity;
- deterministic decision-tree depth;
- certificate complexity;
- GF(2) degree;
- real multilinear degree;
- maximum matching size;
- the complete adjacency spectrum of the active sensitivity graph.

The active sensitivity graphs nevertheless have different global geometry:

| Quantity | (f_A) | (f_B) |
|---|---:|---:|
| Active component sizes | ((16,4)) | ((11,9)) |
| Active component diameters | ((6,2)) | ((4,4)) |

Their active adjacency matrices have the common characteristic polynomial

[
\chi(\lambda)
=
\lambda^{10}(\lambda^2-5)(\lambda^2-3)^2
(\lambda^4-10\lambda^2+13).
]

Thus the graphs are exactly adjacency-cospectral while their component-size and diameter profiles differ.

## Exhaustive finite verification

For (n=5), the sparse layers (k=|f^{-1}(1)|=4) and (k=5) are exhaustively enumerated.

| Layer | Raw truth sets | Canonical representatives | Strong separation classes |
|---|---:|---:|---:|
| (k=4) | 35,960 | 625 | 0 |
| (k=5) | 201,376 | 2,674 | 1 |

The (k=4) result is only a finite negative control for that layer. The (k=5) result identifies the explicit witness above under the repository's stated canonicalization and refinement procedure.

## Infinite family

Let

[
p_r(z)=z_1\oplus\cdots\oplus z_r,
]

and define

[
F_r(x,z)=f_A(x)\oplus p_r(z),\qquad
G_r(x,z)=f_B(x)\oplus p_r(z).
]

Then

[
G_{F_r}=G_{f_A}\square Q_r,
\qquad
G_{G_r}=G_{f_B}\square Q_r.
]

The lift preserves exact cospectrality and equality of the matched Boolean-complexity controls while retaining different component-size and diameter profiles in every essential dimension (N\ge5).

For a nonconstant base function (h), writing (H_r=h\oplus p_r),

[
s(H_r)=s(h)+r,\quad
bs(H_r)=bs(h)+r,\quad
D(H_r)=D(h)+r,
]

and pointwise certificate complexity satisfies

[
C(H_r;(x,z))=C(h;x)+r.
]

For the displayed witnesses, GF(2) degree remains 5 and real multilinear degree becomes (5+r).

## Repository contents

- `pcf/` — exact sensitivity-graph and Boolean-complexity routines.
- `scripts/` — exhaustive sparse-layer and deterministic search programs.
- `tests/` — regression tests for the witness and supporting quantities.
- `.github/workflows/` — reproducible verification workflow.
- `SOFTWARE.md` — implementation and verification scope.
- `CITATION.cff` — citation metadata.

## Reproducibility

The software constructs sensitivity graphs, computes exact small-instance Boolean complexity measures, performs the sparse-layer searches, evaluates component geometry, and verifies the central witness using exact integer characteristic polynomials. Numerical spectral radius may be used during search refinement, but the reported cospectrality result is established exactly.

Python 3.10 or later is required.

## Citation

Akhtar, M. A. K. (2026). _Cospectral Boolean Sensitivity Graphs Can Have Different Global Geometry: An Exact Separation and Infinite Family_ (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23062628

## License

Apache License 2.0.

Copyright © 2026 Mohammad Amir Khusru Akhtar.
