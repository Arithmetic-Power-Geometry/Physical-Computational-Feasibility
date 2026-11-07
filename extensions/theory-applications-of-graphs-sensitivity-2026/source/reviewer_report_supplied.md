Manuscript: Cospectral Boolean Sensitivity Graphs Can Have Different Global Geometry: An Exact Separation and Infinite Family

Material: 17-page manuscript and accompanying LaTeX submission package.

Major revision recommended

# Current assessment: 78/100

Target: 95+/100 in manuscript readiness, not a guaranteed 95% acceptance probability.

I am evaluating the manuscript as a skeptical referee looking for grounds to recommend rejection. The central construction is mathematically interesting, but three questions are decisive:

1. Is the construction genuinely new relative to cospectral graph constructions and existing Boolean sensitivity research?
2. Is the computational enumeration completely and independently reproducible?
3. Is the theorem mathematically substantial enough for Discrete Mathematics, rather than an isolated computational counterexample with a standard lifting argument?

The manuscript's strongest section is the exact five-variable witness. Its weakest elements are the claim of exhaustive classification, the depth of the novelty comparison, and the mathematical significance developed beyond the witness.

I would not recommend submission in its present form. The corrections below are intended to eliminate substantive rejection risks, not merely improve the language.

## 1. Deep literature comparison: where rejection risk arises

The journal explicitly seeks significant research in discrete mathematics and includes graph theory, enumeration and algebraic combinatorics. It also states that papers principally focused on experimental results fall outside its scope. This means your finite enumeration is acceptable as supporting evidence, but the central contribution must stand as a mathematical theorem.&#x20;

Elsevier Shop



I examined relevant published work, including:

| Prior research                                                                                                                                                   | What the referee may challenge                                         | What your manuscript must establish                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [Abiad et al., Counting cospectral graphs obtained via switching](https://doi.org/10.1016/j.disc.2025.114775?utm_source=chatgpt.com) (2026)                      | Cospectral constructions and computational enumeration are established | Why the Boolean cut-graph restriction and matched complexity controls yield a distinct result |
| [Mao and Yan, Constructing cospectral graphs via regular rational orthogonal matrices](https://doi.org/10.1016/j.disc.2025.114542?utm_source=chatgpt.com) (2025) | New cospectral families already arise from algebraic constructions     | Whether your witness follows from a known switching construction                              |
| [Van Dam and Haemers, Developments on spectral characterizations of graphs](https://doi.org/10.1016/j.disc.2008.08.019?utm_source=chatgpt.com) (2009)            | Non-identifiability from spectra is classical                          | Why your restricted graph family creates a meaningful new obstruction                         |
| [Hatami, Kulkarni and Pankratov, Variations on the Sensitivity Conjecture](https://doi.org/10.4086/toc.gs.2011.004?utm_source=chatgpt.com)                       | Boolean complexity separations are a mature subject                    | Why simultaneous equality of your controls is significant                                     |

The recent switching paper develops a general counting framework with asymptotic results, while the 2025 construction paper introduces new switching mechanisms. These are stronger forms of general mathematical development than simply exhibiting one exceptional pair.&#x20;

ScienceDirect+1



Novelty finding: I did not find an exact published duplicate of your specific five-variable pair in the material examined. However, the search is not exhaustive, and I have not established that your example cannot be obtained through an existing switching theorem.

### A deeper mathematical observation

Your witness sets each contain five positive inputs. The sensitivity graph is therefore a bipartite graph whose edges cross between the five positive inputs and the 27 negative inputs.

This gives a useful alternative representation. Let \\(M\\) be the \\(5\times27\\) incidence matrix between the positive and negative vertices. Then

\\[ A(G_f)= \begin{pmatrix} 0&M\\\ M^\top&0 \end{pmatrix}. \\]

Consequently, the nonzero eigenvalues of the sensitivity graph are determined by the eigenvalues of the much smaller matrix \\(MM^\top\\).

This is potentially important for strengthening the paper. Rather than treating cospectrality only as the output of a 20-vertex characteristic-polynomial computation, you could derive it through a small exact matrix determined by the pairwise geometry of the five positive vertices.

That could produce a more elegant, self-contained mathematical proof and possibly a structural classification theorem.

It is not automatically a new result: the block-matrix spectral identity is standard. The opportunity for novelty lies in using it to characterize when distinct sparse Boolean truth sets produce cospectral sensitivity graphs with different component geometry.

## 2. Detailed section-by-section rejection report

Scores are editorial judgments of the current presentation. They are not empirical acceptance probabilities.

| Section                     | Current | Target | Rejection risk |
| --------------------------- | ------- | ------ | -------------- |
| Title and abstract          | 85      | 96     | Moderate       |
| 1. Introduction             | 78      | 95     | High           |
| 2. Related work             | 68      | 96     | Very high      |
| 3. Definitions              | 87      | 98     | Low–moderate   |
| 4. Exact separation         | 86      | 99     | High           |
| 5. Exhaustive verification  | 65      | 98     | Very high      |
| 6. Directional sensitivity  | 82      | 95     | Moderate       |
| 7. Infinite-family theorem  | 85      | 99     | High           |
| 8. Summary-mediated models  | 45      | 95     | Very high      |
| 9. Reproducibility          | 65      | 98     | High           |
| 10. Limitations             | 88      | 96     | Low            |
| 11. Discussion              | 70      | 95     | High           |
| 12. Conclusion              | 82      | 96     | Moderate       |
| References and declarations | 73      | 98     | High           |

### Title and abstract — Page 1

Potential rejection comment: The abstract lists numerous matched invariants, but it does not sufficiently communicate why their simultaneous equality constitutes an important mathematical discovery.

The exhaustive-search count occupies valuable abstract space, while the structural mechanism of cospectrality remains unexplained.

Required improvements: Lead with the non-determination problem for sensitivity graphs, state the exact theorem, and explain why the restriction to Boolean cube cuts matters. Move the enumeration count after the mathematical result. Avoid implying that all of the listed invariants provide independent constraints; some are redundant.

95+ criterion: A mathematician unfamiliar with Boolean sensitivity should understand the problem, new theorem, and significance from the abstract alone.

### Section 1 — Introduction, pages 1–2

Potential rejection comment: The motivation is reasonable, but the paper does not formulate a sharply defined research question whose answer is demonstrably absent from the literature.

The manuscript says that the unresolved issue concerns complete spectral information and matched Boolean measures. It must distinguish a genuinely open problem from a question introduced by the authors for this particular combination of invariants.

Required improvements: Formulate the determination problem precisely. Explain why this class of graphs is restrictive, what is already known for ordinary cospectral graphs, and what is genuinely not established for Boolean sensitivity graphs. State the main theorem near the end of the introduction rather than relying entirely on a contribution list.

A useful mathematical framing is:

\\[ \mathcal S(f)=\mathcal S(g) \quad\not\Rightarrow\quad \operatorname{Comp}(G_f)=\operatorname{Comp}(G_g). \\]

Make clear that \\(\mathcal S\\) includes the full adjacency spectrum and the specified complexity measures.

95+ criterion: The introduction identifies a well-motivated determination problem and makes the contribution understandable without the software.

### Section 2 — Background and related work, pages 2–4

Potential rejection comment: The section is extensive but insufficiently discriminating. It contains numerous references on quantum query complexity, general reproducibility, and classical graph theory without directly testing the novelty of the proposed construction.

Table 1 groups literature into broad methodological categories, but does not compare the strongest competing cospectral constructions at theorem level.

Required improvements: Replace much of the broad survey with a focused comparison of graph cospectrality, sensitivity graphs, hypercube cut structure, switching constructions, and spectral sensitivity. Compare exact hypotheses and conclusions, not just topics.

Specifically, investigate whether the witness can be generated by Godsil–McKay switching or related transformations, and whether a smaller or simpler restricted counterexample is already known.

95+ criterion: Every novelty assertion is supported by a precise comparison with the closest known theorem.

### Section 3 — Definitions, pages 4–5

Potential rejection comment: The strengthened summary \\(S^\dagger(f)\\) combines mathematically independent information with quantities that are already determined by other entries.

For example, the full adjacency spectrum determines the number of graph edges through

\\[ |E(G)|=\frac12\sum_i\lambda_i^2. \\]

Likewise, the degree histogram determines both the maximum degree and the total edge count.

The summary is legitimate, but describing all entries as separate strengths may exaggerate the mathematical restrictions.

Required improvements: Distinguish primary constraints from redundant reporting quantities. Specify whether the spectrum refers to the active graph or the full graph throughout. Define component profiles and diameters precisely, including isolated vertices.

95+ criterion: A minimal, unambiguous mathematical definition of the controlled information, followed by any additional statistics retained for interpretability.

### Section 4 — Exact five-variable separation, pages 5–6

Potential rejection comment: The paper provides an exact characteristic polynomial, but the main proof still depends on computationally asserted invariants rather than a sufficiently transparent mathematical derivation.

This is the strongest section and deserves the most rigorous treatment.

The witness sets are:

\\[ A=\\{00000,01000,10000,11100,11111\\}, \\]

\\[ B=\\{00000,00011,00101,01000,10000\\}. \\]

Required improvements: Derive the active component structures directly from the induced positive-input subgraphs and their cube neighborhoods. Show why both characteristic polynomials agree using a compact incidence or Gram matrix. Provide independently checkable arguments for the Boolean-complexity controls, particularly block sensitivity, certificate complexity and decision-tree depth.

Figure 1 illustrates the difference, but its small labels and dense layout make the graph structure difficult to verify visually. A clean mathematical diagram with labeled vertices would be better.

95+ criterion: The main counterexample is independently verifiable from the printed manuscript, without executing the code.

### Section 5 — Exhaustive finite verification, page 7

Critical methodological risk

Potential rejection comment: The exhaustive-search claims are not sufficiently defined to support the reported classification counts.

Algorithm 1 states that the search canonicalizes under input-variable permutations and output complementation. However, output complementation changes a truth set of size five into one of size 27, so it does not act internally on the fixed \\(k=5\\) layer.

This does not necessarily invalidate the enumeration, but it makes the stated equivalence procedure ambiguous.

Furthermore, the algorithm refines candidates using numerical spectral radius before exact characteristic-polynomial verification. A numerically rounded value must not be used to exclude a genuinely cospectral pair.

Required improvements:

- Define the exact symmetry group acting on the fixed-weight layer.
- Explain how output complementation is handled.
- State whether input bit translations are included or excluded.
- Define precisely what counts as a canonical representative, cheap bucket, collision class and strong separation.
- Prove that every pruning step preserves all possible qualifying pairs.
- Recompute the reported counts with an independent implementation.
- Replace numerical spectral-radius filtering with exact arithmetic, or prove that its numerical use cannot cause false exclusions.

Table 3 reports 625 and 2,674 canonical representatives. These counts require independently reproducible certificates, not merely an assertion that the search was exhaustive.

95+ criterion: An independent researcher can reproduce every enumeration count and prove that no eligible candidate was discarded.

### Section 6 — Directional sensitivity, page 8

Potential rejection comment: The identity

\\[ w_i(f)=|S|-2|E_i(S)| \\]

is elementary edge counting and does not constitute a substantial new result.

Required improvements: Keep the identity, but make it a supporting observation within the sparse-set structural analysis. Use it to derive meaningful constraints on possible cospectral pairs or on the search space.

If it yields no further mathematical consequences, a separate section is unnecessary.

95+ criterion: The identity contributes to a nontrivial structural argument rather than standing alone as an elementary lemma.

### Section 7 — Infinite-family theorem, pages 8–10

Potential rejection comment: The infinite-family theorem is valid in concept, but the construction uses a standard Cartesian-product spectral law. Its mathematical significance must be separated from the novelty of the original witness.

The parity lift is

\\[ F_r(x,z)=f_A(x)\oplus p_r(z), \qquad G_r(x,z)=f_B(x)\oplus p_r(z). \\]

The graph identity

\\[ G\_{F_r}=G\_{f_A}\square Q_r \\]

is straightforward. The more delicate part is proving all Boolean-complexity transformations rigorously.

Required improvements: Present a complete proof of each complexity identity, particularly the decision-tree lower bound. Explicitly handle \\(r=0\\) separately from \\(r\geq1\\), because formerly isolated vertices become non-isolated after lifting.

Table 4 should distinguish general parity-lift identities from identities specific to the five-variable witness.

95+ criterion: The theorem is fully self-contained, its edge cases are explicit, and every claimed invariant is justified.

### Section 8 — Summary-mediated models, page 11

Potential rejection comment: Proposition 1 is a tautological consequence of function composition:

\\[ S(f)=S(g)\implies\Phi(S(f))=\Phi(S(g)). \\]

It is not an independent mathematical discovery.

The language about computational or physical models also introduces applications that the manuscript does not demonstrate.

Required improvements: Remove this as a numbered proposition and standalone section. Retain a brief consequence in the discussion, without implying hardware performance, physical-resource bounds, or predictive benefits.

95+ criterion: Every numbered theorem or proposition represents a substantive mathematical contribution.

### Section 9 — Reproducibility, page 11

Potential rejection comment: The repository is identified only as “GitHub: Physical Computational Feasibility.” The printed manuscript does not provide a complete repository URL or immutable release identifier.

The ZIP contains the LaTeX manuscript, figures, bibliography and a parity-lift regression CSV, but it is not itself a complete independent verification package for the 201,376-case search.

Required improvements: Provide a public repository URL, exact commit, release archive, dependency versions, executable commands, expected outputs, and checksums. Include the exhaustive-search scripts and a separately implemented verifier.

95+ criterion: A referee can independently regenerate the witness, verify the polynomial and reproduce Table 3 from a fixed archived artifact.

### Section 10 — Limitations, pages 11–12

Potential rejection comment: The limitations are generally appropriate, but the paper acknowledges that it has not established minimality or a broader structural classification. This reinforces the question of mathematical significance.

Required improvements: State exactly what is proved, what is not proved, and which conclusions depend on enumeration. Avoid presenting unproved future possibilities as consequences.

95+ criterion: Every limitation is precise and consistent with the theorem statements.

### Section 11 — Discussion, page 12

Potential rejection comment: The discussion repeats the matching invariants and component differences rather than extracting new mathematical insight.

Required improvements: Explain why the counterexample exists structurally. Discuss the role of the positive-input incidence matrix, the restrictions imposed by the hypercube, and what additional invariants could distinguish the graphs.

A structural explanation of why cospectrality survives while component geometry changes would be substantially more valuable than repeating the comparison table.

95+ criterion: The discussion explains the mathematical mechanism and establishes the significance of the theorem.

### Section 12 — Conclusion, page 12

Potential rejection comment: The conclusion largely repeats the abstract and introduction.

Required improvements: State the non-determination theorem concisely, distinguish the explicit construction from the standard parity lift, and identify one precise unresolved mathematical problem.

95+ criterion: A short conclusion that states exactly what has been proved and why it matters.

### References and declarations — Pages 13–17

Potential rejection comment: The reference list is disproportionately long relative to the focused mathematical contribution, and several sources on reproducible research or quantum computing do not materially support the theorem.

There is also an internal authorship inconsistency: the title page lists two authors, but the conflict-of-interest statement uses the singular “author.”

Required improvements: Verify every bibliographic record and DOI; prioritize the closest spectral-graph and Boolean-complexity results. Ensure the declarations consistently reflect both authors and their actual contributions.

The publicly indexed SSRN version lists one author, whereas this submitted version lists two. This is not automatically improper, but the publication record and contribution history should be consistent and transparent.&#x20;

SSRN



95+ criterion: Accurate, relevant references and internally consistent publication declarations.

## 3. The research improvements most likely to change the editorial decision

The preceding corrections are necessary, but they are not equally valuable. I would prioritize the following research tasks.

Priority 1 — Prove a structural cospectrality criterion

Express the sensitivity graph through its positive-to-negative incidence matrix and derive an exact criterion for cospectrality from \\(MM^\top\\). For the present five-point witness, establish the equality by symbolic calculation and investigate whether the criterion extends to a larger class of truth sets.

Potential outcome: A stronger mathematical theorem rather than an isolated verified example.

Priority 2 — Establish a rigorous minimality or classification result

Investigate all Boolean functions in dimensions below five, using symmetry reduction with a proven completeness argument. Determine whether the same strengthened separation is impossible in smaller dimensions.

Potential outcome: A genuine minimality theorem, but only if the exhaustive classification supports it.

Priority 3 — Test known cospectral switching mechanisms

Examine whether the witness is generated by an existing switching operation, and whether the operation preserves the Boolean sensitivity-graph constraints.

Potential outcome: Either a clearer novelty distinction or an important correction to the novelty claim.

Priority 4 — Independently certify the exhaustive search

Reproduce the canonical counts, collision classes, complexity controls and exact characteristic polynomials using an independent verifier. Supply exact arithmetic and a formally specified equivalence relation.

Potential outcome: Elimination of the strongest reproducibility-based rejection risk.

## 4. Recommended revised manuscript structure

I would reorganize the paper to concentrate the mathematical argument.

| Revised section                         | Content                                                                            |
| --------------------------------------- | ---------------------------------------------------------------------------------- |
| 1. Introduction                         | Determination problem, motivation and principal results                            |
| 2. Preliminaries                        | Sensitivity graphs, Boolean measures and spectral controls                         |
| 3. Structural characterization          | Incidence-matrix approach and any newly proved criterion                           |
| 4. Exact counterexample                 | Explicit truth sets, self-contained proof and component geometry                   |
| 5. Minimality and finite classification | Only results rigorously established by exhaustive verification                     |
| 6. Infinite-family construction         | Parity lift, exact transformation laws and complete proof                          |
| 7. Consequences and discussion          | What the spectrum cannot determine and remaining mathematical questions            |
| 8. Conclusion                           | Concise theorem-level conclusion                                                   |
| Appendix / supplementary material       | Enumeration algorithms, verification tables, code and reproducibility instructions |

This would also remove the present standalone elementary modeling proposition and reduce repetition.

## 5. Realistic assessment of the 95+ target

Manuscript-readiness assessment

Current

# 78/100

Aspirational target

# 95+/100

The target is conditional on successful mathematical verification, stronger originality evidence, and substantive revision. It is not a predicted acceptance probability.

### Final referee recommendation

Decision on the present manuscript: Major revision before submission, with a substantial risk of rejection for insufficient mathematical significance.

The main witness is promising. The paper's weakness is not its length, typography or number of references. It is the absence of a sufficiently developed structural theory explaining the constrained cospectrality phenomenon.

I would pursue the incidence-matrix structural theorem first, because it directly addresses both mathematical depth and novelty. Then I would independently verify the exhaustive classification and investigate minimality.

If these investigations yield a new, nontrivial theorem, the paper could become substantially more competitive for Discrete Mathematics. If they do not, the existing exact counterexample may still be publishable, but its best venue and presentation would need to be reconsidered.

A 95+ editorial-readiness assessment is a useful quality target; no responsible reviewer can promise a 95% acceptance chance.