# Final mathematical review: elementary companion

**Reviewed:** 27 November 2026.

**Source:** papers/abelian_comparison_elementary.tex

**SHA256 of the exact reviewed bytes:**

    3e7207f26810e88406a92f8fcd27fbd18616e900a570d13dbe83c1be95c94b7e

**Assessment:** No mathematical blocker found in the reviewed source. The
proof establishes actual mixed-degree limits for arbitrary group
endomorphisms, including non-isogenies, from the stated classical inputs.
This is a mathematical source review, not a formal verification, an
exhaustive literature audit, or PDF visual QA.

## Checks and conclusions

1. **Nef majorant and critical scale.** The degree identity, now explicitly
   accompanied by the top-intersection formula, correctly identifies
   \(X^g/H^g\) with \(P_u(t)\). The cube and mixed nef positivity give the
   majorant, and rational density justifies real shifts. At
   \(t_n=2d^{n/2}\), the bound is exactly \(10^g d^{gn}\). The factor limit
   also holds when \(|\alpha|=\sqrt d\), because its normalized modulus is
   between 1 and 3. The determinant then forces equality of all root
   moduli. No trace, KT, or prior pairing argument is used in this part.

2. **Coefficient extraction.** Interpolation at fixed nodes gives a constant
   depending only on \(g\). Dividing by \(R^{2g-m}\) produces precisely the
   exponent \(R^{m-2j}\) in equation (4). The two choices of \(R^2\) correctly
   bound the individual summands by \(\delta_k\) and
   \(\sqrt{\delta_k\delta_{k+1}}\), respectively. Summing the binomial
   weights justifies \(C_g=4^gK_g\).

3. **Positive support and boundary indices.** The ample perturbation
   \(u^*H+\varepsilon H\) repairs the internal-zero issue: its positive
   log-concave mixed degrees interpolate between 0 and \(h\), and the
   limit proves positivity at every earlier index. The ratio argument is
   therefore legitimate. The proof treats \(h=0\), \(m=0\), the last
   positive even index \(m=2h\), and all indices \(m>2h\) correctly. For
   \(m=2h\), the surviving constant \(2^gK_g\binom gh\) is at most \(C_g\).

4. **Bounded-window detection.** The matrix
   \((\beta_j^r)_{0\le r<d,\,1\le j\le d}\) is invertible for distinct
   nonzero eigenvalues. Inverting it bounds the largest
   \(a_j\beta_j^n\) by a fixed multiple of the largest trace in the window.
   Positive algebraic multiplicities guarantee the former is at least
   \(\rho^n\). Jordan blocks do not alter traces of powers, and zero
   eigenvalues contribute nothing for \(n\ge1\). Constants depend on the
   fixed spectrum, as the statement permits.

5. **Transporting the window to one iterate.** Ampleness gives
   \((f^r)^*H\preceq B_rH\) for each of the finitely many shifts.
   Pullback preserves nefness for non-surjective morphisms too.
   Intersecting the pulled-back inequality gives
   \(\delta_k(f^{n+r})\le B_r^k\delta_k(f^n)\), with the exponent \(k\)
   correct. Equations (3) and (5) consequently give the lower bound in
   (7) for every \(n\ge1\), not merely for a subsequence.

6. **Actual limits and zero spectral radius.** The lower bound and the
   fixed cohomological matrix-coefficient upper bound give the full
   \(n\)-th-root limit when the radius is positive. A zero radius is
   handled separately by nilpotence and eventual vanishing; the source
   does not incorrectly assert a zero-radius exponential bound for
   nonzero early powers. The endpoints \(k=0\) and \(k=g\) are consistent
   with the same argument.

7. **Numerical comparison and odd degrees.** The numerical matrix
   coefficient gives one inequality. The cycle-class span surjects onto
   numerical classes after scalar extension, because pairing with a
   complementary numerical dual basis detects every numerical
   coordinate. This gives the opposite inequality without assuming
   numerical classes inject into cohomology. For positive odd radius,
   the same window argument uses the factor \(B_r^{k+1/2}\) from the
   geometric-mean trace bound, which disappears under \(n\)-th roots.
   The newly explicit zero-odd-radius clause handles that case directly.
   Ordered root products give the reverse odd inequality, including the
   zero tail, and hence paired moduli.

8. **First-degree specialization.** The corrected wording now gives a
   nonpositive discriminant for the nonnegative quadratic. Comparing the
   degree-polynomial coefficient yields
   \(|\operatorname{Tr}u|^2\le4g^2\delta_1(u)\). The window lemma on
   \(H^1\), followed by nef dominance, gives
   \(\delta_1(f^n)\ge c\chi_1^{2n}\). Every inequality in the closing
   chain is valid, and nilpotence handles \(\chi_1=0\). KT and the
   higher-coefficient lemma are unnecessary for this
   specialization.

## Final clarifications and scope

The frozen source explicitly states the even index ranges in the
coefficient lemma and comparison theorem, restricts the odd formula to
\(k<g\), and says that the companion proves its stronger norm and Jordan
conclusions using its extra inputs. These address the earlier
presentation observations.

The first limited change check reversed exactly those four textual
clarifications in memory and recovered the previously reviewed SHA256:

    acf5a45923594ff94cd77545cc8f91cc5612ab9ef1ebf894eee20b95d507a116

The final editorial change check reversed exactly two changes: moving the
MilneRH citation to the curve application, and shortening the final
scope/provenance paragraph. This recovered the intermediate reviewed
SHA256:

    5e5a8bde5cd6a157086a8ec09425111b53444ec1c9991f562e8dc4aea88c7894

Thus no other source changes intervened, and the proofs are unchanged.
The mathematical assessment above applies to the frozen source whose
SHA256 heads this review; no full reaudit or additional tests were needed
for these clarifications and editorial changes.

The historical discussion removed from the short source remains an audit
qualification: Milne's 2015 RH survey, page 2, footnote 1, records the
classical power-sum/pole argument. Deligne's trace/log-determinant identity
is related, but this review makes no verified priority claim for the exact
pole lemma. The elementary companion uses its finite-window proof instead.

The proof explicitly acknowledges degree nonnegativity and does not
claim that it has removed that input. The separation between spectral
moduli and the additional semisimplicity argument is also appropriate.
No theorem-priority or proof-priority conclusion follows from this review.

No source edits were made by this reviewer.
