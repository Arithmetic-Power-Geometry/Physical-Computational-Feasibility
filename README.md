# Physical Computational Feasibility

A theory-first research repository for studying **problem-specific physical resource limits of computation** under explicit constraints on encoding, interaction locality, depth/time, readout, noise, precision, and physical information capacity.

The project does **not** assume that a shorter logical circuit, a compact analog representation, a global physical response, or a self-organizing substrate provides a computational advantage by itself. The central requirement is that all resources capable of carrying hidden computation are accounted for.

## Research program

The repository follows this order:

1. **Theory** — definitions, propositions, lower bounds, counterexamples, and open conjectures.
2. **Software** — exact and numerical implementations of the theoretical quantities.
3. **Tests and comparisons** — parity, majority, dictator, threshold and other Boolean-function families under multiple resource models.
4. **Workflow** — reproducible GitHub Actions execution.
5. **Artifacts** — machine-generated CSV/JSON/figures/tables produced by the workflow.

The repository is an independent theory-and-software research package. Papers may use and scientifically interpret verified results and artifacts produced by the research workflow.

## Core object

For a problem family \(P\), define a resource vector

\[
\mathbf R=(N,p,e,q,d,m,t,\sigma,A,E,\ldots),
\]

where components may include physical state count \(N\), reliable precision \(p\), encoder dependency \(e\), interaction order \(q\), depth \(d\), readout locality \(m\), physical time \(t\), noise scale \(\sigma\), dynamic range \(A\), energy \(E\), and other explicitly modeled resources.

The **physical computational feasibility region** is

\[
\mathfrak F_P
=
\{\mathbf R:\; P \text{ is computable to the required accuracy under } \mathbf R\}.
\]

The scientific target is not a single arbitrary scalar score. It is the boundary \(\partial\mathfrak F_P\), which describes which resources can substitute for one another and which cannot.

## First exact bound: dependency reach

Let \(f:\{0,1\}^n\to\{0,1\}\). Let \(\operatorname{ess}(f)\) be the number of essential input variables.

If:

- each encoded component initially depends on at most \(e\) input variables;
- every computational primitive combines at most \(q\) previous components;
- the architecture has depth \(d\);
- final readout jointly accesses at most \(m\) resulting components;

then

\[
\operatorname{ess}(f)\le m e q^d.
\]

Therefore any such architecture computing \(f\) exactly must satisfy

\[
\boxed{m e q^d\ge \operatorname{ess}(f)}.
\]

For parity \(P_n=x_1\oplus\cdots\oplus x_n\),

\[
\operatorname{ess}(P_n)=n,
\]

so

\[
\boxed{m e q^d\ge n}.
\]

This is a dependency/light-cone lower bound, not claimed as a new foundational theorem.

## Noise-aware requirement

For a physical output \(Y\), define for each essential Boolean-cube edge

\[
\Delta_i(x)
=
D_{\mathrm{TV}}\!\left(P_{Y|x},P_{Y|x\oplus e_i}\right).
\]

If \(f(x)\ne f(x\oplus e_i)\), then reliable binary decoding with worst-case error at most \(\epsilon<1/2\) requires

\[
\Delta_i(x)\ge 1-2\epsilon.
\]

Define

\[
\Delta_{\min}(f)
=
\min_{x,i:\, f(x)\ne f(x\oplus e_i)}
\Delta_i(x).
\]

A necessary reliability condition is

\[
\boxed{\Delta_{\min}(f)\ge 1-2\epsilon}.
\]

This separates **dependency reach** from **surviving physical distinguishability**.

## Precision is not dependency

A device may attempt to compress many logical states into few analog variables. If \(N\) physical variables each support at most \(p\) reliable bits, lossless representation of \(n\) arbitrary bits requires the capacity condition

\[
Np\ge n.
\]

However, this does not imply that a one-bit output such as parity requires \(n\) bits of output-channel capacity. Parity is difficult because every input variable is essential, not because the output contains \(n\) bits. The theory therefore keeps **information volume**, **dependency reach**, and **physical distinguishability** separate.

## Computational displacement

A claimed computational advantage is rejected if the missing difficulty is simply displaced into any uncounted stage, including:

- instance encoding;
- initial-condition preparation;
- nonlocal or high-order interactions;
- precision/dynamic range;
- time or propagation distance;
- training/adaptation;
- postselection/success probability;
- measurement/readout;
- verification;
- energy or entropy export;
- bespoke instance-specific hardware.

See [THEORY.md](THEORY.md) and [NOVELTY_AUDIT.md](NOVELTY_AUDIT.md).

## Current scientific status

The repository now contains an exact Boolean sensitivity-geometry separation theorem. In the complete five-variable layer with five positive inputs, an explicit pair matches a strengthened collection of Boolean complexity controls and has exactly adjacency-cospectral active sensitivity graphs, yet has different active component-size and diameter profiles. A parity-product construction lifts the separation to every essential dimension N >= 5.

The result is a theorem about what these summaries and spectra do not determine. It does not establish a hardware speedup, a new computational model, or a new physical law.

## License

Apache License 2.0.

Copyright © 2026 Mohammad Amir Khusru Akhtar.
