# P08 — hostile-referee audit and manuscript correction register (2026-11-07)

## Materials actually inspected
The locally preserved editable TAG manuscript `/mnt/data/TAG_P01/manuscript/TAG_main.tex`, including its abstract, literature review, exact search algorithm, search-count table, parity-lift section and limitations, and the previously executed P02–P07 evidence in the research extension. The P07 local executable `/mnt/data/TAG_P07/verify_p07.py` was rerun successfully in this stage. The P06 falsification control was independently recomputed in SymPy: S={1,2} and T={3,4} on Q3 each have six cut edges, but their 2×2 Gram polynomials are respectively t²−6t+5 and t²−6t+9.

## Blocking issues and corrections

### BLOCKER 1: fixed-weight canonicalization
Original search text and Algorithm 1 claim 'input-variable permutations and output complement'. At fixed n=5,k=4 or 5, complement maps weight k to 32−k and is not a within-layer group action. Correct action is S5 input-coordinate permutations only, with 625 and 2674 orbits. The 2^(n+1)n! NPN group belongs to the separate all-weight n<=4 minimality audit, not the fixed-weight n5 search.

### BLOCKER 2: ambiguous/incorrect counts
Original table gives k4 cheap buckets 31 and 'collision classes' 26, without an exact computational definition. Recomputed cheap signature (sensitive-edge count, max sensitivity, complete degree histogram, sorted directional counts, essential variables) gives k4=24, k5=63. Exact Gram spectral classes are 27 and 86, and joint (cheap,spectrum) classes are 29 and 92. Under the fully specified protocol, there are 0 k4 and 1 k5 geometry-discordant joint classes surviving the Boolean-complexity refinement. Do not silently identify old 'collision classes' with new joint classes.

### BLOCKER 3: spectral-radius filtering
Original algorithm uses numerical spectral radius before exact polynomial checking, and claims exhaustive candidate elimination. Unless the numerical filter is backed by a mathematically rigorous safe tolerance/bound, it can produce false negatives. Replace the pruning with exact integer Gram characteristic polynomials on **all** canonical representatives. This is now the verified protocol.

### BLOCKER 4: strength of uniqueness claim
One surviving joint class in the n5 k5 search does not imply one unique pair, uniqueness among all n5 functions, or novelty relative to the literature. The 36 S5 representatives split 18/18 between geometry types. State exactly what 'one' means and cite executable evidence.

### BLOCKER 5: source availability and execution provenance
The user-uploaded full ZIP is preserved as a binary GitHub blob, and later P02–P07 scripts and reports are committed as text. The original ZIP is not unpacked into independent GitHub paths. Local verification is not GitHub Actions CI. Do not claim that the exact uploaded manuscript has already been revised or that a compiled updated TAG PDF exists. The new replacement LaTeX is in source/P08_EXACT_SEARCH_REPLACEMENT.tex and has not yet been merged into TAG_main.tex.

### CONDITIONAL: minimality scope
The n<=4 exhaustive negative result supports minimum essential dimension five for the **joint matched signature and geometry-separation condition**. It does not imply that all pairs of cospectral sensitivity graphs on <=4 variables are isomorphic. Present this as a computational theorem with code, group-action proof of completeness and independent execution.

### CONDITIONAL: parity-lift accuracy
At r=0, 12 singleton components are isolated and the 'active graph' omits them. At r>=1, those 12 copies of Q_r are nonisolated, so the active graph equals the full graph. Hence any 'active graph spectrum' formula must distinguish r=0 from r>=1, or explicitly use the full adjacency polynomial consistently. For r>=1, C0=C1=5+r; at r=0, (3,5). GF(2) degree is 5 for all r; real degree is 5+r. P07 local exact r=0..2 graph and r=0..1 complexity checks passed again.

### CONDITIONAL: bibliography and novelty
The Gram criterion, Cartesian-product spectral shifts and parity identities are classical. Godsil–McKay switching is a broad prior-art mechanism, but its ability to connect the specific sensitivity graphs has not been proved or disproved. The manuscript's broad statement that the question is 'unresolved' requires a targeted literature search before claiming priority. No external DOI, title or author metadata was independently revalidated in this P08 step; do not mark prior-art novelty 'complete'. The next gate is focused literature and BibTeX DOI audit.

## Deliverable and next gate
A drop-in LaTeX replacement for the search paragraph, algorithm and table has been committed as `source/P08_EXACT_SEARCH_REPLACEMENT.tex`. The replacement is not yet integrated into the main manuscript; a later P09 rewrite should integrate it and compile/check all references, tables and figures. The exact P07 verification script and evidence remain unchanged.

**Status:** mathematical witness and parity-lift argument survive the present audit; computational-method prose is NOT submission-ready until the corrections are integrated, independently compiled, and referenced to the exact reproducible source.
