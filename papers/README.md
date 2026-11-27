# Paper index and version history

## Current edition (27 November 2026)

The following **two papers are current**. They were introduced in [PR #2](https://github.com/long-mathematics/abelian-degree-polynomials/pull/2), merged at [47ddf69](https://github.com/long-mathematics/abelian-degree-polynomials/commit/47ddf698c2f9fda01c6a5f7ff6130a588fec02eb).

| Role | Title | PDF | Source |
| --- | --- | --- | --- |
| **Main paper** | Finite-time spectral comparison on abelian varieties (4 pages) | [Read PDF](abelian_comparison_streamlined.pdf) | [LaTeX](abelian_comparison_streamlined.tex) |
| **Elementary companion** | Spectral comparison by polynomial interpolation (3 pages) | [Read PDF](abelian_comparison_elementary.pdf) | [LaTeX](abelian_comparison_elementary.tex) |

Read the main paper for the strongest finite-time and Jordan-growth conclusions. Read the companion for the curve RH proof and comparison with fewer geometric prerequisites. These two papers are complementary and neither supersedes the other.

The [revision audit](../audit/streamlined/REVISION.md) and [literature review](../LITERATURE.md) explain the improvements and prior work. The [build manifest](../audit/build_manifest.json) identifies all four source/PDF pairs by hash.

## Historical notes (superseded)

The following **earlier notes are not the recommended edition**. They were introduced in [PR #1](https://github.com/long-mathematics/abelian-degree-polynomials/pull/1), merged at [767d95d](https://github.com/long-mathematics/abelian-degree-polynomials/commit/767d95d1409ecfd9a1b2a53ed49bdf71d8deee42). They are preserved in place so old links and audit records remain valid.

| Earlier note | Historical files | Recommended replacement |
| --- | --- | --- |
| A quadratic proof of finite-field RH for curves (3 pages) | [PDF](short_curve_rh_proof.pdf) · [LaTeX](short_curve_rh_proof.tex) | [Elementary companion](abelian_comparison_elementary.pdf), Section 1 for the short polarized proof and the final first-degree argument for the trace approach; [main paper](abelian_comparison_streamlined.pdf) for semisimplicity. |
| A degree-polynomial proof of spectral comparison in every codimension on an abelian variety (4 pages) | [PDF](abelian_all_degrees_proof.pdf) · [LaTeX](abelian_all_degrees_proof.tex) | [Main paper](abelian_comparison_streamlined.pdf) for sharp bounds and growth; [elementary companion](abelian_comparison_elementary.pdf) for actual limits without gap analysis. |

The historical notes retain the initial discriminant, power-sum and moving-scale/exposed-vertex arguments. Their superseded status is editorial: the later papers give the recommended, streamlined presentations and more precise conclusions. It is not a retraction of the earlier arguments. See the [original audit](../AUDIT.md) and the [revision audit](../audit/streamlined/REVISION.md) for their respective scopes.

## Maintenance

Keep this index and the root README synchronized when adding or replacing a paper. Explicitly label each paper as current main, current companion, or historical/superseded, and identify its replacement where applicable. Preserve stable file links and audited PDF/source pairs.
