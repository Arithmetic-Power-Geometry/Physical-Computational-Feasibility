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
