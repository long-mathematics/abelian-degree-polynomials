# Mathematical and publication audit

**Date:** 27 November 2026.  
**Scope:** the two sources in `papers/`, their compiled PDFs, attribution,
and reproducible exact checks.

## Verdict

No fatal mathematical gap, false stated conclusion, or circular use of
finite-field RH or dynamical comparison was identified. Both notes are
appropriate as expository alternative proofs of established results, subject
to their explicit standard prerequisites.

This verdict is based on independent AI-assisted mathematical readings and
targeted primary-source inspection. It is not external peer review, formal
verification, a new-theorem claim, or an exhaustive priority certification.

## Findings and corrections adopted

| Finding | Resolution in the revised sources |
| --- | --- |
| The curve proof's positivity and power-sum ending are classical. | Scope paragraph now cites Milne's exact historical locators; the recent proof is described as motivation. |
| The polarized map must be a group endomorphism. | Explicit `f in End(A)` hypotheses; numerical divisor classes and geometric cohomology specified. |
| Frobenius conventions could cause reciprocal-root confusion. | The curve application specifies the q-power Frobenius endomorphism after geometric base change and an Fq-defined symmetric ample line bundle. |
| A regular-algebra trace must not be confused with the Tate trace. | The Rosati formula explicitly uses the trace on the Tate module. |
| The semisimplicity transfer needs an algebraic justification. | The rational squarefree minimal polynomial is named, applied to the identity, and extended to Q_l. |
| Additional curve/cohomology prerequisites were implicit. | Jacobian identification, exterior algebra, rationality, and trace formula are now stated. |
| The all-degree note used an unnamed base field and omitted its zero-degree convention. | The field is named K; non-isogenies have degree zero; the rational identity is valid even when the characteristic divides the denominator. |
| The odd-degree formula was already explicit in Hu. | Hu, Remark 5.5 is credited next to Theorem 1. |
| The comparison is known more generally. | Xie's surjective-endomorphism theorem is acknowledged. |
| Scaling and concavity have close methodological precedents. | Xie Section 2.5 and Hu–Truong–Xie Lemma 2.2/proof of Theorem 1.5 are credited. |
| The quantitative byproduct is weaker than very recent work. | Hu–Jiang's September 2026 degree-growth theorem is explicitly compared. |
| Nef-order and two-map hypotheses were implicit. | `D <= E` in nef order and `u,v in End(A)` are defined. |

## Mathematical points checked

### Curve note

1. The rational shifted-pullback identity follows from the theorem of the
   cube; rational shifts, rather than only integer shifts, justify the
   discriminant argument.
2. The coefficient of degree `2g-1` is exactly minus the Tate trace, giving
   the constant `4g^2`.
3. Positive multiplicities prevent cancellation of the genuine poles in the
   power-sum generating function. Jordan blocks do not affect the trace.
4. The determinant/product argument upgrades all upper bounds to equalities.
5. The real quadratic form is positive definite: rationality of its Gram
   matrix rules out an irrational nullspace missed by rational vectors.
6. A squarefree rational minimal polynomial transfers to every Tate module.
   No comparison of regular- and Tate-representation multiplicities is used.
7. Exterior powers, the nef annulus, and the pure unipotent sheaf example
   are valid in the stated scopes. The last concerns arithmetic, not
   geometric, semisimplicity.

### All-codimension note

1. Rational nonnegativity of the degree polynomial extends to all real
   arguments and gives even multiplicity of real roots.
2. The parallelogram majorant has the correct `2^g` factor and all mixed terms.
3. Matrix-coefficient upper bounds allow arbitrary Jordan blocks; polynomial
   terms at subdominant moduli are absorbed by the exponential gap.
4. The scale `t_n=2R^n` gives the stated determinant limit and an eventual
   pointwise lower bound, not merely a limsup or a subsequence.
5. Khovanskii–Teissier fills repeated-modulus blocks in the correct direction.
   Its use can be reduced to surface Hodge index in arbitrary characteristic.
6. Numerical cycle classes are an equivariant quotient of algebraic
   cohomology. No injection or equality of homological/numerical equivalence
   is assumed, and Standard Conjecture D is not needed.
7. The non-surjective extension treats the eventually nilpotent part before
   interpolating the positive block.
8. The two-map inequality does not require commutation, including equal
   polarization factors and the zero-factor boundary cases.

## Verification records

- [Initial curve audit](audit/curve_proof_audit.md) and
  [initial all-codimension audit](audit/all_codimensions_audit.md) retain the
  hashes of the pre-revision texts they inspected. Their proposed edits are
  resolved by the table above.
- [Final source review](audit/final_source_review.md) identifies the revised
  sources by SHA-256.
- [Exact-check guide](audit/exact_checks.md) and
  [recorded JSON](audit/exact_checks.json): 4,399 exact assertions passed.
  These finite checks test normalizations and examples, not general proofs.
- [Build manifest](audit/build_manifest.json): local pdfLaTeX compilation,
  resolved cross-references, source hashes, and PDF hashes.
- [PDF visual review](audit/pdf_visual_review.md): direct inspection of all
  seven rendered pages, with no clipping, overlaps, or missing glyphs found.
- [Literature review](LITERATURE.md): primary-source versions and precise
  theorem/method overlap, checked through the audit date.

The PDFs were visually reviewed after compilation. No claim of remote CI
success is made until a GitHub Actions run actually completes.

## Unresolved matters

- Whether the exact degree-polynomial implementation already appears in
  an uninspected source remains open. The repository claims no priority.
- The notes do not improve the full arbitrary-sheaf Weil II argument.
- The quantitative bound is intentionally a short-proof byproduct and is
  not optimal relative to current literature.
