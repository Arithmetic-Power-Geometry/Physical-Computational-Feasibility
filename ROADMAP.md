# Research Roadmap

## Phase I — Theory

Status: **active**

- [x] Define complete computation chain: encoding → dynamics → readout.
- [x] Define essential-variable count.
- [x] Prove dependency-reach bound \(\operatorname{ess}(f)\le meq^d\).
- [x] Separate robust capacity from dependency complexity.
- [x] Define noise-aware essential-edge distinguishability.
- [x] Define physical computational feasibility region.
- [x] Add no-hidden-computation falsification rules.
- [x] Derive first sensitivity/dependency–noise feasibility inequality.
- [x] Stress-test first inequality against noisy-circuit and contraction literature.
- [ ] Add explicit refresh/redundancy resource model and search for a bound not reducible to known noisy-circuit results.
- [ ] Identify exact assumptions under which the inequality is tight.
- [ ] Compare with known Boolean-function measures.
- [ ] Freeze theory version 0.1 only after the candidate theorem survives.

## Phase II — Software

Begin only after the Phase-I definitions are stable.

Planned modules:

- Boolean-function enumerator for small \(n\);
- exact essential-variable and sensitivity-edge computation;
- block sensitivity and influence baselines;
- configurable physical encoding models;
- noisy-channel simulator;
- total-variation / Hellinger / KL distinguishability metrics;
- Pareto-feasibility explorer;
- counterexample search;
- theorem-bound verifier.

## Phase III — Test and compare

Initial functions:

1. dictator;
2. parity;
3. majority;
4. OR/AND;
5. threshold functions;
6. random Boolean functions for small \(n\);
7. matched pairs with equal output entropy but different sensitivity geometry.

Comparisons:

- essential-variable bound;
- sensitivity;
- block sensitivity;
- total influence;
- channel capacity;
- causal-cone size;
- physical distinguishability;
- proposed cross-resource bound.

## Phase IV — Reproducible workflow

GitHub Actions will:

1. install the software;
2. run unit tests;
3. enumerate benchmark functions;
4. execute noisy-embedding experiments;
5. verify inequalities;
6. create CSV/JSON summary tables;
7. generate plots;
8. upload a versioned artifact bundle.

## Phase V — Artifact

The workflow artifact will contain only generated outputs, for example:

```
artifact/
  manifest.json
  benchmark_summary.csv
  feasibility_frontiers.csv
  counterexamples.csv
  theorem_checks.json
  figures/
```

The artifact is evidence produced by the software, not a manuscript.

## Phase VI — Paper

Only after the theory, implementation and generated artifacts are stable should a manuscript be written externally from the verified findings.
