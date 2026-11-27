# Final source review: finite-time spectral comparison

Date: 27 November 2026.

Reviewed source: papers/abelian_comparison_streamlined.tex

SHA-256:

    5885dd36856eb576450cad2abf5c7f070e1a194c0feef4d7f4b72b16f6bfe008

The source was read in full, including the final degree-zero convention and zero-factor wording. The subsequent explicit index range in Theorem 2 was checked: reversing that sole clause reproduces the previously reviewed hash 7119dbdba467ab50b78b945537cffbe6fe72c8de5b49b4b6c22e1255bdfeaf65 exactly. The hash above identifies the clarified final source. This review made no source edits and did not repeat the literature search, builds, or tests.

## Verdict

**No material mathematical error or circularity was identified. No required correction remains from this review.** The revised statement separates positive spectral radius from nilpotence, limits the Jordan comparison to maximal peripheral block sizes, and states the correct degree-dependent polarized root moduli.

## Points checked

1. **Positivity before the Hermitian construction.** Riemann–Roch and the degree–determinant identity give \(M_u(s)^2=\det(s+u^\dagger u)\) without assuming Rosati positivity. Coefficient comparison gives \(\operatorname{Tr}(u^\dagger u)=2gQ_H(u)\). Effective pullback divisors prove strict positivity for nonzero rational endomorphisms; the rational Gram matrix justifies positive definiteness over the reals. Trace invariance under Rosati and cyclicity make the complexified form Hermitian. The kernel of the free-module surjection and its orthogonal complement are algebra-stable because the action includes adjoints. The transported form is therefore valid without classification or prior semisimplicity.

2. **Identity and sharp sandwich.** The determinant normalization, including quasi-endomorphisms, is correct. Its monic square root pairs the squared singular values, including zeros. The factor \(\binom gk\), the sharpness example, and the opposite sandwich inequality are correct. The endpoints and the zero endomorphism respect the exterior-power conventions.

3. **Numerical quotient and Jordan comparison.** Pairing a cohomological relation with a dual rational numerical basis justifies the quotient after coefficient extension. Numerical and homological equivalence are not assumed equal. The matrix-coefficient and subquotient arguments establish both spectral inequalities and both directions of the maximal peripheral Jordan-size comparison. The exact odd exterior-norm identity gives the odd-degree formula through Gelfand's formula.

4. **Zero radius.** The polynomial growth estimate is explicitly restricted to positive radius. The three zero conditions in (7) are equivalent at every iterate, proving equality of nilpotency indices. The stated \(E_0^2\) example correctly explains the former zero-radius error.

5. **Strict-gap constant and remainder.** The top exterior eigenvalue is algebraically simple. Reality and positivity of the degree sequence, together with the lower norm bound, force this unique dominant eigenvalue and its leading coefficient to be positive. Every other exterior eigenvalue has modulus at most \(\lambda r_{2k+1}/r_{2k}\); Jordan factors are absorbed by any larger \(\eta<\lambda\). The ordinary matrix-coefficient expansion supplies that remainder. The singular-value gap and norm limit then identify the coefficient as \(\|\Pi_k\|/\binom gk\). This also covers a zero next root modulus, when the remaining part is eventually nilpotent.

6. **Sharp composition.** For isogenies, exterior norms give partial-product inequalities and determinant multiplicativity gives equality of the total product. Ordinary majorization applies to the symmetric convex exponential elementary-symmetric function. The following product bound yields exactly \(\binom gk\). Rational scalar perturbation and homogeneous extension to quasi-endomorphisms handle singular maps; the common rank-\(k\) projection attains the constant.

7. **Final extensions.** The nef-annulus quadratic inequalities extend to the complexified endomorphism algebra and finite direct sums, then restrict to the invariant orthogonal complement. They therefore control singular values in the same form on \(V\). The two-map inequalities, including zero factors, yield (10) with the correct exponents and no commutation assumption. The polarized conclusion correctly gives semisimplicity and modulus \(d^{i/2}\) on \(H^i\).

This is a mathematical source review of the identified version, not a formal proof verification or a new priority assessment.
