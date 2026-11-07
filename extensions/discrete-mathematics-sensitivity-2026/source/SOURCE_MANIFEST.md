# Uploaded source manifest (2026-11-07)

These values were computed directly from the uploaded files. **Listed != committed**. The GitHub connector cannot directly transfer attached binary files in this initial step; the original archives were not uploaded to the repo.

| Uploaded file | Size (bytes) | SHA-256 |
|---|---:|---|
| Pasted markdown(20261107-120014).md | 24621 | `4ef3eb716ebceb82560ea65db49346f2a28d70446010fa325675b50927743a05` |
| elsarticle(4).zip | 1430199 | `0b093093e84db49f99bcc9a7c3f69ed1fb61b0147c6d296427aff7963e7f50f6` |
| Sensitivity_LaTeX_Submission_Package(3).zip | 3456546 | `2e75ff94bb1cdfcc14648d3911bdd083c9058f38830018d00d8bd8f40c2b1527` |

## Internal manuscript ZIP members (hashes of original unmodified bytes)

| Member | Bytes | SHA-256 |
|---|---:|---|
| paper.tex | 38315 | `6b3bb6684b58eeb109b949f2da17b370f8763f511df1ba8cfb6c7684230748e1` |
| paper_anonymous.tex | 37254 | `43bcc06ba7416bbf565b64aabb5d9153aeef1fd9ffedf12e040855e0010f7694` |
| references.bib | 19001 | `edcca8bab922e86e32a32802b88a93ffc4cf5d5acd22eed70ceb7252ff28836b` |
| figure1_witness_graphs.jpg | 238239 | `d478bc572c0ef849acc3ca2f7d10bb09788e84d0cfa118bdca0ffa014c680d4b` |
| figure2_invariant_hierarchy.jpg | 239044 | `cc11b09750aca2a886629d374cd03fd4e206d208dae3a4254ead06e9babf460c` |
| figure3_parity_lift.jpg | 189871 | `3ecb2c5a735c2f9793d9c5d1e32f84144e6939477a6cd0eecc2bafe5cce73257` |

## Baseline facts inspected

- The original `paper.tex` uses `\\documentclass[11pt]{article}`, `biblatex` with `backend=biber`, `\\parencite` and `\\printbibliography`.
- It identifies Anand Nayyar as corresponding author; this must be changed in the revised copy only, with corresponding-author agreement.
- The supplied elsarticle archive contains sample `elsarticle-template-num.tex`, `elsarticle-template-harv.tex`, `elsarticle-template-num-names.tex`, `elsarticle.dtx`, `elsarticle.ins`, `elsarticle-num.bst`, `elsarticle-harv.bst`, `elsarticle-num-names.bst`, and documentation.
- The complete LaTeX migration must translate `\\parencite` consistently rather than merely replace the class line.
