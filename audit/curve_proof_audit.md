# Adversarial audit: short curve RH proof

Date: 27 November 2026.

Audited file: `pre-revision/short_curve_rh_proof.tex`.

SHA-256 of the audited source: `f0b25d0ac089fa05384e8cd1d9bbd6b26a52f9712b158bb4cb354a462a04f43f`.

## Verdict

**No fatal mathematical gap found.** I re-derived the trace inequality, both spectral endings, the semisimplicity transfer, and the annulus assertion independently from the stated standard facts. The unipotent sheaf counterexample is valid. The argument applies in arbitrary characteristic to polarized endomorphisms of abelian varieties and gives curve/function-field RH through the Jacobian.

**The curve note should be published as exposition of classical Weil/Rosati positivity, with a concise alternative presentation.** Its trace inequality is precisely the classical Rosati Cauchy--Schwarz inequality in intersection notation. Its power-sum extraction also predates the November 2026 paper: Milne's 2015 exposition already gives essentially the same rational-function proof in footnote 1 on printed page 2. The new paper can explain why the argument was revisited, but should not be credited with originating this extraction step.

No new theorem, first elementary proof, or historically shortest proof is established here. The note's existing explicit disclaimer of priority is appropriate. The useful contribution is a compact arrangement that avoids writing down the Rosati involution and avoids classifying the endomorphism algebra.

## Recommended changes before public release

These are clarification and attribution changes, not repairs to a failed proof.

1. **Specify the endomorphism hypothesis.** In the polarized-circle theorem and the annulus paragraph, explicitly write `f in End(A)`. Otherwise a reader could interpret `f` as an arbitrary self-morphism, while the action on the Tate module and left multiplication on the endomorphism algebra require an origin-preserving homomorphism. General self-morphisms can be treated separately by removing their translation part.
2. **Specify numerical classes and geometric cohomology.** State that all divisor-class equalities and nef inequalities are numerical, and that the cohomology used in the curve application is geometric etale cohomology. The proofs work with numerical equality, so this clarifies rather than strengthens the assumptions.
3. **Make historical attribution explicit.** Replace the opening emphasis on the recent paper's power-sum extraction by a reference to the classical extraction, for example Milne 2015, printed page 2, footnote 1, also used in the recent paper. Cite Milne's Hasse discussion on page 3 and Rosati positivity on pages 21--22 as close predecessors.
4. **Specify the Frobenius convention.** Use the `q-power Frobenius endomorphism pi` on a Jacobian defined over F_q, base changed to the algebraic closure. Choose an F_q-defined symmetric ample line bundle and record `pi*H=qH`. This avoids the reciprocal-eigenvalue ambiguity between a Frobenius morphism and arithmetic/geometric Galois actions on different realizations.
5. **Identify the trace in the Rosati formula.** The concluding identity should read `Tr(u^dagger u | V_l A)=2g Q_H(u)`. The trace on the Tate module is not generally the unweighted trace of left multiplication on the full algebra End^0(A). The proof itself correctly avoids identifying those two traces.
6. **Add one sentence to the minimal-polynomial passage.** Let `mu_f in Q[T]` be the minimal polynomial of the rational operator L_f. Diagonalizability over C makes it squarefree; `mu_f(L_f)(1)=mu_f(f)=0` gives the same annihilating polynomial in every Tate realization; its squarefreeness persists over Q_l. This makes the transfer completely explicit.
7. **List the additional curve/cohomology inputs.** The core spectral theorem uses the listed intersection and degree facts. Its application also uses the exterior-algebra description of abelian cohomology, the Jacobian identification in degree one, and the curve trace formula/rationality. These are classical and independent of RH, but should be recognized as additional inputs if the note compares prerequisite counts.

Optional wording: in the pure-sheaf counterexample, say `arithmetic Frobenius is not semisimple`. This prevents confusion with geometric semisimplicity statements, which do not fail in this example.

## Mathematical re-derivation

### A. The quadratic trace inequality

For a symmetric ample class H, the theorem of the cube supplies a cross-term B_u with

\[
([a]-[b]u)^*H=a^2H-abB_u+b^2u^*H.
\]

For rational t=a/b, b>0, its division by b^2 is a nef class. Thus

\[
t^2-b_ut+a_u\ge0,
\quad
a_u=\frac{u^*H\,H^{g-1}}{H^g},
\quad
b_u=\frac{B_uH^{g-1}}{H^g}.
\]

Rational density extends the inequality to every real t, so the discriminant gives b_u^2<=4a_u. This use of rational shifts is essential: nonnegativity merely at integer shifts would not imply a nonpositive discriminant. The manuscript does use rational shifts correctly.

The degree formula and homogeneity give the polynomial identity

\[
P_u(t)=\frac{(t^2H-tB_u+u^*H)^g}{H^g}.
\]

There is only one contribution to the coefficient of t^(2g-1): choose -tB_u in one factor and t^2H in the other g-1 factors. Therefore that coefficient is -g b_u. Since it is also -Tr(u|V_l A), the proposed constant 4g^2 is correct. No factor of two or sign has been lost.

The inequality is sharp: u=[m] gives Tr(u)=2gm and a_u=m^2.

### B. The power-sum ending

The characteristic polynomial of f is rational, so its complex roots can be used to form a diagonal complex matrix M. For every n, Tr(M^n) is the same rational trace as Tr(f^n|V_l A). This avoids any need to give the l-adic vector space a complex norm or choose a topologically meaningful embedding Q_l into C.

Repeated eigenvalues contribute positive integer multiplicities to

\[
\sum_{n\ge1}\operatorname{Tr}(M^n)z^{n-1}
=\sum_j\frac{m_j\beta_j}{1-\beta_jz}.
\]

Each nonzero beta_j contributes a genuine pole; no cancellation is possible at its reciprocal after equal roots are grouped. The exponential trace bound therefore bounds every root modulus. Jordan blocks cause no difficulty because the trace of a matrix power is the power sum of its eigenvalues with algebraic multiplicities.

When f*H=dH, induction gives f^(n*)H=d^nH. Thus the exact trace bound is 2g d^(n/2). The degree identity yields deg(f)=d^g>0, so f is an isogeny, and the product of the 2g root moduli is d^g. An upper bound sqrt(d) for every factor therefore forces equality for each. This argument is complete and has no use of RH as an input.

### C. Positivity of the real quadratic form

For nonzero u in End(A), the image u(A) has positive dimension. A morphism from a connected reduced abelian variety to a finite subgroup scheme is constant; a nonzero group endomorphism cannot have such an image. After taking a suitable very ample multiple of H, choose a hyperplane divisor that meets u(A) but does not contain it. Its pullback is a nonzero effective divisor on A. Ample intersection with H^(g-1) is strictly positive. This validates Q_H(u)>0.

The quadratic form has a rational Gram matrix in a rational basis of the finite-dimensional algebra End^0(A). Positivity on rational points gives positive semidefiniteness over R. If the Gram matrix were singular over R, its determinant would be zero over Q and its rational nullspace would be nontrivial. A nonzero rational vector there would contradict strict positivity on End^0(A). Hence the real form is genuinely positive definite.

It is important that rationality of the Gram matrix is present. A real semidefinite form can have an irrational kernel while remaining positive on every nonzero rational vector; the manuscript's rational-matrix argument correctly excludes this pitfall.

### D. Similarity, semisimplicity, and realization transfer

For u in End^0(A),

\[
Q_H(fu)
=\frac{u^*f^*H\,H^{g-1}}{H^g}
=dQ_H(u).
\]

Thus d^(-1/2)L_f is a real isometry. Polarization of Q_H gives a positive-definite Euclidean inner product. Its complexification is a positive-definite Hermitian inner product, for which the normalized operator is unitary. Consequently L_f is diagonalizable over C and its roots have modulus sqrt(d).

Let mu_f be the minimal polynomial of the Q-linear map L_f on End^0(A). It is squarefree because its complexification is diagonalizable. Applying mu_f(L_f) to the identity gives mu_f(f)=0 in End^0(A). Every Tate realization is an algebra representation, so mu_f annihilates the represented f. Because Q and Q_l have characteristic zero, the Bezout identity gcd(mu_f,mu_f')=1 persists under scalar extension. Hence f is semisimple on V_l A. Its eigenvalues are roots of mu_f, and under every complex embedding they lie on the same spectral circle.

The argument needs no equality of regular-representation multiplicities and Tate-module multiplicities. Divisibility of minimal polynomials is enough. It also needs no prior semisimplicity of the endomorphism algebra or Tate's isogeny theorem.

Since H^1 is the linear dual of the Tate module with pullback acting by transpose, its eigenvalues and semisimplicity are the same. The exterior-algebra theorem then supplies the claimed result in every H^i(A): exterior powers of a diagonalizable operator remain diagonalizable, and each eigenvalue is a product of i degree-one eigenvalues. In particular this is not an unsupported assertion of Frobenius semisimplicity for general varieties.

### E. The nef annulus

If aH<=f*H<=bH in nef order, pullback by any rational endomorphism u preserves this order after clearing denominators. Intersecting with H^(g-1) yields

\[
aQ_H(u)\le Q_H(fu)\le bQ_H(u).
\]

The inequality extends first to the real algebra by continuity and then to its complexification by applying it separately to real and imaginary parts. For an eigenvector z of L_f with eigenvalue lambda, it gives a<=|lambda|^2<=b. Every Tate-module root is a root of the minimal polynomial of L_f, so the same annulus holds there. Cases a=0 or b=0 cause no problem. No commutation or normality assumption is needed for this assertion.

### F. The pure unipotent sheaf

The map from the profinite Galois group of F_q through its Z_l quotient, followed by

\[
t\longmapsto
\begin{pmatrix}1&t\\0&1\end{pmatrix},
\]

is a continuous representation preserving a Z_l lattice. Choose the sign of the quotient to obtain the stated Frobenius matrix. It defines a lisse Q_l-sheaf on Spec(F_q). All Frobenius eigenvalues over every finite extension are 1, so the sheaf is pointwise pure of weight zero for every complex embedding. Its arithmetic Frobenius has a nontrivial Jordan block. The geometric fundamental group of the point is trivial, so this does not contradict geometric semisimplicity of pure sheaves. It correctly blocks any attempt to infer a positive-definite similarity structure from purity alone in the full arbitrary-sheaf setting.

## Independence of the standard inputs from RH

The degree polynomial, its identification with the Tate-module characteristic polynomial, finite-dimensionality of the endomorphism algebra, and the intersection proof of positivity are developed before RH in the classical theory. Milne's 2015 account gives these as Propositions 1.21--1.26, Theorem 1.27, and then derives RH in Theorem 1.30. The proofs do not cite the spectral-circle conclusion. The finite-rank proof does use earlier algebraic degree facts; therefore the second ending avoids the degree polynomial in the final spectral argument, but should not be advertised as having foundational independence from every degree-theoretic result.

The application to curves also needs the classical Jacobian correspondence and trace formula or its equivalent point-count identity. These are legitimate inputs, but the proof is not an elementary proof from field arithmetic alone.

## Primary literature overlap

### Milne, 2015

J. S. Milne, *The Riemann Hypothesis over Finite Fields: From Weil to the Present Day*, 14 September 2015.

https://www.jmilne.org/math/xnotes/pRH.pdf

- Printed page 2, footnote 1: the same pole/power-sum extraction from point-count bounds.
- Printed page 3: Hasse's elliptic discriminant argument from degree positivity at rational shifts after clearing denominators.
- Propositions 1.21--1.26, printed pages 19--21: degree and Tate-module prerequisites, without RH.
- Theorem 1.27, printed page 21: the same intersection expression for Rosati positivity.
- Corollary 1.29 and Theorem 1.30, printed page 22: the polarized circle and abelian/curve RH.
- The historical note on printed page 23 attributes the direct positivity proof to Lang 1957.

These sources establish substantive overlap. The new note's omission of Rosati notation is a presentation choice, not removal of the underlying positivity input.

### Milne, Abelian Varieties

J. S. Milne, *Abelian Varieties*, version 2.0, 2008.

https://www.jmilne.org/math/CourseNotes/AV.pdf

Part I supplies the cube, degree, Tate-module, cohomology, and positivity facts. Part II, Lemmas 1.2--1.3, printed pages 76--78, proves the spectral-circle statement for elements satisfying the polarization/Rosati relation. Its proof also establishes that the generated commutative algebra has no nilpotents, covering the semisimplicity content. The manuscript's Euclidean regular-representation argument is a concise alternative ending to the same classical mechanism.

### Kedlaya, 2019 lectures

K. S. Kedlaya, *Weil Cohomology in Practice*, Chapter 6, original lecture 16 October 2019.

https://kskedlaya.org/weil-cohom/chapter-6.html

Theorems 6.0.14--6.0.15 give the polarization intersection form and abelian RH. The exact formula is Tr(u u^dagger|V_l A)=2g(u*H.H^(g-1))/H^g. Applying its positive-form Cauchy--Schwarz inequality to 1 and u gives exactly the manuscript's trace inequality, including its constant.

### Serre, 1960

J.-P. Serre, *Analogues kahleriens de certaines conjectures de Weil*, Annals of Mathematics 71 (1960), 392--394, Theorem 1.

https://www.math.purdue.edu/~tongliu/seminar/Weil/Serre-1960.pdf

The proof normalizes a polarized cohomological action and shows it is unitary for a positive-definite Hermitian form. This is an earlier use of the same spectral principle. Its setting is smooth complex projective varieties and its input is Hodge theory, so it should not be cited as directly proving the arbitrary-characteristic abelian result by the manuscript's particular route.

## Publication assessment

Recommended repository classification: **expository proof notes / alternative proofs of established results**. Suitable description: “Short proofs of classical Frobenius spectral bounds from intersection positivity, with explicit dependencies and audit notes.”

The title “A quadratic proof of finite-field RH for curves” is acceptable because it makes no priority claim. Avoid “new proof of RH,” “stronger than Deligne,” “two-page proof of Weil II,” or “first classification-free proof” in the repository description or PR text. The correct scope is curves and abelian varieties, with classical semisimplicity in that setting.

After the small attribution and notation clarifications above, I see no mathematical reason to withhold this curve note from a public expository repository. This is an adversarial mathematical reading, not a formal verification or an assertion that every possible historical source has been exhausted.
