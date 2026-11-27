# Paper index and version history

## Current edition (27 November 2026)

**Three complementary papers, in order of scope rather than chronology.** All three prove RH for smooth projective curves over finite fields (and thus global function fields) and the Frobenius eigenvalue moduli on all cohomological degrees of abelian varieties. The longer papers are stronger in other respects.

| Role | Title | RH scope and extra results | PDF | Source |
| --- | --- | --- | --- | --- |
| **I — shortest standalone RH proof** | A single-scale proof of the Riemann hypothesis for curves over finite fields (1 page) | Full curve/function-field RH via polarized spectral circle; no semisimplicity or dynamical-degree comparison. | [Read PDF](curve_rh_single_scale.pdf) | [LaTeX](curve_rh_single_scale.tex) |
| **II — elementary generalization** | Spectral comparison by polynomial interpolation (3 pages) | Same curve RH, plus actual mixed-degree limits and even/odd spectral comparison for arbitrary endomorphisms, without Rosati or RR. | [Read PDF](abelian_comparison_elementary.pdf) | [LaTeX](abelian_comparison_elementary.tex) |
| **III — strongest main research paper** | Finite-time spectral comparison on abelian varieties (4 pages) | Same curve RH, plus polarized semisimplicity and the sharp finite-time, Jordan-growth, nilpotency, strict-gap and composition results. | [Read PDF](abelian_comparison_streamlined.pdf) | [LaTeX](abelian_comparison_streamlined.tex) |

Read I for RH alone, II for a broader elementary proof with Khovanskii–Teissier and interpolation, and III for the strongest results with classical Rosati and Riemann–Roch inputs. Paper I extracts Section 1 of II into a self-contained exposition relative to the standard abelian/Jacobian facts. Papers II and III originated in [PR #2](https://github.com/long-mathematics/abelian-degree-polynomials/pull/2), merged at [47ddf69](https://github.com/long-mathematics/abelian-degree-polynomials/commit/47ddf698c2f9fda01c6a5f7ff6130a588fec02eb). None treats arbitrary-sheaf Weil II or number-field RH. There is no claim to historical shortest-proof status.

The [revision audit](../audit/streamlined/REVISION.md), [standalone extraction audit](../audit/curve_rh_single_scale.md), and [literature review](../LITERATURE.md) document the scope and provenance. The [build manifest](../audit/build_manifest.json) identifies all source/PDF pairs by hash.

## Historical notes (superseded)

The following **earlier notes are not the recommended edition**. They were introduced in [PR #1](https://github.com/long-mathematics/abelian-degree-polynomials/pull/1), merged at [767d95d](https://github.com/long-mathematics/abelian-degree-polynomials/commit/767d95d1409ecfd9a1b2a53ed49bdf71d8deee42). They are preserved in place so old links and audit records remain valid.

| Earlier note | Historical files | Recommended replacement |
| --- | --- | --- |
| A quadratic proof of finite-field RH for curves (3 pages) | [PDF](short_curve_rh_proof.pdf) · [LaTeX](short_curve_rh_proof.tex) | [Paper I](curve_rh_single_scale.pdf) for curve RH; [Paper II](abelian_comparison_elementary.pdf) for the trace approach and comparison; [Paper III](abelian_comparison_streamlined.pdf) for semisimplicity. |
| A degree-polynomial proof of spectral comparison in every codimension on an abelian variety (4 pages) | [PDF](abelian_all_degrees_proof.pdf) · [LaTeX](abelian_all_degrees_proof.tex) | [Main paper](abelian_comparison_streamlined.pdf) for sharp bounds and growth; [elementary companion](abelian_comparison_elementary.pdf) for actual limits without gap analysis. |

The historical notes retain the initial discriminant, power-sum and moving-scale/exposed-vertex arguments. Their superseded status is editorial: the later papers give the recommended, streamlined presentations and more precise conclusions. It is not a retraction of the earlier arguments. See the [original audit](../AUDIT.md) and the [revision audit](../audit/streamlined/REVISION.md) for their respective scopes.

## Maintenance

Keep this index and the root README synchronized when adding or replacing a paper. Explicitly label each paper as current standalone RH, current elementary generalization, current strongest main paper, or historical/superseded, and identify its replacement where applicable. Preserve stable file links and audited PDF/source pairs.
