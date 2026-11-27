# Adversarial audit: abelian spectral comparison in all codimensions

**Audit date:** 27 November 2026.  
**Audited source:** `pre-revision/abelian_all_degrees_proof.tex`.  
**SHA-256 of the audited source:** `7e9f8774f799d29462f420ecd8afb731d5a9e0c3a188a7628c2da6d103f8fc8e`.

This is an independent skeptical rereading of the mathematical source, followed by primary-source checks against Hu's comparison paper and relevant recent literature. The canonical manuscript was not edited during this audit. This report does not constitute external peer review or a formal proof verification.

## 1. Verdict

**No fatal gap, false theorem, or circular use of the desired comparison theorem was found.** The principal argument is valid under the stated classical prerequisites. In particular, the following chain is sound:

1. The rational degree identity makes the characteristic polynomial nonnegative on the real axis, giving conjugate pairing and even multiplicity of real roots.
2. The numerical parallelogram identity and nef positivity give the mixed-degree polynomial majorant.
3. A fixed matrix coefficient in exterior-power cohomology supplies the exponential upper bound, allowing arbitrary Jordan blocks.
4. Testing the polynomial at an exponential scale forces a positive lower multiple of the target exponential at every strict spectral gap.
5. Khovanskii--Teissier fills every repeated-modulus block.
6. Numerical classes are a quotient of the algebraic part of cohomology; together with the established mixed-degree growth, this gives equality of the numerical and cohomological spectral radii.

The quantitative claim, the non-surjective extension, and the two-map corollary also survive the audit. There is no mathematical reason identified here to withhold publication **as an alternative-proof research note about established results**, after the small clarifications and literature additions below. The audit does not establish bibliographical novelty of the proof organization.

## 2. Corrections and clarifications recommended before publication

None of these requires changing the mathematical argument.

### 2.1 State the degree convention

Equation (4) is written for every rational number, including values at which `[a]-[b]u` is not an isogeny. Add:

> For a homomorphism that is not an isogeny, its degree is defined to be zero.

This is the convention used in Hu's Theorem 2.3 and in the companion curve note. Alternatively, state the degree identity first away from the finitely many non-isogeny values and extend polynomially; the zero convention is shorter.

### 2.2 Name the base field and avoid the codimension clash

The opening paragraph says “over an algebraically closed field” but subsequently writes `char k`, while `k` is also the codimension index. Write “over an algebraically closed field `K`” and use `char K`.

### 2.3 Define the nef order and the two maps

Before or inside the two-map corollary, say that `u,v` are group endomorphisms of `A`, and that `D ≼ E` means that `E-D` is nef. The argument also extends to regular self-morphisms after removing translations, but the group-endomorphism statement is the cleanest immediate formulation.

### 2.4 Attribute the odd-degree formula precisely

The identity

\[
\chi_{2k+1}=\sqrt{\lambda_k\lambda_{k+1}}
\]

already appears explicitly in **Hu, arXiv:1909.12296v3, Remark 5.5**, with an equivalent reindexing. Add that locator next to the theorem's provenance statement. The present proof rederives this formula; it is not a new extension of Hu's conclusions.

### 2.5 Account for the stronger September 2026 quantitative results

Add a short comparison with **Hu--Jiang, arXiv:2609.29877v1, Theorem 1.2 and Proposition 5.1**. Their results imply substantially sharper control of the polynomial factors in degree growth, for normal projective varieties in arbitrary characteristic. The manuscript's inequality (12) is a useful direct byproduct of its short proof, not an improvement on the current best general growth estimates.

### 2.6 Optional exposition improvements

- Say that the field embedding into `C` is abstract, with no continuity intended.
- State that Tate twists are suppressed in the cycle-class paragraph, and all actions there are geometric endomorphism pullbacks.
- State that the constants in (8), (10), and (12) may depend on the fixed variety, endomorphism, ample class, degree, and chosen realization. No uniformity in these data is proved.
- In the non-surjective paragraph, mention the eventual vanishing of the terms beyond `h` before applying the strict-gap argument to the remaining terms. The existing order is understandable, but reversing these two sentences makes the reduction explicit.

## 3. Characteristic polynomial, rational positivity, and complex embeddings

### 3.1 The necessary classical identity

For `u` in `End(A)`, the polynomial

\[
P_u(t)=\det(t-u\mid V_\ell A)
\]

has integer coefficients, is independent of `ell`, and satisfies

\[
P_u(a/b)=b^{-2g}\deg([a]-[b]u),\qquad b>0.
\]

This is not being imported from Deligne's rationality or weight theorem. It is the classical degree-polynomial theorem for abelian varieties. Hu's Theorem 2.3 explicitly states its rational-argument form and cites Mumford, §19, Theorem 4, and Milne, §12, Proposition 12.4.

Clearing a denominator remains valid when the characteristic divides `b`: `[b]` is an isogeny of degree `b^(2g)`, possibly inseparable. No division by `b` in the ground field is used.

### 3.2 Positivity really holds on all of the real axis

Degrees of isogenies are positive, and the zero convention handles non-isogenies. Therefore `P_u(a/b) >= 0` for every rational number. Continuity gives `P_u(t) >= 0` for every real `t`. A real root of odd multiplicity would force a sign change, so every real root has even multiplicity.

Since the coefficients are rational, the nonreal roots occur in complex-conjugate pairs. Sorting their absolute values therefore gives

\[
s_1,s_1,s_2,s_2,\ldots,s_g,s_g.
\]

This proves the parity conclusion stated in Hu's Theorem 1.1 directly from his Theorem 2.3. It does not rely on a classification of endomorphism algebras.

### 3.3 No topological comparison between `Q_l` and `C` is used

The abstract embedding `iota: Q_l-bar -> C` is legitimate. After applying it to matrix entries, ordinary complex finite-dimensional linear algebra applies. The intersection numbers `delta_k(n)` are rational numbers and are fixed by `iota`. The characteristic polynomial is rational, so the complete multiset of its complex roots is independent of the embedding as a multiset. The same holds for all its exterior powers. Consequently the proof does not make an illicit comparison between the `ell`-adic and archimedean topologies.

The Tate-module action and the action by pullback on `H^1` have the same characteristic polynomial: the latter is the transpose action on the linear dual, not the inverse. Inverse eigenvalues would arise from a different convention for a Galois representation, which is not the action used in the proof.

## 4. The mixed-degree polynomial inequality

For rational `t=a/b`, define

\[
X=b^{-2}([a]-[b]f^n)^*H,\qquad
Y=b^{-2}([a]+[b]f^n)^*H.
\]

These are nef rational divisor classes. The theorem of the cube gives

\[
X+Y=2\bigl(t^2H+(f^n)^*H\bigr).
\]

Every mixed intersection of `X` and `Y` is nonnegative. Hence

\[
X^g\le(X+Y)^g.
\]

The top-intersection identity gives `X^g/H^g=P_(f^n)(t)`. Expanding the right side yields exactly

\[
0\le P_{f^n}(t)
\le 2^g\sum_{j=0}^g\binom gj t^{2(g-j)}\delta_j(n).
\]

The factor `2^g` and all powers of `t` are correct. Rational density extends the scalar inequality to every real `t`. No actual endomorphism with an arbitrary real coefficient needs to exist.

The only positivity used here is that of mixed intersections of nef divisors. There is no assumed positivity theorem for arbitrary higher-codimension cycles.

## 5. Upper bounds and Jordan blocks

The equality

\[
\delta_j(n)
=\frac{\bigl((f^*)^n\operatorname{cl}(H)^j\bigr)
             \operatorname{cl}(H)^{g-j}}{H^g}
\]

expresses the mixed degree as a fixed matrix coefficient on `H^(2j)`. Since abelian cohomology is the exterior algebra on `H^1`, the spectral radius on this group is

\[
U_j=\prod_{r=1}^j s_r^2.
\]

If `m_j` is the largest Jordan-block size among eigenvalues of modulus `U_j`, then

\[
\delta_j(n)\le C_j n^{m_j-1}U_j^n.
\]

This remains correct if a subdominant eigenvalue has a larger Jordan block. A factor `n^d r^n` with `r<U_j` is bounded by a constant multiple of `n^(m_j-1)U_j^n`; the exponential gap absorbs any fixed polynomial discrepancy. For an isogeny `U_j>0` in every degree, so this argument has no zero-radius exception within the main theorem.

Semisimplicity is not assumed. Its absence is properly handled by the polynomial factor.

## 6. Strict spectral gaps and the lower bound

Fix `k` with `s_k>s_(k+1)`, choose `s_(k+1)<R<s_k`, and set `t_n=2R^n`.

For roots above `R`,

\[
\frac{|2R^n-\alpha^n|}{|\alpha|^n}\longrightarrow1;
\]

for roots below `R`,

\[
\frac{|2R^n-\alpha^n|}{2R^n}\longrightarrow1.
\]

Because `P_(f^n)(t_n)` is real and nonnegative, it equals the product of these absolute values. Thus

\[
\frac{P_{f^n}(2R^n)}{U_k^nR^{2n(g-k)}}
\longrightarrow 2^{2(g-k)}.
\]

The normalization constant is correct. A possible equality `2R^n=alpha^n` at an isolated small `n` causes no difficulty; strict separation of moduli makes this impossible for all sufficiently large `n`.

The ratios of successive exponential scales on the majorant side are

\[
\frac{U_{j+1}R^{2(g-j-1)}}{U_jR^{2(g-j)}}
=\frac{s_{j+1}^2}{R^2}.
\]

They are greater than one before `k` and less than one after `k`. The `k`-th term therefore has a unique maximal exponential rate. Every other term, including its polynomial factor, is exponentially negligible after division by `U_k^n R^(2n(g-k))`. The positive limit on the determinant side forces

\[
\delta_k(n)\ge c_kU_k^n
\]

for all sufficiently large `n`. This is a pointwise eventual lower bound, not merely a subsequence or limsup bound. There is no exchange of a limit over `R` with a limit over `n`: `R` is fixed strictly inside a gap throughout.

## 7. Repeated moduli and arbitrary characteristic

For each `n`, Khovanskii--Teissier gives

\[
\delta_k(n)^2\ge\delta_{k-1}(n)\delta_{k+1}(n).
\]

Because `f` is an isogeny, `(f^n)^*H` is ample, all these numbers are positive, and their logarithms form a concave sequence. If `s_(a+1)=...=s_b`, the concavity inequality between its endpoint indices is

\[
\delta_k(n)\ge
\delta_a(n)^{(b-k)/(b-a)}
\delta_b(n)^{(k-a)/(b-a)}.
\]

The corresponding target values `U_k` interpolate with equality. The endpoint lower bounds therefore propagate across every block. Together with the upper bounds, this proves all limits and the claimed positive constant lower bounds.

The characteristic-free use of Khovanskii--Teissier is justified. For ample divisors choose sufficiently large very ample multiples and take a general smooth complete-intersection surface of `k-1` divisors of one type and `g-k-1` of the other. Bertini for these embeddings works over an algebraically closed field in every characteristic. The surface Hodge-index theorem gives the stated mixed inequality. Approximation by ample rational classes gives the nef case. This is independent of Deligne's weights and of the numerical/cohomological dynamical comparison being proved.

The flat-block step is essential. An inequality for an exponential envelope alone does not determine an individual coefficient strictly inside a linear segment of that envelope. The manuscript correctly supplies log-concavity rather than silently assuming coefficientwise recovery.

## 8. Numerical classes are a quotient, not a presumed subspace

The proof correctly uses the implication

\[
\text{homologically trivial}\Longrightarrow
\text{numerically trivial},
\]

which follows by pairing a zero cohomology class with every complementary cycle class. It does not assume the converse.

More explicitly, let `V_alg` be the `Q_l`-span of algebraic cycle classes in `H^(2k)(A,Q_l(k))`. A `Q_l`-linear relation among cycle classes has zero intersection with every complementary cycle. Because the numerical pairing is defined by rational intersection matrices, its rank is preserved upon extending scalars from `Q` to `Q_l`. Such a relation is therefore also zero in `N^k(A)_Q tensor Q_l`. Sending a cycle class to its numerical class gives an equivariant surjection

\[
V_{\mathrm{alg}}\twoheadrightarrow N^k(A)_\mathbb Q\otimes\mathbb Q_\ell.
\]

Thus the numerical spectrum is contained in the cohomological spectrum, and `lambda_k<=chi_(2k)`. The opposite inequality follows because `delta_k(n)` is also a fixed matrix coefficient on the numerical group and its exponential rate has already been proved to equal `chi_(2k)`.

This route proves the degree-growth limit rather than invoking its existence as a theorem of algebraic dynamics. It also avoids standard conjecture D.

Tate twists do not change the spectrum of a geometric endomorphism pullback: the endomorphism acts trivially on the coefficient twist. This statement must not be confused with Galois Frobenius acting on twisted cohomology. The manuscript's final Frobenius-convention sentence appropriately distinguishes these actions.

## 9. Quantitative claims and non-surjective maps

### 9.1 Quantitative estimate

For an isogeny, every `delta_k(n)` is positive. Hence the eventual lower bounds can be extended to every `n>=1` by reducing the constant across the finitely many initial values. The upper Jordan bound already holds for every `n>=1` after adjusting its constant. Thus equation (12) is valid as stated under the manuscript's initial isogeny hypothesis.

The assertion that absence of peripheral Jordan blocks gives comparability with `lambda_k^n` is also valid. It does not assert a limiting coefficient or exclude oscillation in the semisimple peripheral spectrum.

### 9.2 Non-surjective extension

Let exactly `2h` characteristic roots be nonzero. For `k>h`, every eigenvalue of the exterior power on `H^(2k)` is zero; the finite-dimensional operator is nilpotent. Hence `delta_k(n)=0` eventually. The numerical quotient is nilpotent as well.

For the remaining indices, use `0<R<s_h` to expose index `h`. Terms beyond `h` have already vanished for large `n`, so the same strict-gap proof is valid. Log-concavity is required only inside the positive part. If `h=0`, all positive-degree operators are nilpotent and the conclusion is immediate.

The proof does not require replacing the abelian variety by a stabilized image. The quantitative statement involving a positive spectral radius should be read on the positive part; no expression involving the largest peripheral Jordan block at a positive radius is intended for a zero-radius group.

### 9.3 Translations

Every regular self-morphism of an abelian variety is a translation composed with a group endomorphism. Translations act trivially on its cohomology and numerical classes. The extension to surjective self-morphisms is therefore valid, as in Hu's proof of Theorem 1.9.

## 10. Two-map common-polarization corollary

Suppose `u^*H=aH`, `v^*H=bH`, with `a,b>=0`. Quadraticity gives

\[
(tu-v)^*H=(at^2+b)H-tB.
\]

For every integral curve `C`, `H.C>0`. Nefness at rational `t` and real continuity give

\[
a(H.C)t^2-(B.C)t+b(H.C)\ge0
\]

for every real `t`. The discriminant condition gives

\[
|B.C|\le2\sqrt{ab}(H.C).
\]

When `a=0` or `b=0`, the same conclusion follows because an affine polynomial nonnegative for every real `t` has zero linear coefficient. Thus there is no lost degenerate case.

The curvewise inequalities say that both `2 sqrt(ab)H-B` and `2 sqrt(ab)H+B` are nef. Consequently

\[
(\sqrt a-\sqrt b)^2H\preceq(u-v)^*H
\preceq(\sqrt a+\sqrt b)^2H.
\]

Top intersections preserve this order for nef classes, proving the degree inequalities. The argument never interchanges `uv` and `vu`, so commutativity is genuinely unnecessary.

The constants are sharp in elementary examples: multiplication maps `[m]` and `[n]` attain the lower bound, while `[m]` and `[-n]` attain the upper bound. This is a direct polarization Cauchy--Schwarz consequence, and no originality claim for it should be made without a separate literature search.

## 11. Literature overlap and recent results

### 11.1 Hu's original comparison paper

Primary source: [Fei Hu, Eigenvalues and dynamical degrees of self-maps on abelian varieties, arXiv:1909.12296v3](https://arxiv.org/pdf/1909.12296), dated 15 March 2022; published in *Journal of Algebraic Geometry* **33** (2024), 265--293, [DOI 10.1090/jag/806](https://doi.org/10.1090/jag/806).

The primary text was inspected at the following locations:

- **Theorem 1.1:** conjugate pairing and even multiplicity of real roots.
- **Theorem 1.9:** equality `chi_(2k)=lambda_k` in every codimension.
- **Theorem 2.1:** exterior-algebra cohomology and Tate duality.
- **Theorem 2.3:** the characteristic/degree identity for every rational argument.
- **Remark 5.5:** the exact odd-degree formula appearing in the manuscript.
- **Corollary 5.6:** a uniform norm-comparison statement for all self-morphisms of a fixed abelian variety.
- **Remark 1.11(3):** treatment of non-surjective maps by stabilized-image reduction.

Hu's paper explicitly says its proof of Theorem 1.1 uses the Albert classification. Its comparison proof subsequently uses the Rosati involution, Albert polynomials, singular-value asymptotics, and a degree-growth interpretation. The present note's rational positivity plus nef polynomial envelope is a different proof organization. The theorem, its odd-degree consequence, and its broader endomorphism scope are established results.

### 11.2 September 2026: Hu--Jiang

Primary sources:

- [Abstract and metadata, arXiv:2609.29877](https://arxiv.org/abs/2609.29877).
- [Full HTML text, arXiv:2609.29877v1](https://arxiv.org/html/2609.29877v1).

Fei Hu and Chen Jiang, *Uniform Turán estimates and sharp bounds for degree and mixed orbit growth*, submitted 24 September 2026. The full HTML introduction, main statements, and proof-strategy section were inspected. This audit did not independently certify every argument of that 34-page preprint.

The paper treats surjective endomorphisms of normal projective varieties in arbitrary characteristic. It describes

\[
\deg_i(f^n)\asymp\lambda_i^n n^{\mu_i},
\]

where `mu_i+1` is the largest peripheral Jordan-block size on the numerical group. Its **Theorem 1.2** states:

- strict log-concavity at index `i` forces `mu_i=0`;
- at equality, `0<=2mu_i-mu_(i-1)-mu_(i+1)<=4`;
- on a maximal affine interval `[r,s]` of `log lambda`, `mu_i<=2(i-r)(s-i)`;
- consequently `mu_i<=2i(d-i)`, with sharp examples.

Its **Proposition 5.1** supplies degree--norm comparison. Its strict-break/affine-interval organization has a thematic relationship to the present note's exposed indices and flat blocks, although it addresses the finer polynomial-growth layer, not this short proof of the abelian cohomological comparison theorem.

The note's inequality (12) is weaker than these recent quantitative results. It remains worth recording because it follows immediately from the alternative proof, but it should be presented as such and cited against the current literature.

### 11.3 October 2026: Hu--Truong--Xie

A recent publisher record was also located: [Tate's Question, Standard Conjecture D, Semisimplicity and Dynamical Degree Comparison Conjecture](https://actamath.cjoe.ac.cn/Jwk_sxxb_en/EN/10.1007/s10114-026-5249-8), Fei Hu, Tuyen Trung Truong, Junyi Xie, *Acta Mathematica Sinica* **42** (2026), 2503--2515, issue date 19 October 2026, DOI `10.1007/s10114-026-5249-8`.

The publisher's indexed abstract states results over algebraic closures of finite fields under standard conjecture D on `X x X`, as well as an alternative proof of a result of Xie about polarized endomorphisms. The complete article was not inspected in this audit. This is relevant context for a repository-wide literature review, but nothing in the present abelian proof depends on it.

### 11.4 Limits of the novelty check

Targeted searches included combinations of “abelian varieties,” “degree polynomial,” “parallelogram,” “dynamical degrees,” “short proof,” and 2026 results, using recency filters for the current-year sweep. No exact earlier match for the degree-polynomial envelope proof was found in that search. This is insufficient to establish priority. The appropriate manuscript language remains that this is a short proof of a known theorem, with novelty of the organization unclaimed.

## 12. Publication recommendation

Proceed with publication as a carefully attributed research note after:

1. adding the zero-degree convention, base-field notation, and nef-order/map definitions;
2. citing Hu's Remark 5.5 for the odd-degree formula;
3. adding the Hu--Jiang 2026 comparison so the quantitative paragraph accurately reflects current literature;
4. retaining the explicit boundary that this is an abelian-variety/function-field argument, not an arbitrary-sheaf proof and not a proof of the classical Riemann hypothesis;
5. retaining the statement that proof novelty has not been established exhaustively.

No mathematical finding from this audit requires retracting the main proof, weakening its theorem, or withholding a public alternative-proof note.
