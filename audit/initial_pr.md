# Prepared initial pull-request description

This is the reviewable description prepared for the initial manuscript PR.
Its presence does not indicate that a remote repository or PR already exists.

## Title

Add audited degree-polynomial proof notes and reproducible checks

## Why

The initial drafts need explicit hypotheses, accurate attribution, and
reproducible sources before circulation. The literature review identifies
classical precedents for the curve argument, Hu's established abelian
comparison theorem, close scaling/concavity precedents, and stronger recent
quantitative growth results. The repository should present the notes as
concise expository proofs of known results.

## Changes

- Add the three-page curve RH note and four-page all-codimension comparison
  note, with editable LaTeX and synchronized PDFs.
- Clarify endomorphism, Frobenius, numerical-equivalence, and minimal-polynomial
  conventions; acknowledge all identified theorem and method overlap.
- Add a dated primary-source literature review through 27 November 2026,
  mathematical audit reports, and a final source review.
- Add exact SymPy checks, a local PDF build script, a Makefile, and a CI
  workflow that reruns checks and compiles the manuscripts.
- Document the standard prerequisites and the limits of the verification.

## Validation completed locally

- 4,399 exact assertions passed, covering 48 matrices, 96 iterate cases,
  672 rational shifts, Jordan growth, and noncommuting similitudes.
- Both PDFs compiled with local pdfLaTeX, with resolved cross-references and
  no overfull boxes; source and PDF hashes are recorded.
- All seven rendered pages passed direct visual inspection.
- Independent AI-assisted mathematical readings and the final revised-source
  review found no fatal gap under the stated prerequisites.
- `git diff --check` passed.

## Scope and limitations

These are expository alternative proofs. No new RH theorem, method-priority
claim, external peer review, or formal proof certification is asserted.
The quantitative byproduct is weaker than Hu–Jiang's September 2026 theorem.
Remote CI status must be checked on the actual PR before merge.
