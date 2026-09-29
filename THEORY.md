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
