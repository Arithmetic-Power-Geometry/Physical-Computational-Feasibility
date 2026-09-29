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

Combinatorial quantities are computed exactly for the small instances used here. Spectral radius is presently numerical and is used as a search/refinement control rather than as an unverified exact identity; any candidate whose claim depends on spectral equality requires an independent exact or higher-precision verification step.

## Scope

The software is an independent research implementation. It does not generate a manuscript. A later article may report results reproduced by the software and archived artifacts.

## Limitations

Full enumeration at n=5 contains 2^32 Boolean functions and is not attempted. The n=5 procedure is a targeted, deterministic, symmetry-reduced sample search; absence of a witness in a finite campaign is not a proof of nonexistence.
