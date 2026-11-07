# Twelve sequential prompts — TAG submission research program

All stages update evidence and references, demonstrate proofs or exact tests, commit changes and report commit SHA. Keep unverified claims explicitly unverified. Each next prompt is introduced only after the prior stage.

| Prompt | Work |
|---|---|
| P01 | Import complete original source/figures and TAG template; fix corresponding-author record; build clean working manuscript |
| P02 | Independently verify five-variable witnesses, Boolean controls, spectra, components and distances |
| P03 | Develop and prove incidence/Gram structural cospectrality criterion |
| P04 | Verify minimum dimension or report scoped, incomplete classification |
| P05 | Replicate exhaustive n=5 sparse-layer enumeration; define exact orbits and safe pruning |
| P06 | Theorem-level novelty comparison including switching operations |
| P07 | Audit parity lifting, component geometry and Boolean-complexity proof |
| P08 | Verify all citations and build authoritative bibliography |
| P09 | Rewrite paper around rigorously proved results, reduce redundant propositions |
| P10 | Improve mathematical figures, tables, algorithm, appendix, code and checksums |
| P11 | Compile, validate and package paper in TAG-specific official formatting |
| P12 | Independent hostile-referee audit, accessibility, authorship and final release |

Official policies: https://digitalcommons.georgiasouthern.edu/tag/policies.html
Final formatting: https://digitalcommons.georgiasouthern.edu/tag/styleguide.html

TAG initial submission uses PDF; later final-form formatting specifies US-letter 8.5x11, 1-inch margins, single column, 12-point Times/comparable font, single spaced, no printed author names/title, page numbers, headers or footers. Its manuscript policy is single-blind by default with opt-in double-blind review. Separate submission metadata is required.

Progress: P00 new extension setup on 2026-11-07; P01 PARTIALLY EXECUTED (local TAG build passed; complete GitHub source/figures/PDF transfer blocked). P02-P12 NOT STARTED.

## 2026-11-07 execution update
P01 remains PARTIAL: local TAG PDF builds, but original binary ZIP/figures/full source are not yet in GitHub. P02 is PARTIAL: exact independent witness computation completed locally and an executable verifier and evidence report committed in `code/p02_verify_witness.py` and `evidence/P02_WITNESS_VERIFICATION.md`. Full enumeration and a separately implemented second checker remain outstanding. No completed-stage claim is made.

## 2026-11-07 archive upload and P02 update
P01 archive transfer VERIFIED: GitHub file `TAG_P01_Complete_Source_and_Build (1).zip`, blob `55db83326c4c885dc5ccf0952f0686ddfa86ffd8`, 34 ZIP entries, checksum validated. The full source exists in GitHub inside the ZIP, not yet unpacked as individual repository files. P02 witness cospectrality and geometry independently cross-checked in Python and JavaScript. P02 exhaustive enumeration, minimality and prior-art novelty still pending.

## P03 audit status, 2026-11-07
Exact full k4 and k5 S5 permutation-orbit enumeration independently reproduced (625, 2674). k5 cheap-bucket count 63 reproduced under explicitly defined exact key; k4 produces 24, not manuscript's 31, under that key. Strong separation count and minimality remain open; P03 is partial, not a full proof of uniqueness or minimum dimension. See `evidence/P03_EXHAUSTIVE_ORBIT_AUDIT.md`.

## P04 exact refinement milestone (2026-11-07)
All 3299 S5 representatives have been refined by exact integer Gram characteristic polynomials and geometry. Unique k5 geometry-discordant joint class contains 36 representatives, split 18/18 and sharing all strengthened Boolean complexity controls; no k4 discordance. k4 cheap bucket count is 24 under the explicit key, not the manuscript's 31. P04 scope is restricted to n=5,k=4/5 and S5 canonicalization; global minimality and literature novelty remain unproved. Code and report committed.

## P05 completed local minimum-dimension verification (2026-11-07)
Independent C++17 and Python/SymPy full n<=4 audits agree: 2,4,14,222 NPN orbits; no spectrum+strengthened-complexity matched pair with different active component geometry. Five is minimal **for this precisely defined phenomenon** when combined with the established n5 witness. Python source and CSV results committed; C++ local evidence archive available but C++ source not yet separately committed. See `evidence/P05_MINIMUM_DIMENSION_AUDIT.md`.

## P06 structural criterion and novelty boundary (2026-11-07)
Proved and computationally tested Boolean cube common-neighbour Gram criterion; all 256 Q3 functions checked, A/B exact 5×5 Gram polynomials certified, negative control tested. Prior art Godsil–McKay 1982 and later switching methods reviewed at source level. Novelty of the matrix identity rejected as classical; potential novelty restricted to Boolean sensitivity counterexample and rigorously scoped finite minimality. GM-switching non-equivalence not established. P06 source, proof and reference register committed.
