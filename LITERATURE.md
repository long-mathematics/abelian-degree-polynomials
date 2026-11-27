# Literature and scope audit

**Audit cutoff:** 27 November 2026 (UTC).  
**Purpose:** Check the two local proof notes against their stated sources and recent relevant work; distinguish a shorter presentation of known results from a new theorem or an established priority claim.

## Findings that affect the manuscripts

No fatal mathematical defect emerged from the literature comparison or from my independent reading of the two notes. This is a research audit, not a formal verification or a referee certification.

The bibliography needs a substantial update. Xie's theorem has broader scope than the abelian note, and his proof contains a close precedent for its scaling and concavity strategy. Section 3 details both points.

The curve note appropriately identifies itself as a classical synthesis. Its quadratic intersection form and scaled-isometry ending belong to the classical Weil–Rosati positivity method. Removing some of the usual intermediate algebra is an expository improvement; semisimplicity in this setting is also classical.

The abelian note's potentially useful contribution is a particular combination of elementary degree-polynomial positivity, a nef parallelogram estimate, and comparison at separated spectral scales. I did not find this exact combination in the papers inspected. That is **not** an exhaustive priority result.

### Local texts inspected

- `pre-revision/short_curve_rh_proof.tex`: *A quadratic proof of finite-field RH for curves*.
- `pre-revision/abelian_all_degrees_proof.tex`: *A degree-polynomial proof of spectral comparison in every codimension on an abelian variety*.

The initial literature audit inspected the pre-revision texts. The repository copies now incorporate the bibliography and scope corrections; their final source hashes and review are recorded in `audit/final_source_review.md`. The September 2026 Hu–Jiang item was added by a separate targeted primary-source check.

## 1. The November finite-field proof: exact version status

### Alpöge–Hexagon

**Primary record:** [Hexagon 2611.00789v2](https://hexagonmath.org/2611.00789v2).  
**Exact PDF:** [2611.00789v2](https://hexagonmath.org/pdf/2611.00789v2).  
**Earlier version:** [2611.00789v1](https://hexagonmath.org/2611.00789v1).

The record lists v1 on **21 November 2026**, ten pages, and current v2 on **24 November 2026**, fourteen pages. The six-page description concerns the core argument with its cohomological prerequisites. The page header retains the original submission date; use the explicit version history for v2's date.

The v2 comments say the proof is unchanged and the presentation was revised after Zhang. The added remarks already cover the single-cohomology-group formulation, the need for a replacement operator to commute with Frobenius, sharpness through Gauss-sum sheaves, and traces' inability to detect nilpotent Jordan parts. Those observations are not new additions from our investigation.

The provenance record identifies an already-adopted correction: weak Lefschetz is taken from Deligne's proof in Katz's appendix rather than the printed proof of Katz's Corollary 3.4.1. It reports no human checking of v2, while acknowledging Zhang's exposition. No v3, withdrawal, or further correction was visible in the primary record at the audit cutoff.

### Dingxin Zhang

**Primary record:** [arXiv:2611.30749](https://arxiv.org/abs/2611.30749).  
**Exact text:** [2611.30749v1 HTML](https://arxiv.org/html/2611.30749v1), [PDF](https://arxiv.org/pdf/2611.30749v1).

The official history lists only **v1, 23 November 2026, 14:24:22 UTC**. The five-page PDF is internally dated **22 November 2026**. Its PDF title is *On an elementary proof of Weil II*; the arXiv record title is *Notes on an elementary proof of Weil II from Hexagon*. These are the same note, not separate competing proofs.

Zhang describes his text as an exposition and makes no originality claim. “Elementary” concerns the analytic core; étale cohomology, Artin vanishing, and perverse weak Lefschetz remain inputs. The inspected text treats the affine-line argument and explains its place in the general theorem. No revised version or correction was present in the official history at the cutoff.

### Other very recent material

Recent searches also surfaced a 24 November exercise-workbook page entitled *The sign-only proof of the Riemann hypothesis for curves*. Its search record cites the same Alpöge–Hexagon sources. Direct retrieval of the substantive page failed, so this audit does **not** classify its mathematical content or count it as an independently checked proof. Primary URL: <https://ultronozm.github.io/grh-workbook/20261124T220500--sign-only-proof-for-curves__workbook.html>.

Searches for late-November RH material returned several discussions of the separate classical-number-field announcement. They are outside the finite-field/function-field scope of these notes and were not treated as evidence for their arguments.

## 2. Exact theorem overlap: Fei Hu

**Paper:** *Eigenvalues and dynamical degrees of self-maps on abelian varieties*.  
**Primary record:** [arXiv:1909.12296](https://arxiv.org/abs/1909.12296).  
**Inspected version:** [v3 full text](https://arxiv.org/html/1909.12296v3), **15 March 2022**. Earlier submissions: 26 September 2019 and 24 October 2021.  
**Publication:** *Journal of Algebraic Geometry* **33** (2024), 265–293; [DOI 10.1090/jag/806](https://doi.org/10.1090/jag/806), published electronically 7 February 2023.

The exact overlaps are Hu's Theorem 1.1 (conjugate pairing and even multiplicity of real roots on first cohomology), Theorem 1.9 (all-codimension equality of numerical and cohomological spectral radii), and Theorem 2.3 (the rational degree-polynomial identity). His §3 uses Albert's classification; §5 uses Rosati positivity, Albert polynomials, mixed intersections, and singular values of matrix powers.

The new note's nonnegativity argument gives a direct route from the degree identity to root parity. Its separated-scale argument replaces the classification/singular-value route for spectral comparison. These are differences in proof, not new parity or comparison statements. Hu's odd-cohomology remark and the exterior-power description also preclude promoting the odd-degree formula as an independent new theorem.

## 3. A broader known theorem and a close methodological precedent

### Junyi Xie

**Paper:** *Numerical spectrums control Cohomological spectrums*.  
**Primary record:** [arXiv:2412.01216](https://arxiv.org/abs/2412.01216).  
**Inspected text:** [v2](https://arxiv.org/html/2412.01216v2). Official history: v1 **2 December 2024**, v2 **30 March 2025**.

Theorem 1.2 proves even-degree numerical/cohomological spectral comparison for every surjective endomorphism of a smooth irreducible projective variety over an arbitrary field. Section 2.5 tilts two concave spectral polygons using Frobenius powers, selects a vertex as the unique maximum, proves equality there, and obtains equality of the polygons. This is a close conceptual precedent for the local note's strict-gap/concavity argument. Xie's introduction and proof explicitly use Deligne's RH theorem.

The proposed abelian proof has a different geometric input and avoids that use of Deligne. A reported Duke DOI, <https://doi.org/10.1215/00127094-2025-0080>, was inaccessible; cite the verified preprint. Its official version dates are given above, rather than the different internal HTML date.

### Hu–Truong–Xie

**Paper:** *Tate's question, Standard conjecture D, semisimplicity and Dynamical degree comparison conjecture*.  
**Primary text:** [arXiv:2503.09432v1](https://arxiv.org/html/2503.09432v1), submitted **12 March 2025**.  
**Publisher record:** [Acta Mathematica Sinica 42 (2026), 2503–2515](https://actamath.cjoe.ac.cn/Jwk_sxxb_en/EN/10.1007/s10114-026-5249-8), issue date **19 October 2026**.

Proposition 1.4 and Lemma 2.2 make the scaling/maximum/concave-envelope method particularly explicit. They derive inequalities of the form

\[
r^k\chi_k\leq\max_j r^{2j}\lambda_j
\]

by composing with positive or negative Frobenius powers and using their known weights. The paper also separates unconditional finite-correspondence comparison from results requiring Standard Conjecture D, including its more general semisimplicity discussion. These hypotheses must not be silently dropped when describing the current state of the subject. The relevant proposition, lemma, and proof were read, not just the abstract.

## 4. Polynomial growth, Jordan blocks, and 2026 intersection-polynomial work

### Hu's exact abelian Jordan-growth results

**Paper:** *Polynomial volume growth of quasi-unipotent automorphisms of abelian varieties (with an appendix in collaboration with Chen Jiang)*.  
**Primary record:** [arXiv:2208.11120](https://arxiv.org/abs/2208.11120); latest v3 **13 August 2023**, first submitted **23 August 2022**.  
**Publication:** *IMRN* 2024, no. 8, 6374–6399; [DOI 10.1093/imrn/rnad170](https://doi.org/10.1093/imrn/rnad170). Theorem 1.5, Theorem 1.12, and the relevant proof sections were inspected in the [PDF](https://arxiv.org/pdf/2208.11120).

For a quasi-unipotent abelian automorphism, Theorem 1.12 relates the largest Tate-module Jordan block to the largest block on the numerical divisor space: a Tate block of size (s) gives first-degree growth of order (n^{2(s-1)}). The paper also proves stronger paired-block structure than mere pairing of eigenvalue moduli. Consequently, an exact Jordan-growth law in this zero-entropy setting is already established. The local manuscript's nonoptimal polynomial upper bound should remain described as a byproduct, not an optimal new theorem.

### Hu–Jiang, September 2026

**Paper:** *Uniform Turán estimates and sharp bounds for degree and mixed orbit growth*.
**Primary version:** [arXiv:2609.29877v1](https://arxiv.org/html/2609.29877v1), submitted **24 September 2026**; the official history showed only v1 at the cutoff.

Theorem 1.2 and Proposition 5.1 give the growth form `deg_i(f^n) ≍ lambda_i^n n^{mu_i}` for surjective endomorphisms of normal projective varieties in arbitrary characteristic, with `mu_i <= 2i(d-i)`. Strict log-concavity forces a zero peripheral polynomial exponent, while equality imposes a discrete-Laplacian constraint. These are substantially stronger statements than the local note's nonoptimal lower/upper bounds. The revised note cites them explicitly and makes no optimal-growth claim. The relevant theorem statements and proof strategy were checked; the present audit does not independently certify that entire 34-page preprint.

### Hu–Jiang, April/May 2026

**Paper:** *A lower bound for polynomial volume growth of automorphisms of zero entropy*.  
**Primary record:** [arXiv:2604.21398](https://arxiv.org/abs/2604.21398).  
**Inspected text:** [v2](https://arxiv.org/html/2604.21398v2), **11 May 2026**; v1 **23 April 2026**.

Definition 3.7 introduces a dynamical intersection polynomial built from products of \(\exp(x_iL)H\), with (L) the nilpotent logarithm of the divisor action. Theorem 3.12 connects its degree with polynomial volume growth; Theorem 1.1 proves sharp lower bounds. Lemma 3.6 records the abelian connection with Tate Jordan blocks.

This is directly relevant recent work on polynomial intersection growth. Its polynomial uses nilpotent logarithms in a zero-entropy setting, whereas the local argument uses the degree of scalar shifts of an endomorphism and exponential spectral scales. The relevant definitions and arguments do not duplicate the local proof as written, but “intersection polynomials control dynamical growth” is already an established research theme.

### Hu's polarized parity paper

**Paper:** *Parity and symmetry of polarized endomorphisms on cohomology*.  
**Verified primary version:** [arXiv:2511.17109v1](https://arxiv.org/html/2511.17109v1), submitted **21 November 2025**; the [official record](https://arxiv.org/abs/2511.17109) showed no later version at the cutoff.

The paper studies polarized self-maps of arbitrary smooth projective varieties, including symmetry of Jordan-block multiplicities. It uses Xie's modulus theorem and hard Lefschetz. It supplies further context for distinguishing eigenvalue pairing, equality of absolute values, and semisimplicity. The local elementary abelian argument does not prove the corresponding assertions for arbitrary varieties or sheaves.

## 5. Classical overlap of the curve proof

Milne's [*The Riemann Hypothesis over Finite Fields*](https://www.jmilne.org/math/xnotes/pRH.pdf), especially Theorem 1.27, Corollary 1.29, and Theorem 1.30, gives the Rosati-positive intersection form and the polarized/Frobenius spectral-circle argument. Kedlaya's [*RH for abelian varieties*](https://kskedlaya.org/weil-cohom/chapter-6.html) gives another accessible account of degree polynomials, Tate faithfulness, and the passage through the Jacobian. Those substantive portions were checked.

The local proof packages positivity directly as

\[
Q_H(u)=\frac{u^*H\cdot H^{g-1}}{H^g},
\]

then views multiplication by a polarized endomorphism as a scaled Euclidean isometry. This removes some intermediate exposition, but its mathematical mechanism and resulting semisimplicity are classical. A power-sum ending is a different presentation of the spectral-radius step, not a strengthening of Weil's theorem.

## 6. Mathematical checks and limits of the present assessment

The following points in the local arguments were checked independently, rather than accepted because a related theorem is known:

1. **Root parity:** the rational degree identity makes the characteristic polynomial nonnegative on a dense subset of the real line. Continuity then gives nonnegativity everywhere, so each real zero has even multiplicity. This does not require a canonical choice of half of the complex roots.
2. **The nef majorization:** the two classes obtained from scalar shifts by (+f^n) and (-f^n) are nef, and their sum is the parallelogram expression. Monotonicity of mixed intersections gives the stated polynomial upper bound. Rational shifts are extended to real shifts by continuity.
3. **Strict gaps:** choosing a scale strictly between adjacent distinct eigenvalue moduli gives a unique dominant term. The product asymptotic gives a lower bound for every sufficiently large iterate, so the argument proves a limit, not just equality of limsups.
4. **Flat blocks:** per-iterate Khovanskii–Teissier log-concavity transfers lower bounds from the block endpoints. Positivity is available for the isogeny case. The zero-eigenvalue extension needs the separate eventual-nilpotence argument supplied in the note.
5. **Numerical comparison:** a numerical cycle space is an equivariant quotient of the subspace of cohomology generated by algebraic cycles. The proof only needs homological triviality to imply numerical triviality; it does not assume the converse or Standard Conjecture D.
6. **Semisimplicity:** the positive quadratic form gives this for the polarized abelian endomorphism. A trace-only sheaf argument cannot provide the same conclusion in general. These are different scopes and should remain separate.

The most defensible publication description is therefore: **a proposed concise alternative proof of known abelian results, with a classical curve specialization and explicit comparison with recent proofs.** It would be premature to describe either note as a new theorem, the shortest available proof, or a completed simplification of the full Weil II theorem.

## 7. Search coverage and limitations

The audit used primary arXiv and Hexagon records, author-hosted texts, and publisher records. Searches included last-week/last-fortnight queries for the new finite-field proof and corrections, recent-quarter queries for abelian dynamical comparison, and targeted older searches for degree-polynomial positivity and Jordan growth. Relevant theorem statements and proof sections were read. Search snippets alone were not used to validate mathematical arguments.

The inspected recent records did not reveal a later version of either November proof or a newly checked independent replacement of its general sheaf argument. Search indexing is incomplete and publication dates can differ from submission, posting, and internal manuscript dates. Inaccessible pages, private circulation, unindexed notes, forthcoming work, and other-language literature remain limitations. There was no exhaustive citation-graph search or consultation with the authors. Accordingly, this report supports careful attribution and correction of scope; it does not certify priority or the absence of further literature.

### Recommended bibliography additions

Add Xie 2412.01216 and Hu–Truong–Xie 2503.09432 to the all-degree note's discussion of proof strategy and current scope. Add Hu 2208.11120 if polynomial/Jordan growth is discussed substantively. Hu–Jiang 2604.21398 and Hu 2511.17109 are useful contextual references, especially in an expanded research version. Retain Hu 1909.12296 as the direct abelian theorem reference and the classical Milne/Kedlaya references for the curve note.
