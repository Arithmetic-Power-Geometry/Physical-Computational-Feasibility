# Assumptions and Model Boundaries

The project deliberately states model assumptions explicitly because apparent physical-computation advantages often disappear when encoding, nonlocality, precision or readout assumptions are exposed.

## Dependency model

The bound

\[
\operatorname{ess}(f)\le meq^d
\]

assumes a layered dependency graph in which:

- each initial encoded component depends on at most \(e\) original inputs;
- each update has fan-in at most \(q\);
- there are \(d\) dependency layers;
- the final decision accesses at most \(m\) terminal components.

It does not automatically apply to:

- unbounded-fan-in primitives;
- instance-specific global encoders;
- nonlocal measurements with hidden preparation cost;
- analog encodings whose dependency structure is not modeled by these assumptions.

Those cases require explicit resource accounting rather than being declared counterexamples.

## Precision model

The bound

\[
Np\ge n
\]

means that \(N\) degrees of freedom, each with at most \(2^p\) reliably distinguishable levels, cannot losslessly encode more than \(Np\) arbitrary classical bits.

It is not a lower bound on the communication required to output a one-bit function.

## Noise model

The total-variation requirement

\[
D_{\mathrm{TV}}(P,Q)\ge1-2\epsilon
\]

is a binary discrimination requirement for worst-case error \(\epsilon\) on a function-changing pair.

Future software will additionally support other metrics, but no metric substitution will be treated as innocuous without proving the associated decision bound.

## Fair-comparison rule

A comparison is invalid if one architecture receives any of the following for free while another must compute or construct it:

- precomputed labels;
- a problem-specific physical wiring;
- a global interaction;
- exponentially precise parameters;
- a prepared entangled/resource state;
- nonuniform advice;
- oracle access;
- postselection without success-probability cost.

## Physical interpretation

The framework is substrate-agnostic. It may be instantiated for digital, analog, stochastic, neuromorphic, quantum, mechanical or other physical systems, but claims apply only under the assumptions verified for that substrate.
