# Working on these proof notes

- These are expository alternative proofs of established theorems. Preserve
  the explicit attribution to Weil/Rosati, Hu, Xie, and related recent work.
- Do not claim a new RH theorem, a first proof, or historical shortest-proof
  status without a new substantive argument and an adequate literature audit.
- The abelian comparison proof must remain independent of Deligne's weights
  and the dynamical comparison it proves. Numerical cycle classes are used
  as a quotient of algebraic cohomology, not as a presumed injected subspace.
- Edit the sources in `papers/`, then run `make check` and `make pdf`.
  Keep checked-in PDFs synchronized with their TeX sources.
- The exact matrix checks detect constants and normalization errors. They
  are neither a formal verification nor a proof of the general theorems.
- Record substantive mathematical and literature changes in `AUDIT.md` and
  `LITERATURE.md`; date source-version checks explicitly.

- Keep the root README and `papers/README.md` synchronized. Explicitly label
  current main and companion papers separately from historical/superseded
  notes, identify replacements, and preserve existing PDF/source URLs.
