# Final PDF visual review

Date: 27 November 2026.

All seven final page images were inspected directly with the image-viewing tool, in batches of at most two images. The inspected renders are in build/qa/streamlined/: main-1.png through main-4.png and elementary-1.png through elementary-3.png. The final elementary renders were rechecked after shortening the scope paragraph.

## Identified final PDFs

| PDF | Pages | SHA-256 |
| --- | --- | --- |
| papers/abelian_comparison_streamlined.pdf | 4 | aa80e30ac85e0bf5a965127bd4cf96580bf9ae5b00a5c1ad1417a3e5a23e8159 |
| papers/abelian_comparison_elementary.pdf | 3 | b01eb0621dbf4ff706b945b762aef4216e4b39e14119ff4d1883c25055e4eb6d |

Page counts and these file hashes were read from the final local PDFs. No source or PDF was edited or rebuilt by this reviewer.

## Page-by-page observations

| Render | Visual observations |
| --- | --- |
| Main, page 1 | The two-line title, author/date, abstract, first section, definitions, and start of the Hermitian-form proof are readable. Equations (1)–(3), fractions, subscripts, dagger notation, and numerical-class notation are complete and stay inside the text area. The proof continues naturally on the following page. |
| Main, page 2 | The end of the Hermitian proof, Theorem 2, and the dynamics section have consistent spacing. The final explicit index range in Theorem 2 is visible. Norm bars, exterior-power notation, the growth estimate, and the equivalence chain (7) render correctly; equation numbers do not collide with formulas. The concluding paragraph fits above the footer. |
| Main, page 3 | The zero-radius remark, strict-gap projection formula, and composition inequality are legible and unclipped. Equation (8), its remainder threshold, and the proof-ending squares are placed cleanly. Section 4 begins with several lines of text before continuing on page 4; the heading is not stranded. |
| Main, page 4 | The continuation of Section 4, square-root bounds in (10), provenance paragraph, and all five references are complete. Long URLs wrap inside the margins. The remaining lower-page white space is ordinary final-page space, with no apparent truncation. |
| Elementary, page 1 | The long title fits on one line. The abstract, input list, nef-majorant formula, and polarized corollary are clearly separated. Sums, products, roots, and equation labels are readable. The final application paragraph and page number are intact. |
| Elementary, page 2 | The explicit index ranges in Lemma 3 and Theorem 5 are visible. The coefficient estimate, trace-detection display, and limit formulas fit cleanly. The section transition has adequate following text. The proof ends this page after a complete displayed inequality and continues normally on page 3. |
| Elementary, page 3 | Equation (7) opens the continued proof cleanly. The numerical-quotient discussion, shorter first-degree argument, trace inequality, and limit chain are readable. The shortened scope paragraph and all four references fit on this page, with wrapped URLs inside the margins and clear separation from the footer. No fourth references page remains. |

## Result and scope

**Visual QA passed for all seven final pages.** No clipped text or formulas, overlapping elements, missing-glyph placeholders, broken equation fences, unresolved citation markers, or unresolved cross-reference markers were visible. Typography and margins are consistent, page numbers are sequential, and the final pagination is four pages plus three pages.

This report records visual rendering and pagination observations only. It does not certify mathematical correctness, literature attribution, or the build process; those are addressed by the separate source and build records.
