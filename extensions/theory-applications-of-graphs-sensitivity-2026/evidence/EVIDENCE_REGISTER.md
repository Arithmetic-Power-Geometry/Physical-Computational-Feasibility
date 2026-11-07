# Exact evidence and proof register — 2026-11-07

| ID | Claim | Status | Proof/certificate required |
|---|---|---|---|
| E01 | f_A/f_B five-variable witness and all sensitivity/complexity controls | Reported by manuscript, independently unverified in this setup | Independently computed truth masks, matrices, complexity certificate |
| E02 | Exact active characteristic polynomial equality | Manuscript-reported | Gram-matrix proof, independent exact polynomial |
| E03 | Components (16,4) versus (11,9); diameters (6,2) versus (4,4) | Manuscript-reported | Explicit labeled edge lists and independent graph traversal |
| E04 | n=5,k=5 exhaustive 201376 truth sets | Count of candidates is combinatorially correct, search coverage unverified | Complete enumeration log, code and hash |
| E05 | Canonical reps 625 and 2674; one strong collision | Unverified; symmetry action ambiguous | Formally defined group action, exact orbit counts, safe pruning |
| E06 | Novelty beyond known switching constructions | Open | Theorem-level literature comparison; switch testing |
| E07 | Parity lift spectral/product and Boolean measures | Manuscript claims | Formal proof audit and exact regression checks |
| E08 | TAG style and author metadata | Journal rules verified, conversion pending | Complete source, PDF build, separate author record |
| E09 | Raw source and figure archive upload | Not yet committed | GitHub verified byte archive + SHA256 |
| E10 | Mohammad Amir Khusru Akhtar as corresponding author | Recorded in metadata | Confirm reflected in source/portal and consent |

A claimed theorem is NOT considered independently verified merely because the uploaded manuscript states it. Preserve failures and contradictions and modify results accordingly.

## P01 verified local build, 2026-11-07
TAG_main.pdf compiled with pdflatex/Biber: 18 US-letter pages, 12pt, 1in margins; no printed title, author names or page numbers. Original 30 files extracted locally and preserved. Original ZIP, source, figures and PDF **not yet in GitHub**. Evidence report: `evidence/P01_EXECUTION_REPORT.md`. P01 remains PARTIAL. This build does not verify the paper's mathematical claims.

## P02 witness check
E01–E03 locally independently verified for explicit A/B via exact graph construction, BFS, Gram polynomial, certificate and query complexity DPs; see `evidence/P02_WITNESS_VERIFICATION.md` and `code/p02_verify_witness.py`. The one-sided certificate maxima are (C0,C1)=(3,5); individual positive-input certificate values are (4,4,4,5,5). E04–E06 remain unverified. P01 source transfer still open. P02 second independent checker still open.

## 2026-11-07 verified GitHub archive upload and independent P02 cross-check
The user-uploaded `TAG_P01_Complete_Source_and_Build (1).zip` is present at the extension root. GitHub content API reports 5,791,395 bytes, Git blob SHA `55db83326c4c885dc5ccf0952f0686ddfa86ffd8`, independently matched to the local archive bytes; SHA256 `b8f74b26238b5867de9a7853c3f051d8ff2cddf35fe5987b09df3e7582fd4919`. Local `ZipFile.testzip()` passed, 34 entries. Complete original and derived materials are now committed as one intact archive; individual files have NOT been extracted to GitHub paths. P01 archival gate passed; editable source-at-path gate remains open.
A separately implemented dependency-free JavaScript checker `code/p02_independent_js_check.js` independently recomputed 21 edges, 12 isolates, active component sizes/diameters (16,6),(4,2) versus (11,4),(9,4), and both exact Gram characteristic coefficient vectors `[1,-21,162,-578,957,-585]`. Its output matches the independent Python/SymPy witness check. P02 full exhaustive enumeration/minimality remains open.

## P03 independent fixed-weight enumeration, 2026-11-07
Exhaustive S5 orbit counts verified: k4 35960 raw / 625 orbits; k5 201376 raw / 2674 orbits. Exact inexpensive bucket signature (edges, maximum sensitivity, degree histogram, sorted directional counts, essential variables) yielded k4 **24**, contradicting manuscript's unqualified 31 under this explicitly defined protocol; k5 63 matches. Manuscript's k4=26 collision classes, k5=63 collision classes and k5=1 strong separation NOT independently verified. Output complement is not a within-layer symmetry. No n≤4 or all-weight minimality claim verified. See `evidence/P03_EXHAUSTIVE_ORBIT_AUDIT.md` and committed C++/Python scripts.

## P04 exact all-representative refinement (2026-11-07)
Locally executed exact spectral/geometry checks on all 625 k4 and 2674 k5 S5 representatives. k4: 24 cheap, 27 exact spectral, 29 joint cheap+spectral buckets; 0 geometry-discordant. k5: 63 cheap, 86 exact spectral, 92 joint buckets; **one** geometry-discordant bucket of 36 S5 representatives (18 per geometric type), all retaining (bs,D,C0,C1,GF2 degree,real degree)=(5,5,3,5,5,5). Full input hypercube automorphisms collapse these to two orbits, one per geometric type. No global minimality claim. The old k4=31 cheap-bucket count remains unsupported. See `evidence/P04_EXACT_SPECTRAL_COMPLEXITY_REFINEMENT.md` and `code/p04_exact_refinement.py`.

## P05 minimum-dimension exact audit (2026-11-07)
All Boolean functions n=1..4 exhaustively covered under full NPN action (input permutations, input bit flips, output complement). 2,4,14,222 NPN orbits; 2,4,14,222 distinct exact combined spectral/complexity signatures; zero geometry-discordant signatures. Independent local C++17 and Python/SymPy implementations agree. Exact no-floating-point computations. GitHub files: `code/p05_minimum_dimension_independent.py`, `evidence/P05_RESULTS.csv`, `evidence/P05_MINIMUM_DIMENSION_AUDIT.md`. This supports minimum dimension 5 for **the specified strengthened-signature phenomenon**, not all cospectral graph distinctions. Original n5 k4 bucket discrepancy remains unresolved.

## P06 exact Boolean-specific Gram criterion (2026-11-07)
Proved the explicit common-neighbour formula H_xx=n−d_S(x), H_xy=2−|N(x)∩N(y)∩S| if Hamming distance 2, otherwise 0. At fixed n and positive-fibre size k, sensitivity cospectrality iff the H characteristic polynomials agree, equivalently their first k integer power traces agree. Verified exact A/B 5×5 Gram matrices, 256 Q3 truth sets via independent incidence construction, and a falsification control with equal sensitive-edge counts but unequal spectra. Classical matrix consequences, **not claimed as a new general theorem**. Full GM-switching independence and exhaustive prior-art novelty are unproved. See `evidence/P06_STRUCTURAL_CRITERION_NOVELTY.md`.

## P07 parity-lift theorem (2026-11-07)
Proved Γ(f XOR parity_r)=Γ(f) Cartesian-product Q_r, exact shifted spectral polynomial and component sizes/diameters for all r>=0. The A/B pairs remain cospectral and nonisomorphic in every dimension 5+r. Both lifts have essential variables, sensitivity, block sensitivity and ordinary deterministic decision-tree depth 5+r; C0=C1=5+r for r>=1 (at r=0 C0=3,C1=5); GF2 degree remains 5, real degree 5+r. Local exact graph checks r=0,1,2 and complexity checks r=0,1 passed. See evidence/P07_PARITY_LIFT_THEOREM.md, evidence/P07_COMPONENTS.csv, evidence/P07_LOCAL_SHA256SUMS.txt and code/p07_parity_lift_verify.py. No CI run or complete global novelty audit claimed.

## P08 hostile-referee audit (2026-11-07)
Inspected original TAG_main.tex; found three blocking search-method problems: output complement incorrectly included in fixed-weight S5 canonicalization, k4 cheap count 31 not reproducible under explicit key (correct 24), and unsafe numerical spectral-radius pruning in claimed exhaustive algorithm. Created exact drop-in LaTeX replacement with k4/k5 orbit, cheap, spectral and joint counts and correctly scoped 'one' strong class. Re-ran local P07 exact verifier successfully. Independently recomputed P06 Q3 equal-edge noncospectral control in SymPy. See evidence/P08_HOSTILE_REFEREE_AUDIT.md and source/P08_EXACT_SEARCH_REPLACEMENT.tex. Main manuscript and compiled PDF NOT yet revised.
