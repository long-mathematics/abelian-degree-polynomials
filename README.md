# Abelian degree polynomials

Concise expository proofs of classical polarized spectral bounds and the
numerical/cohomological degree comparison for abelian varieties, using degree
polynomials and intersection positivity.

**Status, 27 November 2026:** the mathematical audit found no fatal gap under
the stated standard prerequisites. The theorems are established results, and
the literature contains close precedents for the proof strategy. This project
claims neither a new RH theorem nor historical shortest-proof or method
priority. It does not prove arbitrary-sheaf Weil II.

## Manuscripts

The recommended starting point is the streamlined note. The elementary
companion reaches actual degree-growth limits with fewer geometric inputs.
The two earlier notes remain available for comparison.

| Note | PDF | Editable source |
| --- | --- | --- |
| Finite-time spectral comparison on abelian varieties | [PDF](papers/abelian_comparison_streamlined.pdf) | [LaTeX](papers/abelian_comparison_streamlined.tex) |
| Spectral comparison by polynomial interpolation | [PDF](papers/abelian_comparison_elementary.pdf) | [LaTeX](papers/abelian_comparison_elementary.tex) |
| A quadratic proof of finite-field RH for curves | [PDF](papers/short_curve_rh_proof.pdf) | [LaTeX](papers/short_curve_rh_proof.tex) |
| A degree-polynomial proof of spectral comparison in every codimension on an abelian variety | [PDF](papers/abelian_all_degrees_proof.pdf) | [LaTeX](papers/abelian_all_degrees_proof.tex) |

## Streamlined revision

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

## Earlier arguments

The earlier curve note obtains the classical inequality

$$
|\operatorname{Tr}(u\mid V_\ell A)|^2
\le 4g^2\frac{u^*H\cdot H^{g-1}}{H^g}
$$

from the discriminant of a nef quadratic family. If $f^*H=dH$, iteration
and the classical power-sum lemma give $|\alpha|=\sqrt d$. A second ending
uses the positive quadratic form on the endomorphism algebra to prove
semisimplicity as well. Frobenius on a curve's Jacobian gives curve and
global-function-field RH. This is a compact Weil–Rosati presentation.

The earlier all-codimension note retains the full mixed-degree majorant

$$
0\le P_{f^n}(t)\le
2^g\sum_{j=0}^g\binom gj t^{2(g-j)}\delta_j(n),
\qquad
\delta_j(n)=\frac{((f^n)^*H)^jH^{g-j}}{H^g}.
$$

Choosing $t=2R^n$ between distinct root moduli isolates one growth rate.
Khovanskii–Teissier log-concavity recovers the indices in repeated-modulus
blocks. The resulting known formulas are

$$
\lim_{n\to\infty}\delta_k(n)^{1/n}=\lambda_k=\chi_{2k},
\qquad \chi_{2k+1}=\sqrt{\lambda_k\lambda_{k+1}}.
$$

The note includes a nonoptimal quantitative byproduct, the non-surjective
extension, and bounds for the difference of two maps with a common
polarization. No semisimplicity assumption is used in the comparison proof.

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

The original exposed-vertex presentation is retained, alongside the
classification-free norm proof and the elementary interpolation proof.
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

The GitHub Actions workflow runs both check scripts and rebuilds all four PDFs. A
configured workflow is not evidence of a completed remote CI run; see the
actual pull-request checks for that status.

## Provenance and license

Prepared for Christopher D. Long with AI assistance, including parallel
mathematical and literature audits. The notes attribute established results
to their original literature; no independent human referee review is claimed.

Original project files are provided under the [MIT license](LICENSE).
Referenced third-party papers are linked, not redistributed, and retain
their own rights.

