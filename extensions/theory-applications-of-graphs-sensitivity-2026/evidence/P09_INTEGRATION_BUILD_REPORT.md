# P09 integrated TAG manuscript — build and provenance

The revised 19-page TAG manuscript was compiled locally on 2026-11-07 using pdfLaTeX, Biber and latexmk. The exact revised source is in the separately supplied `TAG_P09_Integrated_Manuscript.zip`, which also contains all three figures, the original references.bib, BUILD.sh, PDF and SHA256SUMS.txt.

## Source integration
Original manuscript: `TAG_P01_Complete_Source_and_Build (1).zip`, preserved in this GitHub project root. P09 integrates P02–P08 witness, corrected exact S5 enumeration, n<=4 minimum-dimension certificate, Boolean-cut Gram criterion and parity lift. It corrects the false fixed-weight output-complement symmetry, k4 bucket count 31 to 24, and removes numerical spectral-radius candidate pruning. The old 'collision class' counts are not silently substituted for new joint-class counts.

## Exact local artifact SHA256
- TAG_main.tex: 034e45ce821a20caf4b3a91c12ed48d79f30f5de3379462a8aff0b747ab5e599
- TAG_main.pdf: 60ae56ba4b06aa2741508eca4abecd401b8c5f74caa9eb8e4614375794026aca
- references.bib: edcca8bab922e86e32a32802b88a93ffc4cf5d5acd22eed70ceb7252ff28836b
- BUILD.sh: 19ff9dfea703117652d178bedabb27ac1dd39086e46fea597c95ed382693f9e9

## Rebuild
Unpack the P09 ZIP, then run `bash BUILD.sh`. The script executes `latexmk -pdf -interaction=nonstopmode -halt-on-error TAG_main.tex`; latexmk detects the Biber bibliography. The PDF was 19 pages, 881239 bytes, and had no reported undefined references or overfull boxes. One underfull page warning is nonblocking.

## GitHub status (important)
The complete **revised 42,287-byte TAG_main.tex**, compiled PDF and three JPEGs are **NOT separately committed to GitHub** in this stage. The original P01 source archive and P02–P08 text proofs, algorithms, evidence, and registers are already on GitHub. This P09 provenance record and build instructions are committed as text. The full P09 ZIP is available as a conversation download, not a GitHub repository file. Do not claim the revised PDF or complete source has been committed until an upload or direct file commit is independently verified.

## Editorial gates
The author/coauthor identity block is retained in editable source but not printed in the final-form TAG PDF. Confirm coauthor participation and affiliations before submission. The bibliography compiles, but independent verification of every BibTeX metadata field and recent citation remains pending. The finite minimum-dimension result is explicitly computational; the novelty comparison does not claim independence from Godsil–McKay switching. The next stage should upload the exact revised ZIP or source, verify SHA256, audit bibliography and perform final visual/referee inspection.
