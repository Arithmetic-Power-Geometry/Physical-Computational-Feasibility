# Novelty Audit

This file separates validated mathematics from conjecture and from ideas rejected during development.

Scores are internal research-priority estimates, not claims of publication novelty.

| Concept/result | Current assessment | Novelty estimate |
|---|---|---:|
| Bounded fan-in parity depth | established circuit reasoning | 10/100 |
| \(meq^d\ge n\) for parity | generalized dependency/light-cone counting | 20/100 |
| \(meq^d\ge\operatorname{ess}(f)\) | useful general form | 30/100 |
| Spatial causal-volume lower bound | established locality/light-cone territory | 15/100 |
| \(Np\ge n\) robust capacity bound | elementary information-capacity counting | 10/100 |
| Output entropy is distinct from dependency complexity | important but conceptually known | 35/100 |
| Noise-aware essential-edge distinguishability | useful bridge between physical decoding and Boolean sensitivity | 50/100 |
| Boolean sensitivity-edge preservation in physical state space | promising formulation | 55–60/100 |
| Problem-specific physical feasibility region | framework candidate; overlaps multi-resource complexity | 60–65/100 |
| Computational displacement / no-hidden-computation audit | useful methodological synthesis | 55–60/100 |
| Cross-resource sensitivity–noise–locality theorem | **not yet obtained** | 75–85/100 potential |

## Not claimed

The repository does **not** currently claim:

- a new law of physics;
- a post-quantum computational model;
- a universal advantage over classical or quantum computation;
- a new Boolean-complexity invariant;
- a breakthrough lower bound.

## Strongest surviving research question

Given a Boolean function \(f\) and a noisy physical implementation, what combinations of locality, time, precision, interaction order, state-space dimension and readout capability are necessary to preserve the distinguishability of all function-changing input perturbations?

The first benchmark family is:

- dictator;
- majority;
- parity;
- threshold functions;
- selected functions with different sensitivity/block-sensitivity/influence profiles.

## Breakthrough criterion

A result will be promoted from framework to breakthrough candidate only if all of the following hold:

1. a precise theorem is stated;
2. a proof or exhaustive finite verification is available;
3. known special cases are recovered correctly;
4. counterexamples and boundary conditions are documented;
5. the theorem is not reducible to a standard light-cone, Shannon-capacity, Boolean-sensitivity or thermodynamic bound;
6. software reproduces all reported numerical results;
7. GitHub Actions generates independent machine-readable artifacts.

Until then, novelty language remains conservative.


## Prior-art correction: regeneration

A literature stress test shows that reliable computation with noisy gates already contains strong results connecting sensitivity/block sensitivity, redundancy, depth, and tolerable noise. Signal-propagation work also derives information-decay and noisy-depth limits. Recent 2026 work develops conditional contraction coefficients for channels with side information, including quantum networks.

Accordingly:

| Candidate | Revised estimate | Decision |
|---|---:|---|
| "Refresh must cost something" | 15/100 | too general |
| Regeneration requires redundancy in noisy circuits | 10/100 | established territory |
| Sensitivity + noisy-gate redundancy | 10/100 | established |
| Conditional/side-information contraction as a general concept | 10/100 | active established literature |
| Current feasibility-window synthesis | 45–55/100 | useful framework |
| Task-specific feasibility boundary including explicit refresh resources | 60–70/100 potential | investigate |
| New quantitative bound not reducible to noisy-circuit/SDPI results | 80/100 potential | breakthrough target |

The repository therefore remains explicitly pre-breakthrough.


## Finite geometry separation

Exhaustive (n=4) enumeration found functions F111 and F393 with identical essential-variable count, total sensitivity, maximum sensitivity, and sensitivity-degree histogram, but different sensitivity-graph component structure, matching number, diameter profile, and spectral radius.

This is a valid finite separation, but the sensitivity graph and spectral sensitivity are established objects in Boolean-function complexity. The result therefore supports a new experimental question rather than a breakthrough claim.

| Item | Estimate | Status |
|---|---:|---|
| Explicit F111/F393 scalar-profile separation | 45/100 | new-to-project finite witness |
| Sensitivity graph | 0/100 as project novelty | established |
| Spectral sensitivity | 0/100 as project novelty | established |
| Non-spectral sensitivity-graph geometry as physical predictor | 60–70/100 potential | test next |
| A theorem linking such geometry to physical feasibility beyond known measures | 80+/100 potential | breakthrough target |


## Physical-layout novelty audit

The direct embedding route was stress-tested.

- Natural hypercube layout: total wire length collapses exactly to sensitive-edge count.
- Free one-dimensional layout: minimizing total edge length is the established Minimum Linear Arrangement problem.
- General graph embedding/layout has extensive VLSI, network-layout and combinatorial-optimization literature.

Therefore "physical embedding cost of the sensitivity graph" is not sufficient as the project's novelty.

The surviving novelty claim must be a **coupled feasibility law** rather than a single graph parameter.
