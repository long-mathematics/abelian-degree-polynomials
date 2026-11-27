# Exact normalization checks

The accompanying script performs deterministic exact calculations in the model
of an integer matrix acting on a power of an elliptic curve with the product
polarization. It is a set of **sanity checks for formulas and normalizations**,
not a verification of the geometric proofs.

## Reproduce

Use Python 3 with **SymPy 1.14.0**. From the repository root, run:

```bash
python3 scripts/check_identities.py --report audit/exact_checks.json
```

The script checks the SymPy version, raises `AssertionError` on a failed identity
or inequality, prints a concise JSON report, and optionally writes exactly that
report to the requested path. The committed JSON is actual execution output.
There are no random seeds, timestamps, numerical root approximations, or
floating-point comparisons.

## Model and normalization

For an integer matrix \(M\) representing an endomorphism of \(E^g\), the action on
degree-one cohomology contains two copies of the matrix representation. Thus

\[
P_M(t)=\det(tI-M)^2,
\qquad \operatorname{Tr}_{H^1}(M)=2\operatorname{tr}(M).
\]

With the product polarization, put \(G=M^{\mathsf T}M\). The normalized mixed
intersection numbers are

\[
\delta_j(M)=\frac{e_j(G)}{\binom gj},
\qquad
\delta_0=1,\quad
\delta_1=\frac{\operatorname{tr}(G)}{g},\quad
\delta_g=\det(M)^2.
\]

The script computes \(e_j(G)\) by sums of principal minors. It independently
compares their mixed polynomial with the characteristic-polynomial expression
for \(\det(t^2I+G)\).

## Coverage

The deterministic matrix families cover dimensions 1 through 4 and include zero
and singular matrices, signed diagonals, strict diagonal gaps, nonnormal Jordan
matrices, nilpotent shifts, rank-one matrices, dense matrices, cyclic
permutations, rotation blocks, and repeated-modulus blocks. Duplicate matrices
are merged. Each distinct matrix is tested at iterate exponents 1 and 2.

For each iterate, the script checks the trace coefficient, both mixed-degree
endpoints, iteration of the top degree, the first mixed-degree normalization,
the trace inequality, and Khovanskii--Teissier log-concavity. At each of seven
rational shifts of both signs, including zero, it checks

\[
P_M(t)=\det\big((tI-M)^{\mathsf T}(tI-M)\big)\ge0,
\qquad
P_M(t)\le 2^g\det(t^2I+G),
\]

as well as the exact Gram-matrix identity underlying the latter bound:

\[
2(t^2I+G)-(tI-M)^{\mathsf T}(tI-M)
=(tI+M)^{\mathsf T}(tI+M).
\]

For \(J=\begin{pmatrix}2&1\\0&2\end{pmatrix}\), it checks directly for
\(1\le n\le8\) that

\[
\delta_1(J^n)=4^n\left(1+\frac{n^2}{8}\right).
\]

Four pairs of **noncommuting** integral similitudes, formed from scaled signed
permutations, test the two-map bounds. If \(U^{\mathsf T}U=r^2I\) and
\(V^{\mathsf T}V=s^2I\), the script checks

\[
(r-s)^2I\preceq(U-V)^{\mathsf T}(U-V)\preceq(r+s)^2I
\]

by exact nonnegativity of all principal minors of each difference, and checks
the corresponding degree bounds. A generic symbolic 2-by-2 matrix also checks
the sum-of-squares normalization of the trace defect.

## Limits

These finite examples can expose sign, factor-of-two, binomial-normalization,
and iterate-exponent mistakes. They cannot establish the degree identity for
arbitrary abelian varieties, the geometric intersection theorems, the
all-iterate limiting arguments, historical novelty, or the correctness of an
entire manuscript. Those claims must be assessed from the written proofs and
their cited foundations. A passing JSON report is not a proof certificate.
