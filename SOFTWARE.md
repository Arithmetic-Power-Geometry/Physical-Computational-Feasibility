# Software

This repository contains exact small-n Boolean-function analysis and reproducible search software supporting the Physical Computational Feasibility research programme.

## Modules

- `pcf.boolean_geometry`: sensitivity graphs and residual graph geometry.
- `pcf.measures`: exact small-n Boolean complexity measures, including GF(2) ANF degree and real multilinear polynomial degree.
- `pcf.transport`: local transport and refresh models.
- `pcf.capacity`: endpoint-capacity models.
- `pcf.layout`: physical-layout baselines.
- `scripts.search_n5`: symmetry-reduced targeted n=5 search with progressive refinement.
- `scripts.campaign_n5`: deterministic multi-seed campaign and machine-readable artifacts.

## Verification

GitHub Actions first compiles the Python sources, then runs regression tests, then executes the n=5 campaign and uploads its CSV/JSON artifacts. A search result is not treated as evidence unless the corresponding verification workflow completes successfully.

## Exact and numerical quantities

Combinatorial quantities are computed exactly for the small instances used here. Spectral radius is used numerically during search/refinement. For the central n=5 witness, exact adjacency cospectrality is independently verified by equality of the integer characteristic polynomials of the active sensitivity graphs.

## Scope

The software is an independent research implementation. It does not generate a manuscript. A later article may report results reproduced by the software and archived artifacts.

## Limitations

Full enumeration of all 2^32 five-variable Boolean functions is not attempted. The structured sparse-layer search exhaustively enumerates all C(32,4)=35,960 truth sets with four positive inputs and all C(32,5)=201,376 truth sets with five positive inputs; broader n=5 random campaigns remain finite evidence only.
