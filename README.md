# Abelian degree polynomials

Concise alternative proofs of spectral comparison on abelian varieties, with applications to the Riemann hypothesis for curves and global function fields.

## Current papers — start here

**The recommended edition is the two-paper revision of 27 November 2026 ([PR #2](https://github.com/long-mathematics/abelian-degree-polynomials/pull/2)).** These are complementary papers, not successive versions of each other. Neither of the earlier papers is required reading.

| | Current paper | Files |
| --- | --- | --- |
| **Main paper — read first** | **Finite-time spectral comparison on abelian varieties** (4 pages). Rosati positivity, sharp norm bounds, exact Jordan growth, nilpotency, strict-gap constants and composition. | [PDF](papers/abelian_comparison_streamlined.pdf) · [LaTeX](papers/abelian_comparison_streamlined.tex) |
| **Companion — fewer prerequisites** | **Spectral comparison by polynomial interpolation** (3 pages). Actual mixed-degree limits without Rosati or Riemann–Roch, plus a particularly short proof of curve/function-field RH. | [PDF](papers/abelian_comparison_elementary.pdf) · [LaTeX](papers/abelian_comparison_elementary.tex) |

For curve RH alone, read Section 1 of the elementary companion. For the strongest quantitative results, read the main paper. For both approaches, read the current pair above.

**Status:** audited expository proofs of established theorems, with explicit quantitative consequences. The project claims neither a new RH theorem nor priority for its proof methods. Its scope is abelian varieties and curves, not arbitrary-sheaf Weil II. The reviews are AI-assisted, not independent human peer review or formal proof verification.

The two initial notes from [PR #1](https://github.com/long-mathematics/abelian-degree-polynomials/pull/1) are **superseded as recommended reading**. They remain available for historical and alternative-proof comparison; see the [paper index and version history](papers/README.md#historical-notes-superseded). All existing PDF and source URLs are preserved.

## Main results of the current papers

With one Hermitian form compatible with Rosati, the main note proves

$$
\binom gk\delta_k(u)=e_k(t_1,\ldots,t_g),\qquad
\delta_k(u)\le\|\wedge^{2k}u\|\le\binom gk\delta_k(u),
$$

where the squared singular values are $t_1,t_1,\ldots,t_g,t_g$.
The identity is Hu's; the explicit binomial factor is sharp. A quotient of
a finite sum of regular modules supplies the Hermitian form, avoiding a
classification or simple-factor decomposition.

The resulting consequences include actual limits for every endomorphism,
exact exponential-polynomial growth at positive radius, equality of largest
peripheral Jordan sizes on numerical classes and even cohomology, and
equality of nilpotency indices at zero radius. The two latter conclusions
also follow from Hu's published uniform norm comparison. The note gives
the strict-gap leading constant as the norm of the dominant spectral
projection divided by $\binom gk$, and proves the sharp composition bound

$$
\delta_k(uv)\le\binom gk\delta_k(u)\delta_k(v).
$$

The elementary companion uses polynomial coefficient interpolation,
Khovanskii–Teissier, and a bounded block of consecutive traces. Nef
dominance bounds all those future degrees by the present degree. This
proves **actual limits and an every-iterate positive-radius lower bound**
without Rosati, Riemann–Roch, an isogeny hypothesis, or spectral-gap
analysis. Its curve RH specialization uses the single scale
$t_n=2d^{n/2}$ and no trace lemma.

See [the revision audit](audit/streamlined/REVISION.md) for corrections to
the supplied draft, the precise scope of the improvements, and additional
regression checks. In particular, growth estimates involving
$n^{m-1}\rho^n$ are stated only for $\rho>0$; nilpotent actions are
handled separately.

## Prior work and scope

The detailed, version-dated review is in [LITERATURE.md](LITERATURE.md).
The most important overlaps are:

- **Classical Weil–Rosati theory:** Milne's 2015 exposition already includes
  the power-sum/pole argument, Hasse's discriminant argument, and the
  positive-form spectral-circle proof. Semisimplicity in the abelian setting
  is classical too.
- **Fei Hu, J. Algebraic Geometry 33 (2024), 265–293:** Theorem 1.9 is the
  abelian all-codimension comparison; Remark 5.5 already states the odd-degree
  formula. The rational degree identity is Theorem 2.3. Corollary 1.7 and
  equation (5.5) give the mixed-degree/singular-value identity; Corollary 5.6
  gives uniform norm comparison for every self-morphism.
- **Milne, Introduction to Shimura Varieties (2005), Proposition 8.10:**
  the compatible positive-form principle used in the streamlined note is
  classical.
- **Junyi Xie, arXiv:2412.01216v2:** the even comparison holds much more
  generally, for surjective endomorphisms of smooth projective varieties.
  Section 2.5 is a close precedent for the exposed-vertex/concavity strategy;
  its geometric input uses Deligne's weight theorem.
- **Hu–Truong–Xie, arXiv:2503.09432v1:** Lemma 2.2 and the proof of
  Theorem 1.5 give a related scaled maximum/concave-envelope argument.
- **Hu–Jiang, arXiv:2609.29877v1, 24 September 2026:** the polynomial-growth
  estimates are stronger than this note's quantitative byproduct, and apply
  to normal projective varieties in arbitrary characteristic.
- **Hu, arXiv:2610.18094v1, 13 October 2026:** Theorem 1.5 already gives
  exact positive leading asymptotics at strict breaks, with the same
  exponential remainder threshold, in broader rational/meromorphic scope.
- **November 2026 finite-field exposition:** Hexagon 2611.00789v2 and
  Zhang 2611.30749v1 motivated the revisit. Their arbitrary-sheaf theorem has
  broader scope and is not replaced by these abelian arguments.

The original exposed-vertex presentation is retained as a historical alternative; the two current papers are the recommended edition.
The value of these revisions is explicit constants, proofs with stated
prerequisites, and corrected edge cases. The search does not certify
originality or priority.

## Audit and verification

[AUDIT.md](AUDIT.md) records the mathematical checks, corrections, and limits
of verification. Detailed independent AI-assisted readings and the final
source review are in [audit/](audit/).

[scripts/check_identities.py](scripts/check_identities.py) checks exact
integer-matrix realizations on product-polarized powers of elliptic curves.
The recorded run passed **4,399 assertions**, covering 48 distinct matrices,
96 matrix/iterate cases, 672 rational shifts, Jordan growth, and noncommuting
similitudes. See [the guide](audit/exact_checks.md) and
[the actual JSON output](audit/exact_checks.json).

[scripts/check_streamlined.py](scripts/check_streamlined.py) adds exact
regression checks for the sharp composition constant, nilpotent exception,
Jordan growth, strict-gap projector coefficient, and a flat-spectrum
nonconvergence example. Its recorded run passes **117 assertions**, making
**4,516** across both scripts. See its [guide](audit/streamlined/exact_checks.md)
and [recorded output](audit/streamlined/exact_checks.json).

These are normalization and example checks. They are not a formal proof,
external peer review, or computational certification of arbitrary abelian
varieties. The arguments remain ordinary proofs using standard algebraic
geometry. No Lean formalization is included.

## Reproduce the checks and PDFs

Use Python 3.10 or later and a local TeX distribution providing `pdflatex`,
Latin Modern, AMS packages, `mathtools`, `microtype`, `geometry`, `hyperref`,
and `enumitem`. On Debian/Ubuntu, the TeX packages are
`texlive-latex-extra texlive-fonts-recommended lmodern`.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
make check
make pdf
```

To regenerate the exact-check record:

```sh
python scripts/check_identities.py --report audit/exact_checks.json
```

The PDF builder runs local pdfLaTeX with shell escape disabled, repeats passes
until references resolve, and rejects overfull boxes. It writes auxiliary
files under `build/`, updates `papers/*.pdf`, and records source/PDF hashes
in [audit/build_manifest.json](audit/build_manifest.json). It downloads no
TeX resources. PDF bytes can differ across TeX distributions; the manifest
identifies the actual generated files.

The GitHub Actions workflow runs both check scripts and rebuilds all four PDFs (the two current papers and the two historical notes). A
configured workflow is not evidence of a completed remote CI run; see the
actual pull-request checks for that status.

## Provenance and license

Prepared for Christopher D. Long with AI assistance, including parallel
mathematical and literature audits. The notes attribute established results
to their original literature; no independent human referee review is claimed.

Original project files are provided under the [MIT license](LICENSE).
Referenced third-party papers are linked, not redistributed, and retain
their own rights.

