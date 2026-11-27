# Streamlined proof revision

**Date:** 27 November 2026.
**Input:** the user-supplied `abelian_comparison_streamlined.tex` and the
accompanying Claude/Gemini proposals. The supplied source's SHA-256 was
`4e9f92ec8f85bc5736cbe877670e576d19ab12a9f78ab0708abf1619e628603e`.
The attachment itself was not overwritten. The revised sources are in
`papers/`; they have separate final source reviews and build hashes.

## Outcome

The core Rosati/singular-value argument is valid. The revised main note
uses a quotient of a finite sum of regular modules to produce the
compatible Hermitian form, then derives the sharp norm sandwich from
Riemann–Roch. The elementary companion gives a separate proof under a
lighter prerequisite budget and reaches actual limits by bounded-window
trace detection. The main note is four pages and the companion three.

Both are expository proofs of established results with explicit
quantitative consequences. Their algebraic inputs, finite checks, and
AI-assisted source reviews do not constitute a formal verification or an
independent human referee report.

## Corrections and qualifications

| Supplied assertion | Audited resolution |
| --- | --- |
| An all-iterate upper bound `C n^(m-1) rho^n` for every endomorphism. | False when `rho=0` and the action is nonzero nilpotent. For `f(x,y)=(y,0)` on product-polarized `E^2`, `delta_1(f)=1/2` but `chi_2=0`. State the polynomial estimate for positive radius, and use exact vanishing/nilpotency equivalence for zero radius. |
| Polarized semisimplicity and “the same” root modulus on every cohomological degree. | The modulus is `d^(i/2)` on `H^i`; it is `sqrt(d)` only in degree one. |
| Log-concavity and `delta_0=1` imply initial-segment support. | Log-concavity alone permits internal zeros, e.g. `(1,0,0,1)`. Apply it to `u*H + epsilon H` and pass to the limit, proving positivity at all indices preceding a positive term. |
| The numerical quotient is well defined over `Q_l`. | Explicitly pair a cohomological relation with representatives of a dual numerical basis. This proves the assertion without identifying numerical and homological equivalence. |
| The proposed growth results are stronger new theorems. | Hu's Corollary 5.6 already gives uniform cohomological/numerical norm comparison. The maximum peripheral Jordan-size and nilpotency-index equalities follow from that published theorem. They do not identify the full Jordan forms. |
| Exact leading asymptotics at a strict gap are a new strengthening of the literature. | The abelian argument is valid, but Hu's October 2026 Theorem 1.5 already proves a broader result with the same remainder threshold. |
| Weyl's inequality is required for the finite spectral bound. | The proof only needs `rho(T) <= ||T||` and the exterior-power norm formula. |
| The precise finite power-sum pole lemma should be credited to Deligne as its originator. | Deligne's trace/log-determinant identity is related. The exact priority assertion is not supported by the inspected passages; use “classical power-sum/radius-of-convergence argument.” |

## Verified improvements to the supplied presentations

### One compatible form, without decomposing the algebra

Riemann–Roch gives the identity

\[
M_u(s)^2=\det(s+u^\dagger u).
\]

Its next-to-leading coefficient identifies the Tate trace form with the
geometrically positive quadratic form `2g Q_H`. Rationality of the Gram
matrix upgrades rational positivity to real positive definiteness. On the
complexified endomorphism algebra, `Tr(a* b)` therefore makes left
multiplication a star representation. A module surjection `E^m -> V`
has an invariant orthogonal complement to its kernel, which supplies the
desired form on `V`. No radical argument, classification, or simple-module
decomposition is needed. This is a classical positive-involution principle;
Milne's Proposition 8.10 is the precise reference.

### A sharp composition bound

Writing `B_k=binom(g,k)`, the proposed `B_k^2` factor improves to

\[
\delta_k(uv)\le B_k\delta_k(u)\delta_k(v).
\]

Exterior-norm submultiplicativity gives log-majorization of the paired
squared singular values of the product. Convexity of
`e_k(exp(x_1),...,exp(x_g))` gives the elementary-symmetric inequality.
Rational perturbation by scalar identity maps handles singular maps.
The same rank-`k` scalar projection in each factor attains equality.
The maps need not commute.

### The strict-gap coefficient is explicit

If `r_(2k)>r_(2k+1)` and `lambda=chi_(2k)>0`, let `Pi_k` be the spectral
projection at the unique dominant eigenvalue of `wedge^(2k)f`. Then

\[
\delta_k(f^n)=\frac{\|\Pi_k\|}{B_k}\lambda^n+O(\eta^n),
\qquad \lambda r_{2k+1}/r_{2k}<\eta<\lambda.
\]

The norm refers to the fixed Hermitian form from the note. Its leading
constant is at least `1/B_k`, and diagonal examples attain that value.
This is a precise coefficient formula within the known strict-gap regime.
Without a gap, a normalized leading coefficient need not converge: the
involution `[[1,1],[0,-1]]` on `E^2` has `delta_1(f^n)` alternating between
`3/2` and `1`, while the spectral radius and polynomial exponent are both
constant. The two-sided growth statement remains valid.

### Bounded windows turn the elementary limsup into a limit

For a fixed matrix with positive radius and distinct nonzero eigenvalues
`beta_j`, invert the finite matrix `(beta_j^r)` to obtain

\[
\max_{0\le r<d}|\operatorname{Tr}(T^{n+r})|\ge c_T\rho(T)^n.
\]

The pointwise exterior-trace bound from polynomial interpolation and
Khovanskii–Teissier supplies an upper bound by the corresponding degrees.
Ample nef dominance `(f^r)*H <= B_r H` bounds these finitely many future
degrees by `B_r^k delta_k(f^n)`. This gives a lower bound for **every**
iterate. Combined with the cohomological matrix-coefficient upper bound,
it proves the actual limit without retaining the moving-scale gap/block
argument. Zero radius gives eventual vanishing directly.

For `k=1`, the quadratic trace inequality replaces polynomial interpolation
and Khovanskii–Teissier, and the same window argument proves the actual
unpolarized first-degree limit.

### Curve RH at one critical scale

In the polarized case the nef majorant is
`P_(f^n)(t) <= 2^g (t^2+d^n)^g`. Set `t_n=2d^(n/2)` directly. The
factor 2 prevents cancellation at the boundary modulus; the nth-root
limit of each absolute factor is `max(sqrt(d),|alpha|)`. The majorant
and determinant force the spectral circle. No trace lemma, logarithmic
scale selection, separate pairing lemma, or Khovanskii–Teissier is needed.

## Literature and verification records

- [Targeted literature audit](literature_audit.md), including Hu's
  Corollaries 1.7 and 5.6, Milne's Proposition 8.10, and the September and
  October 2026 preprints.
- [Rosati proposal audit](rosati_audit.md) and
  [elementary proposal audit](elementary_audit.md), with detailed derivations.
- Final source reviews: [main note](main_source_review.md) and
  [elementary companion](elementary_source_review.md), tied to source hashes.
- [Exact regression guide](exact_checks.md) and
  [recorded output](exact_checks.json), testing new constants and edge cases.
- [PDF visual review](pdf_visual_review.md), covering the seven new pages.
- [Build manifest](../build_manifest.json), containing all source/PDF hashes.

The old source notes and their historical audits are retained. The
streamlined notes are the recommended presentations. Remote CI status
belongs to the actual revision PR; configured automation is not by itself
evidence of a completed run.
