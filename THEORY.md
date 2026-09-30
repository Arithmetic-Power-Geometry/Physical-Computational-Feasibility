# Theory

## 1. Scope

The project studies which combinations of physical resources are necessary for a system to compute a target function reliably.

The starting point is deliberately conservative:

- no computational advantage is inferred from a short logical description alone;
- no analog advantage is inferred from compact state dimension alone;
- no physical relaxation advantage is inferred from equilibrium alone;
- no learning/self-organization advantage is inferred without counting acquisition cost;
- no global observable is treated as free if its implementation, preparation or readout already contains the answer.

The framework therefore separates the full computation into stages

\[
x
\xrightarrow{\mathcal E}
S_0
\xrightarrow{\mathcal D}
S_T
\xrightarrow{\mathcal M}
Y,
\]

where \(\mathcal E\) is encoding/preparation, \(\mathcal D\) physical dynamics, and \(\mathcal M\) measurement/readout.

A valid comparison must account for all three stages.

---

## 2. Essential variables

Let

\[
f:\{0,1\}^n\to\{0,1\}.
\]

Input variable \(i\) is **essential** if

\[
\exists x\in\{0,1\}^n:
f(x)\ne f(x\oplus e_i).
\]

Define

\[
\operatorname{ess}(f)
=
\left|
\left\{
i:
\exists x,,
f(x)\ne f(x\oplus e_i)
\right\}
\right|.
\]

Examples:

- dictator \(f(x)=x_1\): \(\operatorname{ess}(f)=1\);
- majority on \(n\) variables: \(\operatorname{ess}(f)=n\);
- parity: \(\operatorname{ess}(f)=n\).

The output entropy may be one bit in all three cases. Essential-variable count therefore captures a different requirement from output information volume.

---

## 3. Dependency-reach proposition

### Assumptions

Consider a layered architecture satisfying:

1. **Encoder locality:** each initial encoded component depends on at most \(e\) original input variables.
2. **Interaction order:** each primitive at a later layer depends on at most \(q\) components from the previous layer.
3. **Depth:** there are \(d\) interaction layers.
4. **Readout locality:** the final decision depends on at most \(m\) layer-\(d\) components.

### Proposition 1

For any output computed by the architecture,

\[
\operatorname{ess}(f)\le m e q^d.
\]

Hence exact computation requires

\[
\boxed{m e q^d\ge \operatorname{ess}(f)}.
\]

### Proof

An encoded component depends on at most \(e\) input variables.

After one \(q\)-local layer, a component depends on at most \(eq\) original variables. Inductively, after \(d\) layers it depends on at most

\[
eq^d
\]

original variables.

A readout combining at most \(m\) such components therefore depends on at most

\[
meq^d
\]

original variables. Every essential variable of \(f\) must lie in this dependency set, yielding the result. \(\square\)

### Corollary: parity

For

\[
P_n(x)=x_1\oplus\cdots\oplus x_n,
\]

every input variable is essential, so

\[
\boxed{meq^d\ge n}.
\]

This proposition is a generalized dependency/light-cone counting result and is not presented as a novelty claim by itself.

---

## 4. Spatial propagation model

Suppose a local physical model has:

- spatial dimension \(D\);
- bounded input density \(\rho\);
- initial interaction radius \(r\);
- effective propagation speed \(v\);
- run time \(t\);
- \(m\) local readout regions.

A coarse causal-volume estimate gives

\[
N_{\mathrm{reachable}}
\lesssim
m\rho(r+vt)^D.
\]

A function with \(\operatorname{ess}(f)\) essential spatially distributed inputs therefore requires, subject to the stated assumptions,

\[
m\rho(r+vt)^D
\gtrsim
\operatorname{ess}(f).
\]

For parity this becomes

\[
m\rho(r+vt)^D\gtrsim n.
\]

This section is a model-specific locality bound; constants and geometry depend on the substrate.

---

## 5. Reliable analog capacity

If a physical representation uses \(N\) degrees of freedom and each degree of freedom admits at most \(2^p\) reliably distinguishable states, then the representation admits at most

\[
2^{Np}
\]

robust global states.

Losslessly representing \(n\) arbitrary bits requires

\[
2^{Np}\ge 2^n,
\]

hence

\[
\boxed{Np\ge n}.
\]

This is a capacity bound, not a computation lower bound for one-bit functions.

A one-bit function such as parity does **not** require an \(n\)-bit output channel. If an encoder maps directly to the parity bit, then the encoder has already implemented the global dependence. Therefore encoding complexity and dependency locality must remain explicit.

---

## 6. Noise-aware distinguishability

Let a physical device generate output distribution

\[
P_{Y|x}.
\]

For neighboring Boolean inputs define

\[
\Delta_i(x)
=
D_{\mathrm{TV}}
\left(
P_{Y|x},
P_{Y|x\oplus e_i}
\right).
\]

Whenever

\[
f(x)\ne f(x\oplus e_i),
\]

any decoder that must choose the correct value of \(f\) for both inputs with error at most \(\epsilon\) requires

\[
\boxed{
\Delta_i(x)\ge 1-2\epsilon
}.
\]

### Proposition 2

Define

\[
\Delta_{\min}(f)
=
\min_{x,i:\,f(x)\ne f(x\oplus e_i)}
\Delta_i(x).
\]

Worst-case error \(\epsilon\) implies

\[
\boxed{
\Delta_{\min}(f)\ge1-2\epsilon
}.
\]

### Reason

For two hypotheses with equal prior probabilities, optimal binary discrimination error is

\[
P_e^*
=
\frac{1-D_{\mathrm{TV}}(P,Q)}{2}.
\]

If a single decoder must achieve error at most \(\epsilon\), then the relevant distributions must satisfy the stated inequality.

---

## 7. Sensitivity-edge geometry

Define the sensitivity edge set

\[
\mathcal E_f
=
\left\{
(x,i):
f(x)\ne f(x\oplus e_i)
\right\}.
\]

Its cardinality is

\[
|\mathcal E_f|
=
\sum_x s(f,x),
\]

where \(s(f,x)\) is local Boolean sensitivity.

Parity has

\[
s(P_n,x)=n
\]

for every \(x\), so every edge of the Boolean hypercube changes the class label.

The physical encoding therefore must support reliable class separation across every parity-changing edge:

\[
D_{\mathrm{TV}}
\left(
P_{Y|x},
P_{Y|x\oplus e_i}
\right)
\ge1-2\epsilon
\qquad
\forall x,i.
\]

This motivates the main open problem:

> How do physical dimension, locality, interaction order, evolution time, dynamic range, noise and readout constrain the ability to preserve a large Boolean sensitivity-edge set under a physical encoding/dynamics/readout chain?

---

## 8. Physical computational feasibility region

For problem family \(P\), resource model \(\mathcal M\), and target error \(\epsilon\), define

\[
\mathfrak F_{P,\mathcal M,\epsilon}
=
\left\{
\mathbf R:
\exists
\text{ implementation in }\mathcal M
\text{ using }\mathbf R
\text{ with error}\le\epsilon
\right\}.
\]

The resource vector may include

\[
\mathbf R=
(N,p,e,q,d,m,t,\sigma,A,E,S,V,\ldots).
\]

No universal scalarization is assumed.

The object of study is the Pareto boundary

\[
\partial\mathfrak F_{P,\mathcal M,\epsilon}.
\]

A cross-resource theorem is scientifically interesting when it identifies a necessary relation among multiple resource coordinates that cannot be reduced to a single previously known bound.

---

## 9. Computational displacement

A purported improvement in one coordinate is not automatically an advantage.

For example:

- reducing depth may increase interaction order;
- reducing state dimension may require higher precision;
- simplifying readout may move computation into encoding;
- constant-time global response may require nonlocal preparation;
- postselection may hide cost in success probability;
- adaptive structure may hide cost in training or verification.

### No-Hidden-Computation criterion

Any claimed physical-computation advantage must explicitly account for:

\[
C_{\rm total}
=
C_{\rm encode}
+
C_{\rm prepare}
+
C_{\rm evolve}
+
C_{\rm precision}
+
C_{\rm measure}
+
C_{\rm verify}
+
C_{\rm failure}
+
C_{\rm reset},
\]

with physical resources retained separately whenever scalar addition would be unjustified.

---

## 10. Current open theorem target

The central target is not another causal-cone inequality.

We seek a theorem coupling at least two genuinely different resource mechanisms, for example:

- Boolean sensitivity-edge load and physical distinguishability;
- locality/time and noise contraction;
- analog precision and robust edge separation;
- interaction order and required measurement margin.

A representative target has the form

\[
\Psi
\left(
\mathcal E_f,
q,d,t,\sigma,A,m,p
\right)
\ge
L(f,\epsilon),
\]

where \(L\) is problem dependent and \(\Psi\) is not merely a repackaging of one-dimensional capacity or light-cone bounds.

No such general theorem is claimed in the present theory package.

---

## 11. Falsification rules

A candidate theorem is rejected or downgraded if it reduces directly to:

- circuit fan-in/depth;
- ordinary causal cones;
- Shannon channel capacity;
- elementary state counting;
- standard Boolean sensitivity/influence alone;
- communication complexity alone;
- rate-distortion alone;
- thermodynamic energy-time-accuracy bounds alone;
- an instance-specific encoder that has already solved the problem.

These rules are intentional: the purpose of the repository is to discover a genuinely nontrivial cross-resource law, not to rename known results.


---

## 12. Noise-contracted causal depth

The previous sections separately constrain whether an essential input can reach the readout and whether a function-changing perturbation remains distinguishable. This section couples the two under an explicit contraction model.

### Assumption: per-stage distinguishability contraction

Consider an essential input perturbation (x\leftrightarrow x\oplus e_i). Suppose its relevant physical signal travels through a causal route of length (ell_i). Assume each noisy stage along that route is a channel whose total-variation contraction coefficient is at most

[
0\le \eta<1.
]

Thus, for any two distributions entering one such stage,

[
D_{\mathrm{TV}}(KP,KQ)
\le
\eta D_{\mathrm{TV}}(P,Q).
]

Repeated application gives

[
D_{\mathrm{TV}}^{\mathrm{out}}
\le
\eta^{\ell_i}
D_{\mathrm{TV}}^{\mathrm{in}}
\le
\eta^{\ell_i}.
]

### Proposition 3 — essential-path contraction bound

If the device computes (f) with worst-case error at most (epsilon<1/2), then every function-changing perturbation routed through (ell_i) contractive stages must satisfy

[
\boxed{
\eta^{\ell_i}\ge1-2\epsilon
}.
]

### Proof

Proposition 2 requires output total-variation distance at least (1-2\epsilon) for every function-changing pair. Contractivity gives output distance at most (eta^{\ell_i}). Combining the inequalities yields the result. \(\square\)

For (0<\eta<1), this gives a maximum admissible noisy path length

[
\boxed{
\ell_i
\le
\frac{\ln(1-2\epsilon)}{\ln\eta}
}.
]

The numerator and denominator are both negative.

### Interpretation

Dependency reach imposes a **minimum** amount of propagation or aggregation. Noise contraction imposes a **maximum** amount of propagation through unrefreshed contractive stages. A reliable architecture exists only if these requirements overlap.

---

## 13. Balanced-tree parity feasibility window

Consider a balanced (q)-ary aggregation architecture with

[
e=m=1.
]

To make one readout depend on all (n) parity inputs, Proposition 1 requires

[
q^d\ge n,
]

so

[
d\ge \lceil\log_q n\rceil.
]

Under the homogeneous contraction assumption of Proposition 3, reliable computation also requires

[
d
\le
\frac{\ln(1-2\epsilon)}{\ln\eta}.
]

Therefore a necessary feasibility condition is

[
\boxed{
\lceil\log_q n\rceil
\le
\frac{\ln(1-2\epsilon)}{\ln\eta}
}.
]

Equivalently,

[
\boxed{
\eta^{\lceil\log_q n\rceil}
\ge
1-2\epsilon
}.
]

Ignoring the ceiling for a coarse continuous bound,

[
n
\lesssim
q^{
\ln(1-2\epsilon)/\ln\eta
}.
]

This is a **feasibility-window corollary**, not presently claimed as a new information-theoretic inequality. Its two ingredients are standard-style dependency growth and distinguishability contraction. Its role here is to make their resource conflict explicit for a problem-specific physical architecture.

### Example

Let

[
q=2,qquad \eta=0.9,qquad \epsilon=0.1.
]

Reliability requires output distinguishability at least

[
1-2\epsilon=0.8.
]

The contraction constraint permits at most

[
d
\le
\frac{\ln 0.8}{\ln 0.9}
\approx2.12.
]

Thus an integer-depth architecture can use at most two unrefreshed contractive aggregation stages. Binary parity dependency requires

[
d\ge\lceil\log_2 n\rceil.
]

Consequently this simplified model can support at most

[
n\le4
]

inputs under these assumptions.

This example is intentionally small: it demonstrates the collision of resource constraints, not a universal parity limit.

---

## 14. Limits of Proposition 3

The contraction theorem does not apply unchanged when:

- intermediate error correction or signal regeneration increases distinguishability using additional resources;
- fresh ancillas, redundancy or external free energy are injected;
- different stages have different contraction coefficients;
- multiple causal routes combine;
- the relevant metric is quantum trace distance rather than classical total variation;
- the physical dynamics are not Markovian stagewise channels.

These are not loopholes to ignore. They define the next resource coordinates that must be charged.

For heterogeneous stages,

[
D_{\mathrm{TV}}^{\mathrm{out}}
\le
\left(\prod_{j=1}^{\ell_i}\eta_j\right)
D_{\mathrm{TV}}^{\mathrm{in}},
]

giving the necessary condition

[
\boxed{
\prod_{j=1}^{\ell_i}\eta_j
\ge1-2\epsilon
}.
]

The next theory target is to include **refresh/regeneration cost** explicitly and determine whether increasing distinguishability after contraction necessarily consumes a quantifiable resource such as redundancy, energy, fresh low-entropy ancillas, extra time, or additional physical volume.



---

## 15. Regeneration and side-information accounting

A passive channel acting only on the current carrier cannot increase total-variation distinguishability. Therefore any apparent regeneration step that raises task-relevant distinguishability must use resources not contained in that degraded carrier alone.

Represent an active refresh stage as

\[
(S,Z)\xrightarrow{\mathcal R}S',
\]

where \(S\) is the degraded carrier and \(Z\) denotes additional physical resources such as redundant copies, correlated side information, fresh ancillas, external observations, or newly supplied task-relevant information.

The key accounting rule is:

> Distinguishability restoration is not free merely because it occurs inside a physical device; the source, preparation and reliability of \(Z\) must be included in the feasibility vector.

This rule does not by itself provide a new lower bound. Reliable noisy computation already has deep theories of redundancy, noise thresholds and signal propagation. In particular, known results lower-bound reliable noisy-circuit size in terms of sensitivity and block sensitivity, including logarithmic redundancy for parity-like functions.

### Consequence for this project

The project will not claim that "regeneration requires redundancy" is new.

Instead, refresh is represented explicitly by additional coordinates, for example

\[
\mathbf R_{\rm refresh}
=
(r, a, v, \tau, \xi, \ldots),
\]

where possible coordinates include redundancy width \(r\), fresh-ancilla count \(a\), physical volume \(v\), refresh time \(\tau\), and a model-specific reliability/resource coordinate \(\xi\).

A candidate cross-resource result must outperform a simple restatement of known noisy-circuit redundancy or contraction results.

---

## 16. Refined research target

After prior-art falsification, the target is now:

\[
\boxed{
\text{task geometry}
+
\text{dependency reach}
+
\text{noise}
+
\text{explicit refresh resources}
\Longrightarrow
\text{a model-specific feasibility boundary}
}
\]

with three requirements:

1. the dependency component cannot be reduced to ordinary output entropy;
2. the noise/refresh component cannot be reduced to a standard contraction coefficient or known noisy-gate redundancy theorem;
3. the resulting inequality must make a new quantitative prediction for at least one explicit physical architecture.

This is the threshold that must be met before the project claims a new theorem beyond framework synthesis.


---

## 17. Finite separation: scalar sensitivity does not determine sensitivity-edge geometry

For a Boolean function (f), let (G_f) be the graph on ({0,1}^n) containing exactly the hypercube edges across which (f) changes value.

An exhaustive enumeration at (n=4) produces a matched pair of Boolean functions with truth-table masks 111 and 393 (using lexicographic integer inputs (0,ldots,15), least-significant mask bit corresponding to input 0000).

Both functions have:

- 4 essential variables;
- 12 undirected sensitive edges (directed total sensitivity 24);
- maximum sensitivity 3;
- identical sensitivity-degree histogram: two vertices of degree 0, eight of degree 1, two of degree 2, and four of degree 3.

Yet their sensitivity graphs are not geometrically equivalent under these summaries.

### Function F111

One-set:

[
\{0000,0001,0010,0011,0101,0110\}.
]

Active sensitivity-graph component sizes:

[
\boxed{10,2,2}.
]

Maximum-matching size:

[
\boxed{6}.
]

Active-component diameters:

[
\boxed{6,1,1}.
]

Adjacency spectral radius:

[
\boxed{\sqrt 6\approx2.44949}.
]

### Function F393

One-set:

[
\{0000,0011,0111,1000\}.
]

Active sensitivity-graph component sizes:

[
\boxed{6,4,4}.
]

Maximum-matching size:

[
\boxed{4}.
]

Active-component diameters:

[
\boxed{4,2,2}.
]

Adjacency spectral radius:

[
\boxed{\sqrt 5\approx2.23607}.
]

### Proposition 4 — geometry separation

Essential-variable count, total sensitivity, maximum sensitivity, and the complete vertex sensitivity-degree histogram do not determine the connectivity, component-size distribution, matching number, diameter profile, or spectral radius of a Boolean function's sensitivity graph.

### Proof

The explicit pair F111/F393 has identical values for all four stated scalar/profile quantities but different values for each listed graph-geometric quantity. Therefore those summaries cannot determine the latter. \(\square\)

### Novelty boundary

The sensitivity graph itself is established in Boolean-function complexity, and its adjacency spectral norm is studied as spectral sensitivity. Proposition 4 therefore does **not** claim invention of the sensitivity graph or spectral sensitivity.

The research question is narrower:

> Do non-spectral geometric properties of (G_f), when combined with an explicit physical locality/noise model, predict physical resource requirements not captured by sensitivity, block sensitivity, spectral sensitivity, or standard query/circuit measures?

This is now an experimentally falsifiable question and provides the transition point from pure theory to exhaustive software search.


---

## 18. Stronger finite separation with matched spectral sensitivity

Exhaustive enumeration of all 65,536 four-variable Boolean functions yields a stronger controlled pair: F126 and F395.

Their one-sets are

[
F126^{-1}(1)=\{0001,0010,0011,0100,0101,0110\},
]

[
F395^{-1}(1)=\{0000,0001,0011,0111,1000\}.
]

They have identical:

- essential-variable count: 4;
- undirected sensitive-edge count: 12;
- maximum sensitivity: 3;
- complete sensitivity-degree histogram:
  [
  0^2,1^6,2^6,3^2;
  ]
- adjacency spectral radius:
  [
  \boxed{\rho(G_f)=2}.
  ]

Nevertheless,

[
F126:\quad
\text{active components}=(7,7),\;
\nu=6,\;
\text{diameters}=(4,4),
]

while

[
F395:\quad
\text{active components}=(9,5),\;
\nu=5,\;
\text{diameters}=(6,4).
]

Here (
u) is the maximum-matching number.

### Proposition 5 — spectral-matched residual-geometry separation

Essential-variable count, sensitive-edge count, maximum sensitivity, the full sensitivity-degree histogram, and sensitivity-graph spectral radius do not jointly determine sensitivity-graph component sizes, maximum-matching number, or diameter profile.

### Proof

F126 and F395 agree on every quantity in the premise and differ on every listed residual-geometric quantity. \(\square\)

The exhaustive (n=4) search finds four matched scalar+spectral classes with differing residual geometry, so the phenomenon is not unique to this witness.

### Research significance

This proposition is a graph-theoretic separation, not yet a physical-computation lower bound. Its role is to remove spectral radius as a sufficient explanation for all remaining sensitivity-graph geometry.

The next experiment must test whether two such spectrally matched functions have different resource requirements under the **same explicitly defined physical locality/noise model**. Only such a result could elevate residual geometry from descriptive structure to a physical-computation predictor.


---

## 19. First physical model and a negative result

Consider (n) input coordinates placed on sites of a one-dimensional line. Input coordinate (i) is assigned site (pi(i)), and a single readout occupies site (r).

For every sensitive edge ((x,i)inmathcal E_f), the perturbation caused by flipping coordinate (i) must propagate distance

[
d_i=|pi(i)-r|.
]

Under homogeneous contraction (eta), its surviving distinguishability is modeled as

[
Delta_i=\eta^{d_i}.
]

Reliable decoding requires

[
Delta_i\ge1-2\epsilon.
]

The implementation optimizes over all input permutations and readout sites.

### Negative result

For the spectrally matched witness pair F126/F395, this model does not expose the residual sensitivity-graph geometry.

The reason is structural. Its objective has the form

[
C(f)=
\sum_i w_i(f)c_i,
]

where

[
w_i(f)
=
|\{x:(x,i)\in\mathcal E_f\}|
]

is the number of sensitive edges in coordinate direction (i), while (c_i) depends only on the physical distance/noise assigned to coordinate (i).

Such a coordinate-separable model discards adjacency relations among different sensitive edges.

### Proposition 6 — coordinate-separable blindness

Any physical cost functional depending on a Boolean function only through the directional sensitive-edge counts (w_i(f)),

[
C(f)=F(w_1(f),\ldots,w_n(f)),
]

cannot distinguish two functions having the same directional sensitivity-count vector, regardless of differences in sensitivity-graph component structure, matching number, or diameter.

This follows immediately because all residual graph structure is absent from the arguments of (F).

### Consequence

To test whether residual sensitivity-graph geometry has physical meaning, the next model must be nonseparable across sensitivity edges. Candidate mechanisms include:

- state-dependent routing;
- shared finite-capacity transport channels;
- congestion between simultaneously protected transitions;
- common refresh resources;
- trajectory-dependent physical states.

This negative result narrows the model class required for the next experiment.


---

## 20. Shared-capacity falsification

A natural attempt to make sensitivity-graph geometry operational is to impose shared protection capacity: in one round, a physical state may participate in at most one protected sensitive transition.

This scheduling problem is exactly edge coloring of the sensitivity graph (G_f).

Every sensitivity graph is a subgraph of the Boolean hypercube. The hypercube is bipartite, and every subgraph of a bipartite graph is bipartite. Therefore, by König's line-coloring theorem,

[
\boxed{
\chi'(G_f)=\Delta(G_f)=s(f)
}.
]

Thus the minimum number of endpoint-conflict-free protection rounds is already determined by maximum sensitivity.

For the matched pair F126/F395,

[
s(F126)=s(F395)=3,
]

so both require exactly

[
\boxed{3}
]

such rounds.

Although their maximum matching numbers differ,

[
\nu(F126)=6,qquad \nu(F395)=5,
]

that difference does not induce different edge-coloring round complexity.

### Proposition 7 — endpoint-capacity collapse

For any Boolean function, a shared-capacity model whose only conflict rule is that two simultaneously serviced sensitive edges may not share a Boolean state has exact round complexity equal to maximum sensitivity.

Consequently this model cannot provide a physical invariant beyond (s(f)).

### Consequence

Residual sensitivity-graph geometry can become operational only if the physical constraints depend on more than endpoint conflict. Examples that remain logically possible include metric embedding cost, finite spatial wire length, state-dependent trajectories, component setup/reset cost, or nonlocal congestion in a physical substrate. Each must be justified independently; none is assumed to be novel.


---

## 21. Physical-layout audit

A direct embedding hypothesis was tested next.

### Fixed Boolean-hypercube embedding

If Boolean states retain their natural hypercube coordinates and each sensitivity edge is realized by its native cube edge, every sensitive edge has unit length. Hence total wire length is simply

[
L_{\rm cube}(f)=|E_f|.
]

For F126 and F395,

[
L_{\rm cube}(F126)=L_{\rm cube}(F395)=12.
]

Thus the natural hypercube embedding cannot expose their residual geometry through total edge length.

### Freely optimized one-dimensional embedding

If active Boolean states may instead be placed freely on a line and the objective is

[
L_{\rm line}(G_f)
=
\min_{\pi}
\sum_{(u,v)\in E_f}
|\pi(u)-\pi(v)|,
]

the resulting problem is the classical Minimum Linear Arrangement problem.

Therefore minimum wire length under unrestricted linear placement is not introduced here as a new complexity measure.

### Proposition 8 — layout baseline

Two immediate physical-layout constructions collapse to known quantities:

1. fixed natural hypercube wire length equals sensitive-edge count;
2. optimized one-dimensional total wire length is Minimum Linear Arrangement.

Consequently neither construction, by itself, supplies the missing new physical-computational invariant.

### Implication

A publishable new invariant must couple computational transition geometry to a physical constraint not already exhausted by standard graph layout. Candidate constraints must be motivated by the computation itself, for example simultaneous requirements on layout, noisy distinguishability, refresh, and reusable architecture. Merely renaming graph-layout cost as physical complexity is excluded.


---

## 22. Summary-mediated model blindness

Let (mathcal F_n) be a family of Boolean functions and let

[
S:mathcal F_n	oSigma
]

be a summary map. A physical-cost model (C) is **(S)-mediated** if there exists a map (Phi) such that

[
C(f)=Phi(S(f))
]

for every (finmathcal F_n).

The summary may contain several quantities simultaneously, for example essential-variable count, sensitive-edge count, maximum sensitivity, directional sensitivity counts, degree histogram, or spectral radius.

### Theorem 9 — Summary-Mediated Blindness

If (C) is (S)-mediated and

[
S(f)=S(g),
]

then

[
oxed{C(f)=C(g)}.
]

Consequently, if a target physical phenomenon (T) separates (f) and (g),

[
T(f)
e T(g),
]

then no (S)-mediated model can represent (T) exactly on the whole function family.

### Proof

By (S)-mediation,

[
C(f)=Phi(S(f)).
]

If (S(f)=S(g)), substitution gives

[
C(f)=Phi(S(f))
=Phi(S(g))
=C(g).
]

The second statement follows by contradiction. \(square\)

### Important novelty boundary

The abstract theorem is a factorization observation and is not claimed as a deep standalone mathematical theorem. Its scientific value comes only from:

1. choosing a physically meaningful summary class;
2. proving that broad physical model families factor through that summary;
3. constructing matched Boolean witnesses;
4. identifying a physically justified target phenomenon that does not factor through the summary.

Without items 2–4, the theorem is only a formal bookkeeping statement.

---

## 23. Concrete blindness hierarchy

The previous propositions instantiate Theorem 9.

### Coordinate-separable transport

If

[
C(f)=F(w_1(f),ldots,w_n(f)),
]

then (S(f)=(w_1,ldots,w_n)). Residual adjacency among sensitivity edges is invisible.

### Endpoint-conflict protection

For endpoint-exclusive servicing of sensitive transitions,

[
C(f)=chi'(G_f)=Delta(G_f)=s(f),
]

because (G_f) is bipartite. Thus (S(f)=s(f)).

### Native hypercube wire length

[
C(f)=|E_f|,
]

so (S(f)=|E_f|).

### Spectral summaries

Any proposed cost of the form

[
C(f)=Phi(operatorname{ess}(f),|E_f|,s(f),H_{deg}(f),ho(G_f))
]

must assign equal cost to F126 and F395, because they agree on every argument.

Yet their residual graph structures differ:

[
(7,7),,
u=6,,D=(4,4)
]

versus

[
(9,5),,
u=5,,D=(6,4).
]

This proves incompleteness of that summary for reconstructing those graph properties. It does **not** yet prove that any real physical cost differs between F126 and F395.

---

## 24. Criterion for the central paper theorem

A central theorem suitable for the eventual paper must go beyond Summary-Mediated Blindness.

It should establish a physically motivated model class (mathcal M) and a resource (R_{mathcal M}) such that:

[
S(F126)=S(F395)
]

but

[
oxed{
R_{mathcal M}(F126)
e R_{mathcal M}(F395)
}.
]

Preferably the result should extend to an infinite family rather than a single four-variable witness.

The strongest desired form is

[
S(f_k)=S(g_k)
quad	ext{while}quad
rac{R_{mathcal M}(f_k)}
{R_{mathcal M}(g_k)}
	oinfty
]

or another asymptotically nontrivial separation.

This is the threshold for moving from a strong framework/no-go study to a substantially stronger complexity-theoretic contribution.


---

## 25. Corrected conventional-complexity controls

A subsequent exhaustive audit identified an error in the earlier reported conventional profiles for F126/F395. The incorrect Proposition 10 is withdrawn.

The corrected exact values are:

\[
F126:\quad bs=3,\;\deg_{\mathrm{ANF}}=3,\;D=4,\;C=3,\;\{C_0,C_1\}=\{3,3\},
\]

\[
F395:\quad bs=3,\;\deg_{\mathrm{ANF}}=4,\;D=4,\;C=3,\;\{C_0,C_1\}=\{2,3\}.
\]

Thus F126/F395 remains a valid scalar+spectral sensitivity-geometry separation, but it is **not** matched on algebraic degree or the one-sided certificate profile.

### Exhaustive strengthened-summary audit at n=4

All 65,536 four-variable Boolean functions were grouped by

\[
S^*(f)=
(\operatorname{ess},|E|,s,H_{\deg},\rho,bs,\deg_{\mathrm{ANF}},D,C,\{C_0,C_1\}).
\]

The enumeration produced 220 distinct (S^*)-classes. For the residual geometry tuple

\[
G^*(f)=(\text{active component sizes},\nu,\text{active diameter profile}),
\]

no (S^*)-class contained more than one (G^*)-value.

Therefore:

\[
\boxed{
S^*(f)=S^*(g)\Longrightarrow G^*(f)=G^*(g)
\quad\text{for all four-variable Boolean functions.}
}
\]

This is a finite exhaustive fact for (n=4), not a theorem for arbitrary (n).

### Consequence

The strengthened matched-witness search must move beyond (n=4). Exhaustive enumeration of all five-variable Boolean functions would require (2^{32}) truth tables, so the next phase uses targeted/symmetry-aware search rather than full enumeration.

Scientific correction is part of the reproducibility record; the withdrawn claim must not be used in later novelty statements.


## 26. Sparse truth-set cut identities

Let \(S=f^{-1}(1)\subseteq Q_n\), and let \(G_f=\delta(S)\) be the sensitivity graph.  Write \(E_i(S)\) for internal edges of the induced subgraph \(Q_n[S]\) in coordinate direction \(i\), and \(E(S)=\sum_i E_i(S)\).

Every vertex of \(Q_n\) has one incident edge in each coordinate direction. Counting incidences from vertices of \(S\) gives the exact identities

\[
w_i(f)=|S|-2|E_i(S)|,
\]

and therefore

\[
|E(G_f)|=n|S|-2|E(S)|.
\]

Thus, once the truth-set cardinality \(|S|=k\) is fixed, the directional sensitivity profile determines the multiset of directional internal-edge counts of \(Q_n[S]\), while total sensitivity determines the total number of internal edges.  These identities explain part of the rigidity seen in sparse-layer searches, but they do **not** by themselves determine the isomorphism type of \(Q_n[S]\), the cut-component structure, matching number, diameter profile, or the other strengthened complexity measures.

### Exact finite checkpoint

For \(n=5\) and \(|S|=4\), exhaustive enumeration of all \(\binom{32}{4}=35{,}960\) truth sets produced 625 classes after output-complement and input-variable permutation canonicalization and 31 cheap strengthened-summary buckets. No residual-geometry separation survived the full refinement controls. This is an exhaustive statement for this layer only; it is not a theorem for all five-variable Boolean functions.


### Directional-profile equivalence lemma

For fixed \(n\) and fixed truth-set cardinality \(k=|S|\), define \(a_i(S)=|E_i(S)|\), the number of internal truth-set edges in coordinate direction \(i\). Then

\[
w_i(f)=k-2a_i(S)
\quad\Longleftrightarrow\quad
 a_i(S)=\frac{k-w_i(f)}{2}.
\]

Hence the labeled vectors \((w_1,\ldots,w_n)\) and \((a_1,\ldots,a_n)\) determine each other exactly. After quotienting by input-variable permutations, their sorted multisets also determine each other. Consequently, within a fixed sparse layer, directional sensitivity is not an independent source of information from directional internal adjacency; it is an equivalent coordinate-wise encoding of it.

**Corollary.** The parity constraints \(w_i\equiv k\pmod 2\) and bounds \(0\le w_i\le k\) are necessary for every directional profile in the \(k\)-th truth-set layer.

This lemma is an exact structural simplification, not the central determination theorem: identical directional internal-edge counts need not determine the induced truth-set graph or the residual geometry of the sensitivity cut.
