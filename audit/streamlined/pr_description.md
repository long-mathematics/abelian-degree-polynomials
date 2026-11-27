# Prepared revision PR description

This is the reviewable description for the streamlined revision. Actual
remote CI and merge status are recorded on the PR, not inferred from this file.

## Title

Add sharp norm comparison and an elementary proof with actual limits

## Why

The supplied streamlined proof combines useful simplifications but needs a
zero-radius correction and closer attribution. Its all-iterate polynomial
bound fails for nonzero nilpotent actions, and several proposed stronger
consequences already follow from Hu's published uniform norm comparison.
The elementary interpolation proposal can also be improved beyond its
stated limsup conclusion.

## Changes

- Add a four-page main note deriving Hu's finite-time identity with a
  compatible Hermitian form constructed by a free-module quotient.
- Prove the sharp norm sandwich, exact positive-radius Jordan growth,
  nilpotency-index equivalence, a spectral-projection formula at strict
  gaps, and composition with sharp constant `binom(g,k)`.
- Add a three-page elementary companion. A bounded block of consecutive
  traces plus nef dominance gives actual limits for all endomorphisms,
  without Rosati, Riemann–Roch, or gap analysis; the curve argument uses one
  critical scale.
- Correct the nilpotent case, justify absence of internal zeros by ample
  approximation, and specify the `d^(i/2)` polarized cohomological modulus.
- Credit Hu's Corollaries 1.7 and 5.6, Milne's positive-involution principle,
  and the September and October 2026 growth results. Claim no priority.
- Add exact regression examples and extend CI to both scripts and all four
  PDFs. Retain the earlier notes and their historical audit records.

## Validation completed locally

- `make check`: 4,399 original assertions plus 117 new exact assertions,
  totaling 4,516. No floating-point SVD is used.
- All four manuscripts compile with resolved cross-references and no
  overfull boxes. The earlier PDFs remain byte-identical.
- All seven new rendered pages passed visual QA.
- Both final revised sources have independent AI-assisted reviews tied
  to their SHA-256 hashes; no mathematical blocker remains.
- The checks are normalization and example checks, not formal verification
  or external human peer review.

## Remote gate

Run the manuscript/check workflow on the exact PR head and verify the
uploaded Git tree against the locally reviewed tree before merging.
