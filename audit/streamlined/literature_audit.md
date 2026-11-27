# Targeted literature audit: streamlined abelian comparison note

Audit date: 27 November 2026. Manuscript inspected: `upload/abelian_comparison_streamlined.tex`. This is a research and attribution check, not a claim of exhaustive priority clearance or a referee certification. No manuscript or repository file was edited.

## Assessment

The strongest defensible description is **a shorter organization of known results, with explicit quantitative consequences and independently checkable proofs**. The finite-time determinant identity has an exact precedent. Uniform cohomological-versus-numerical norm comparison is already stated in the same published paper; its elementary linear-algebra consequences include the proposed peripheral Jordan and nilpotency comparisons. Exact leading asymptotics at strict gaps are also now available in substantially greater generality.

The sharp binomial constant is a transparent extraction from an existing coefficient formula. Its explicit presentation is useful, but this search does not justify claiming a new bound. The classification-free quotient construction is a good simplification of the exposition; the underlying positive-involution representation principle is classical.

## 1. Direct overlap: Hu, arXiv:1909.12296v3

[Versioned full text](https://arxiv.org/html/1909.12296v3); [official record](https://arxiv.org/abs/1909.12296). Versions: 26 September 2019; 24 October 2021; 15 March 2022. Published in *Journal of Algebraic Geometry* **33** (2024), 265–293, [DOI 10.1090/jag/806](https://doi.org/10.1090/jag/806).

Precise locators:

| Manuscript ingredient | Primary-source location |
|---|---|
| Paired roots and even multiplicity of real roots | Theorem 1.1 |
| Characteristic polynomial interpreted as degree | Theorem 2.3 |
| Coefficients of the square-root characteristic polynomial of \(u^\dagger u\) | Corollary 1.7; its Riemann–Roch proof in §4 |
| Mixed degrees expressed through squared singular values | Equation (5.5) |
| Even cohomological/numerical spectral comparison | Theorem 1.9 |
| Uniform norm comparison for **every self-morphism**, including non-surjective ones | Corollary 5.6 and equation (5.7) |

Corollary 1.7 becomes the manuscript’s determinant identity after changing the polynomial variable’s sign. Equation (5.5) already gives the normalized elementary-symmetric formula. Corollary 5.6 explicitly states a constant independent of the self-morphism:

\[
\|f^*|H^{2k}\|_\iota\le C\|f^*|N^k_{\mathbb R}\|.
\]

The proofs of Corollary 1.7, equation (5.5), Lemma 5.4, and Corollary 5.6 were read. For a new self-contained proof, the proposed Hermitian/exterior-power argument is clearer than importing the last proof’s assertion about transpose action on numerical classes without explanation.

## 2. Elementary deductions to label as consequences

The following calculations are our explicit deductions, rather than claims that the cited papers print these exact formulations.

### Sharp finite-time constants

For nonnegative numbers \(\tau_1\ge\cdots\ge\tau_g\), put \(T_k=\tau_1\cdots\tau_k\). Every summand of \(e_k(\tau)\) is at most \(T_k\), and one summand equals it. Thus

\[
T_k\le e_k(\tau)\le\binom gk T_k.
\]

After substituting the coefficient identity and the exterior-power operator norm, this proves the proposed sandwich. Only the elementary inequality \(\rho(T)\le\|T\|\) is needed for the spectral-radius bound; invoking a general Weyl inequality adds no useful ingredient.

The constants are optimal: for the product polarization on \(E^g\), a projection onto \(E^k\) has \(T_k=1\) and \(\delta_k=1/\binom gk\). Scalar multiplication realizes equality on the other side. Even if one restricts to isogenies, diagonal maps with \(k\) entries \(N\) and the remaining entries \(1\) approach the binomial ratio as \(N\to\infty\).

### Peripheral Jordan blocks and nilpotency

Numerical cycle classes form an equivariant subquotient of the cycle-class subspace in cohomology. Fixed choices of norms, inclusion, and quotient therefore give the reverse operator-norm inequality, with a constant independent of the map. Combining the two inequalities for every iterate gives

\[
\|T^n\|\asymp\|S^n\|,
\quad T=f^*|H^{2k},\quad S=f^*|N^k.
\]

For positive spectral radius, Jordan normal form gives \(\|T^n\|\asymp\rho(T)^n n^{b_T-1}\), where \(b_T\) is the largest Jordan block among eigenvalues of maximal modulus. Consequently \(\rho(T)=\rho(S)\) and \(b_T=b_S\). When the common radius is zero, the pointwise norm inequalities give \(T^n=0\iff S^n=0\), hence identical nilpotency indices. These are immediate consequences of an established uniform norm comparison, and should be presented as such. They do not identify every Jordan block or the full Jordan forms.

## 3. Positive involutions: an exact classical reference

J. S. Milne, [*Introduction to Shimura Varieties*](https://www.jmilne.org/math/xnotes/svi2005.pdf), *Clay Mathematics Proceedings* **4** (2005), 265–378: **Proposition 8.10**, printed pp. 325–326.

For a semisimple real algebra with involution, this proposition equates positive trace, existence of a compatible positive form on a faithful module, and existence on every module. Its proof uses the regular trace form and direct summands, without an Albert case analysis. This is a precise citation for the representation principle used in Route II.

The following quotient proof is a useful elementary presentation. Once the regular module \(E\) has its positive compatible form, choose a surjection \(E^N\twoheadrightarrow V\). Its kernel is invariant under all left multiplications, including their adjoints. Its orthogonal complement is therefore invariant and maps isomorphically onto \(V\), carrying the desired form. This avoids first proving semisimplicity and decomposing into simple modules. It simplifies the manuscript’s proof but does not establish a new representation theorem.

## 4. Existing exact polynomial-growth results

### Hu, arXiv:2208.11120v3

[Official record](https://arxiv.org/abs/2208.11120); [PDF](https://arxiv.org/pdf/2208.11120). Versions: 23 August 2022; 5 September 2022; 13 August 2023. Published in *IMRN* (2024), no. 8, 6374–6399, [DOI 10.1093/imrn/rnad170](https://doi.org/10.1093/imrn/rnad170).

**Theorem 1.5** describes paired Jordan structures on Tate spaces. **Theorem 1.12**, printed p. 6, identifies the largest numerical-divisor Jordan block for quasi-unipotent automorphisms: a largest Tate block of size \(s\) gives size \(2s-1\) on \(N^1\), and polynomial exponent \(2s-2\). Its proof, printed p. 18, explicitly studies the second compound matrix. **Remark 4.3**, printed p. 19, discusses higher exterior powers, including a fourth-degree exponent formula. The appendix contains further Riemann–Roch/determinant computations.

This is directly relevant precedent for deriving exact polynomial behavior from Tate-space Jordan blocks. Theorem 1.12 and its proof were inspected, not just the abstract.

### Hu–Jiang, arXiv:2609.29877v1

[Official record](https://arxiv.org/abs/2609.29877); [versioned full text](https://arxiv.org/html/2609.29877v1). Submitted **24 September 2026**; only v1 is listed as of this audit.

**Proposition 5.1** proves

\[
\deg_i(f^n)\asymp\|(f^n)^*|N^i\|\asymp\lambda_i^n n^{\mu_i},
\]

with \(\mu_i+1\) the largest peripheral numerical Jordan-block size. **Theorem 1.2** proves \(\mu_i=0\) at strict log-concavity gaps, the adjacent-exponent inequality \(0\le2\mu_i-\mu_{i-1}-\mu_{i+1}\le4\) on flat portions, and the universal bound \(\mu_i\le2i(d-i)\), for surjective endomorphisms of normal projective varieties in arbitrary characteristic. **Remark 1.4** distinguishes peripheral semisimplicity from full semisimplicity.

The proof of Proposition 5.1 was read: it uses effective/pliant cones to compare degree and numerical operator norm, followed by finite-dimensional Jordan theory. Appendix A supplies sharp examples on powers of elliptic curves. Thus universal exponent bounds and strict-gap vanishing are established in much broader scope than the attachment.

## 5. Very recent exact asymptotics at gaps

Fei Hu, [*Degree growth of rational and meromorphic self-maps*, arXiv:2610.18094v1](https://arxiv.org/html/2610.18094v1); [official history](https://arxiv.org/abs/2610.18094). Submitted **13 October 2026**, 10:13:03 UTC; only v1 is listed.

**Theorem 1.5** gives

\[
\deg_i(f^n)=C\lambda_i^n+O(\eta^n),\qquad C>0,
\]

for every \(\sqrt{\lambda_{i-1}\lambda_{i+1}}<\eta<\lambda_i\), for dominant rational self-maps of normal projective varieties in arbitrary characteristic, and dominant meromorphic self-maps of compact Kähler manifolds.

The complete proof in **§4.1**, including **Lemma 4.1**, was read. An exponentially small discrete second difference of \(\log\deg_i(f^n)\) makes its slopes exponentially Cauchy, yielding the positive leading constant and error. **Corollaries 5.3–5.4** give ratio convergence and a simple dominant generating-function pole. **Remark 1.6** explains why the endpoint exponential error can require a polynomial factor.

Accordingly, adding an exact positive normalized limit at a strict gap does not extend the present literature’s theorem scope. It remains a worthwhile short corollary in the abelian proof.

## 6. Older directly pertinent precedents

- Nguyen-Bac Dang, [*Degrees of iterates of rational maps on normal projective varieties*, arXiv:1701.07760](https://arxiv.org/pdf/1701.07760), v2 dated 16 July 2019; *Proc. London Math. Soc.* **121** (2020), 1268–1310. **Theorem 2**, proved as **Theorem 5.3.2**, establishes uniform degree/operator-norm comparison on numerical classes, including relative degrees. The proof in §5.3 was read; it uses cone decompositions and Siu-type estimates. This is important prior art for the degree–norm bridge, not a claim about all étale cohomology.

- Charles Favre–Elizabeth Wulcan, [*Degree growth of monomial maps and McMullen’s polytope algebra*, arXiv:1011.2854](https://arxiv.org/pdf/1011.2854), v2 dated 31 March 2011. **Theorem A/§5, Theorem 5.1** compare monomial-map degrees with exterior-power norms. **Theorem D/§6, Theorem 6.1** give exact leading asymptotics at strict gaps. The proof setup, diagonalizable case, and §6 theorem were read. This is an older instance of the same broad operator-growth strategy, in a different geometric setting.

- Nguyen-Bac Dang–Charles Favre, [*Spectral interpretations of dynamical degrees and applications*, arXiv:2006.10262](https://arxiv.org/pdf/2006.10262), v2 dated 11 May 2021; [*Annals of Mathematics* **194** (2021), 299–359](https://annals.math.princeton.edu/2021/194-1/p05). **Theorem 1** gives \(\deg_1(f^n)=C\lambda_1^n+O(\eta^n)\) under \(\lambda_1^2>\lambda_2\), in characteristic zero. Its theorem statement was checked; this audit did not reproduce the paper’s full Banach-space construction.

The newer papers above are sufficient to settle the requested attribution questions. No sweeping claim about the complete Dinh–Nguyen–Truong literature is intended.

## 7. Power-sum lemma: credit the classical argument precisely

Deligne, [*La conjecture de Weil: I*, IHÉS **43** (1974), 273–307](https://www.numdam.org/item/PMIHES_1974__43__273_0/), [English translation hosted by Milne](https://www.jmilne.org/math/Documents/DeligneWeilI.pdf), **(1.5.3)** contains the trace/log-determinant formal identity. The arguments at **(3.5)–(3.6)** concern nonnegative-coefficient products and radius comparison; they are not a verbatim statement of the arbitrary finite power-sum pole lemma.

Dingxin Zhang, [arXiv:2611.30749v1](https://arxiv.org/html/2611.30749v1), **Lemma 2.1**, gives the exact rational-pole proof for finite power sums and calls the traces-to-eigenvalues passage standard. Its proof was read.

Recommended wording: “the classical power-sum/radius-of-convergence argument; compare Deligne, Weil I, (1.5.3).” Neither attribution of priority to the new preprint nor an unsupported claim that Deligne originated this elementary lemma is justified by these sources.

## 8. Concrete corrections and editorial consequences

1. **Zero spectral radius:** Corollary (ii) cannot assert \(\|T^n\|\le Cn^{m-1}\rho(T)^n\) for every \(n\ge1\) when \(\rho(T)=0\) but \(T\ne0\) is nilpotent. State the exponential-polynomial estimate for positive radius, defining \(m\) as the largest peripheral Jordan block; handle radius zero by eventual vanishing and the nilpotency comparison.
2. **Cohomological weight:** Corollary (iii) should explicitly say modulus \(d^{i/2}\) on \(H^i\). “The same holds” immediately after a clause giving modulus \(\sqrt d\) is ambiguous.
3. **What is added:** Say “explicit sharp constants and a shorter proof,” not “a stronger new theorem,” unless a genuinely new statement is isolated and independently checked.
4. **Citations to add:** Hu Corollary 5.6; Milne Proposition 8.10; Hu–Jiang Proposition 5.1/Theorem 1.2; Hu Theorem 1.5 (October 2026); precise classical power-sum attribution if that lemma remains in an earlier companion note.
5. **Strength of comparisons:** Peripheral maximum-block equality is weaker than equality of all Jordan blocks. Strict-gap degree asymptotics likewise do not assert semisimplicity of the entire cohomological operator.

## Search coverage and limitations

Searches used primary arXiv records, versioned HTML/PDFs, author-hosted text, and journal pages. Recent searches included 30–60-day windows for abelian norm comparison, degree growth, Jordan blocks, and singular values, through 27 November 2026. Those searches found no additional primary paper changing the conclusions above beyond the September and October Hu/Hu–Jiang preprints already inspected. This negative result is bounded by indexing, query choice, and access; it is not a comprehensive novelty certificate. Unverified community reposts and search snippets were not accepted as mathematical evidence.

The previous broader review, `LITERATURE.md`, separately records the November short-RH papers and general dynamical-degree comparison literature. This targeted report neither replaces that record nor certifies that the general sheaf arguments have been reduced to the Jacobian/abelian setting.
