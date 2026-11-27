# Audit of the streamlined elementary proposals

**Date:** 27 November 2026.  **Object reviewed:** the supplied
`upload/abelian_comparison_streamlined.tex`, together with the relayed
Vandermonde-coefficient proposal. This report does not modify the repository
or its manuscripts.

## 1. Findings and recommended arrangement

The attachment's polarized spectral-circle proof and its isogeny proof using
a concave liminf are mathematically sound. The strict-gap assertion can be
strengthened to an exact positive leading constant with a sharp universal
lower bound. The proposed coefficient method is also valid after repairing
its positivity argument. By itself its power-sum conclusion is only a
limsup statement; a short bounded-window lemma upgrades it to actual limits
and a lower bound for every iterate with positive spectral radius.

For a compact note with minimal additional prerequisites, use:

1. The common shifted-degree inequality for a direct critical-scale proof of
   polarized RH.
2. Interpolation of the characteristic polynomial and KT for pointwise trace
   bounds, with an ample-perturbation proof of contiguous positive support.
3. A finite Vandermonde window and nef dominance to obtain every growth
   limit, including non-isogenies, without a spectral-gap argument.
4. The moving-scale argument as an optional refinement giving an explicit
   sharp lower bound for the leading constant at strict gaps.

This arrangement uses neither Rosati nor Riemann--Roch as an additional
argument. The usual degree/characteristic-polynomial identity, exterior
cohomology, intersection theory, and KT remain substantive classical inputs.
No claim of historical proof novelty or shortest-proof status is justified.

## 2. Notation and the basic inequality

Let \(A\) have dimension \(g>0\), let \(H\) be symmetric ample, and let

\[
 P_u(t)=\det(t-u\mid V_\ell A),\qquad
 \delta_j(u)=\frac{(u^*H)^jH^{g-j}}{H^g},\qquad
 M_u(s)=\sum_{j=0}^g\binom gj\delta_j(u)s^{g-j}.
\]

Write \(a_m(u)=\operatorname{Tr}(\bigwedge^m u)\), so

\[
 P_u(t)=\sum_{m=0}^{2g}(-1)^m a_m(u)t^{2g-m}.
\]

For rational \(t=a/b\), set

\[
 X_t=b^{-2}([a]-[b]u)^*H,\qquad
 Y_t=b^{-2}([a]+[b]u)^*H.
\]

They are nef, and \(X_t+Y_t=2(t^2H+u^*H)\). The degree identity and mixed
nef positivity give

\[
 0\le P_u(t)\le 2^gM_u(t^2). \tag{2.1}
\]

Polynomial continuity extends this to every real \(t\). The quadratic
expressions defining \(X_t,Y_t\in N^1(A)_\mathbb R\) likewise remain nef
at real \(t\), by closedness of the nef cone. Degrees of non-isogenies are
understood to be zero.

**Terminology correction:** coefficient extraction uses
\(\lvert P_u(t)\rvert=P_u(t)\). Thus degree nonnegativity is still used.
What the coefficient route avoids is a *separate root-pairing lemma*, not
degree positivity itself.

## 3. The polarized RH argument can be shorter still

Assume \(f^*H=dH\), \(d>0\), and let \(\alpha_1,\ldots,\alpha_{2g}\) be
the characteristic roots. For \(t_n=2d^{n/2}\), (2.1) gives

\[
 P_{f^n}(t_n)\le 2^g(4d^n+d^n)^g=10^g d^{gn}. \tag{3.1}
\]

For every \(\alpha\), including \(|\alpha|=\sqrt d\),

\[
 |2d^{n/2}-\alpha^n|^{1/n}
 \longrightarrow\max(\sqrt d,|\alpha|).
\]

In the equality case this follows from
\(1\le|2-(\alpha/\sqrt d)^n|\le3\); the other cases are immediate.
Taking \(n\)-th roots in (3.1) yields

\[
 \prod_{i=1}^{2g}\max(\sqrt d,|\alpha_i|)\le d^g.
\]

Each factor is at least \(\sqrt d\), so all \(|\alpha_i|\le\sqrt d\).
Finally \(\prod_i|\alpha_i|=\deg f=d^g\), giving equality for every root.

This removes logarithms, forbidden scales, and the subsequent limit
\(x\downarrow\tfrac12\log d\). It also handles zero roots automatically
in the scalar-limit calculation, although polarization itself makes \(f\)
an isogeny. It needs no KT, pairing lemma, trace estimate, or power-sum lemma.
It is the already audited critical-scale method in its simplest real-shift
form, rather than a new theorem. The same calculation gives
\(|\alpha|\le\sqrt d\) from the one-sided hypothesis \(f^*H\preceq dH\).

The argument proves root moduli; semisimplicity requires the additional
positive-form argument. Passing from the Jacobian to a curve still requires
the standard Jacobian identification and zeta/trace-formula facts. It is
safer to choose any ample line bundle defined over \(\mathbb F_q\) and
symmetrize it than to assume that a particular chosen theta divisor is
already defined over \(\mathbb F_q\).

## 4. Repairing the no-internal-zeros assertion

Log-concavity alone does **not** exclude internal zeros: the sequence
\((1,0,0,1)\) is nonnegative and satisfies all adjacent log-concavity
inequalities. The attachment correctly notices this; it should not then
claim that its elementary theorem already covers non-isogenies without
supplying the rest of the argument.

Here is a repair requiring no image-dimension lemma. For any nef \(L\), put

\[
 d_j=\frac{L^jH^{g-j}}{H^g},\qquad
 d_j(\varepsilon)=\frac{(L+\varepsilon H)^jH^{g-j}}{H^g}.
\]

For \(\varepsilon>0\), all \(d_j(\varepsilon)>0\) and KT makes their
logarithms concave. If \(h=\max\{j:d_j>0\}\), interpolation between indices \(0\) and \(h\) gives

\[
 d_j(\varepsilon)\ge d_h(\varepsilon)^{j/h}
 \quad(0\le j\le h).
\]

Passing to \(\varepsilon\downarrow0\) proves \(d_j>0\) for every
\(0\le j\le h\). Thus the positive support is an initial interval, and
the ratios \(d_j/d_{j-1}\) decrease on that interval. When \(h=0\), the
assertion is immediate. This argument distinguishes the geometric
approximation input from bare log-concavity.

Alternatively, for \(L=u^*H\), positivity through the dimension of the
image and vanishing thereafter give the same conclusion. The perturbation
argument is shorter and sufficient for coefficient extraction.

## 5. The coefficient proposal, with all normalizations explicit

For a polynomial \(q\) of degree at most \(2g\), interpolation at any fixed
\(2g+1\) distinct points of \([-1,1]\) gives a constant \(K_g\), depending only on \(g\), such that every coefficient
of \(q\) has modulus at most \(K_g\max_{[-1,1]}|q|\). This is just inversion
of a fixed Vandermonde matrix. For example, equally spaced nodes give the
explicit, deliberately nonoptimal choice

\[
 K_g=\binom{2g}{g}\frac{(2g)^{2g}}{(2g)!}.
\]

Apply this to \(q(x)=P_u(Rx)\), \(R>0\). By (2.1),

\[
 |a_m(u)|\le2^gK_g
 \sum_{j=0}^g\binom gjR^{m-2j}\delta_j(u). \tag{5.1}
\]

Let \(0,\ldots,h\) be the positive support proved in Section 4.

For \(1\le k\le h\), choose

\[
 R^2=\frac{\delta_k}{\delta_{k-1}}.
\]

Decreasing consecutive ratios imply

\[
 R^{2k-2j}\delta_j\le\delta_k
 \quad\text{for every }j.
\]

Consequently, with \(C_g=4^gK_g\),

\[
 |a_{2k}(u)|\le C_g\delta_k(u). \tag{5.2}
\]

For \(0\le k<h\), choose \(R^2=\delta_{k+1}/\delta_k\). The same ratio
calculation yields

\[
 R^{2k+1-2j}\delta_j\le\sqrt{\delta_k\delta_{k+1}},
\]

and hence

\[
 |a_{2k+1}(u)|
 \le C_g\sqrt{\delta_k(u)\delta_{k+1}(u)}. \tag{5.3}
\]

For \(m>2h\), let \(R\downarrow0\) in (5.1): every term tends to zero,
so \(a_m(u)=0\). This handles all zero right-hand sides in (5.2)--(5.3).
The \(k=0\) even case is the identity \(a_0=\delta_0=1\). At \(m=2h\),
the same limit gives the sometimes better bound
\(|a_{2h}|\le2^gK_g\binom gh\delta_h\).

Thus the relayed scaling calculations are correct, including their
binomial factor and the power \(4^g\). Neither \(C_g\) nor the displayed
choice of \(K_g\) should be called optimal.

Applying the usual power-sum limsup identity to
\(a_m(f^n)=\operatorname{Tr}((\bigwedge^m f)^n)\) gives

\[
 \chi_{2k}\le\limsup_n\delta_k(n)^{1/n}\le\chi_{2k},
\]

where the last inequality follows because \(\delta_k(n)\) is a fixed
matrix coefficient on \(H^{2k}\). This proves equality of the limsup, not
yet the existence of the limit. Section 6 supplies the missing upgrade.

## 6. Bounded windows give all the limits without gap analysis

### A finite-dimensional lemma

Let \(T\) be a complex matrix with \(\rho=\rho(T)>0\). Let
\(\beta_1,\ldots,\beta_d\) be its distinct nonzero eigenvalues, with
positive algebraic multiplicities \(m_j\), and set

\[
 p_n=\operatorname{Tr}(T^n)=\sum_{j=1}^d m_j\beta_j^n
 \qquad(n\ge1).
\]

Let \(V=(\beta_j^r)_{0\le r<d,\,1\le j\le d}\). It is invertible.
Writing \(z_n=(m_j\beta_j^n)_j\), we have

\[
 (p_n,\ldots,p_{n+d-1})^{\mathsf T}=Vz_n.
\]

For the induced infinity norm,

\[
 \max_{0\le r<d}|p_{n+r}|
 \ge\frac{\|z_n\|_\infty}{\|V^{-1}\|_\infty}
 \ge\frac{\rho^n}{\|V^{-1}\|_\infty}. \tag{6.1}
\]

No semisimplicity assumption is needed: Jordan blocks do not change the
trace of powers. Constants depend on the fixed spectrum; this is not a
claim of a uniform estimate for varying, coalescing spectra.

### Nef dominance controls a finite forward window

For each fixed \(r\), choose \(B_r>0\) with

\[
 (f^r)^*H\preceq B_rH.
\]

Such a number exists because \(H\) is ample. Pull back by \(f^n\), then
use monotonicity of intersections of nef classes:

\[
 (f^{n+r})^*H\preceq B_r(f^n)^*H,
 \qquad
 \delta_k(n+r)\le B_r^k\delta_k(n). \tag{6.2}
\]

This holds for non-surjective endomorphisms as well.

### Consequence for every codimension

Apply (6.1) to \(T=f^*|H^{2k}\), and (5.2) to \(f^{n+r}\). If
\(\chi_{2k}>0\), then

\[
 \frac{\chi_{2k}^n}{\|V^{-1}\|_\infty}
 \le\max_{0\le r<d}|a_{2k}(f^{n+r})|
 \le C_g\max_{0\le r<d}B_r^k\,\delta_k(n).
\]

Thus there is \(c_k>0\), depending on the fixed \(f,H,k\), such that

\[
 c_k\chi_{2k}^n\le\delta_k(n)
 \le C_k n^{m_k-1}\chi_{2k}^n
 \qquad(n\ge1). \tag{6.3}
\]

The upper bound is ordinary Jordan-form growth of the fixed cohomological
matrix coefficient; \(m_k\) may be the largest peripheral Jordan-block
size. In particular,

\[
 \lim_n\delta_k(n)^{1/n}=\chi_{2k}.
\]

If \(\chi_{2k}=0\), that cohomological operator is nilpotent, so
\(\delta_k(n)=0\) eventually and the same limit is zero. Do **not** assert
the upper bound in (6.3) for every \(n\ge1\) with a zero spectral radius:
a nonzero nilpotent operator can have nonzero early powers.

Finally, \(\delta_k(n)\) is also a matrix coefficient on numerical
classes, so its established limit is at most \(\lambda_k\). Conversely,
the span of algebraic cycle classes in \(H^{2k}\) surjects equivariantly
onto \(N^k(A)_\mathbb Q\otimes\mathbb Q_\ell\): a cohomological relation
has zero intersection with every complementary cycle, and the numerical
intersection pairing is perfect after extension of scalars. Hence

\[
 \chi_{2k}\le\lambda_k\le\chi_{2k}.
\]

No equality of numerical and homological equivalence is assumed.

Equation (5.3) and the power-sum limsup identity now give

\[
 \chi_{2k+1}\le\sqrt{\chi_{2k}\chi_{2k+2}}.
\]

For any ordered list of root moduli, the opposite inequality holds, since

\[
 \frac{\chi_{2k+1}^2}{\chi_{2k}\chi_{2k+2}}
 =\frac{r_{2k+1}}{r_{2k+2}}\ge1
\]

when the denominator is nonzero. If a denominator vanishes, the preceding
upper bound forces the middle radius to vanish as well. Thus one obtains
the odd-degree equality and paired moduli without invoking the separate
parity lemma.

**Conclusion:** the coefficient/window route proves full limits for all
endomorphisms, with no need to analyze positive image dimension, strict
gaps, repeated blocks, or a concave liminf. The positivity repair is used
only in the pointwise coefficient estimate.

## 7. An especially short first-degree version

Write

\[
 (t-u)^*H=t^2H-tB+u^*H.
\]

Intersecting with \(H^{g-1}/H^g\) gives a nonnegative real quadratic
\(t^2-bt+\delta_1(u)\). Its discriminant is nonpositive. Comparing the
coefficient of \(t^{2g-1}\) in the degree polynomial gives
\(\operatorname{Tr}(u)=gb\), so

\[
 |\operatorname{Tr}(u)|^2\le4g^2\delta_1(u). \tag{7.1}
\]

Apply (6.1) to \(f\) on \(H^1\), and use (6.2) with \(k=1\). If
\(\chi_1>0\), this gives

\[
 c\chi_1^{2n}\le\delta_1(n).
\]

The cohomological matrix-coefficient upper bound and the elementary
exterior-power inequality then give

\[
 \chi_1^2\le\liminf_n\delta_1(n)^{1/n}
 \le\limsup_n\delta_1(n)^{1/n}
 \le\chi_2\le\chi_1^2.
\]

Therefore the actual limit is \(\chi_1^2=\chi_2=\lambda_1\). The zero
radius case is eventual vanishing. This version needs no KT and no
coefficient interpolation of degree \(2g\). For a limsup-only statement,
the ordinary power-sum lemma is shorter than the bounded-window lemma.

## 8. Audit of the concave-liminf route and the exact gap constant

For an isogeny, the attachment's steps (a)--(f) are valid. In particular:

- Positive mixed degrees make all logarithms legitimate.
- If \(2\ell_j(n)\ge\ell_{j-1}(n)+\ell_{j+1}(n)\) and the liminfs are
  finite, then \(2L_j\ge L_{j-1}+L_{j+1}\). Its exact endpoint bounds make
  the \(L_j\) finite.
- At a strict gap, every noncentral tilted term has a strictly smaller
  limsup. Together with the lower bound on the maximum, this does imply
  eventual attainment at the central index.
- Concavity fills the affine blocks exactly as asserted.

The prose claiming “no case split” should be softened: the proof still
uses the corners and the affine intervals. Its liminf formulation is a
clean organizational compression, not a removal of that mechanism.

At \(s_k>s_{k+1}\), exactly one indexed eigenvalue product in
\(\bigwedge^{2k}H^1\) has maximal modulus. It includes the entire top
generalized-eigenspace block, so it is algebraically simple even if \(f\)
is not semisimple. Conjugate pairing and even real-root multiplicities
make that eigenvalue

\[
 \mu_k=\prod_{i\le2k}\alpha_i=\chi_{2k}>0.
\]

Let \(\Pi_k\) be its spectral projector on \(H^{2k}\), let
\(v_k=[H^k]\), and let \(\ell_k(w)=w\cdot[H^{g-k}]/H^g\). Then

\[
 c_k=\ell_k(\Pi_kv_k),\qquad
 \delta_k(n)=c_k\chi_{2k}^n+O((\rho_k')^n),
 \quad\rho_k'<\chi_{2k}. \tag{8.1}
\]

Choose \(\rho_k'\) strictly above the other eigenvalue moduli to absorb
their polynomial Jordan factors. A proven lower growth rate excludes
\(c_k=0\), and positivity of \(\delta_k(n)\) excludes \(c_k<0\).
Thus the attachment's exact positive leading-limit claim is correct.

### Symmetrizing the majorant

The same nef expansion gives the stronger pointwise inequality

\[
 P_u(t)+P_u(-t)\le2^gM_u(t^2). \tag{8.2}
\]

Indeed, \(X_t^g+Y_t^g\le(X_t+Y_t)^g\). Its constant \(2^g\) is sharp:
take \(u=[m]\) and \(t=m\ne0\).

At a strict gap, choose \(s_{k+1}<R<s_k\), put \(U_k=\chi_{2k}\), and
use either sign of \(t_n=R^n\). Then

\[
 \frac{P_{f^n}(\pm R^n)}{U_k^nR^{2n(g-k)}}\longrightarrow1.
\]

All noncentral mixed terms are exponentially negligible. Equation (8.2)
therefore gives

\[
 \liminf_n\frac{\delta_k(n)}{U_k^n}
 \ge\frac{2^{1-g}}{\binom gk}.
\]

### KT improves this to the sharp lower constant

The volume-root/Minkowski consequence of KT says

\[
 (X^g)^{1/g}+(Y^g)^{1/g}\le((X+Y)^g)^{1/g}
 \quad(X,Y\text{ nef}).
\]

It follows by interpolation of mixed intersections for ample classes,
then ample approximation; do not infer it from a nonnegative log-concave
sequence without handling possible zeros. Applied to \(X_t,Y_t\), it is

\[
 P_u(t)^{1/g}+P_u(-t)^{1/g}
 \le2M_u(t^2)^{1/g}. \tag{8.3}
\]

At the strict-gap scale both terms on the left have the same leading
asymptotic, while the central mixed term is
\(\binom gk\delta_k(n)R^{2n(g-k)}\). Consequently

\[
 \boxed{\quad c_k
 =\lim_n\frac{\delta_k(n)}{\chi_{2k}^n}
 \ge\binom gk^{-1}>0.\quad} \tag{8.4}
\]

This is sharp: on product-polarized \(E^g\), take \(f\) diagonal with \(k\)
entries \(a\) and (g-k) entries \(b\), where integers \(a>b>0\). Then
\(\delta_k(n)/a^{2kn}\to\binom gk^{-1}\).

Interpolating the normalized lower bounds over a repeated-modulus block

\[
 [a,b]\quad\text{gives}\quad
 \liminf_n\frac{\delta_k(n)}{\chi_{2k}^n}
 \ge\binom ga^{-(b-k)/(b-a)}
       \binom gb^{-(k-a)/(b-a)}
 \ge\binom gk^{-1}.
\]

The last inequality is log-concavity of the binomial coefficients. This
does not assert convergence of the normalized sequence inside a flat
block; nontrivial Jordan growth can make it diverge. For a non-isogeny,
the same moving-scale proof can be run on the eventual positive block,
exposing its final index against the zero roots. The coefficient/window
route avoids that extra bookkeeping.

## 9. Best trace constants, and what is needed to obtain them

The optimal dimension-only constants are

\[
 \boxed{|a_{2k}(u)|\le\binom{2g}{2k}\delta_k(u)},\qquad
 \boxed{|a_{2k+1}(u)|\le\binom{2g}{2k+1}
                 \sqrt{\delta_k(u)\delta_{k+1}(u)}}. \tag{9.1}
\]

They follow from the stronger paired-singular-value model in Route II,
not from the crude Vandermonde constant above. Here is an explicit proof.
Let the singular values be

\[
 x_1,x_1,\ldots,x_g,x_g,\qquad x_j\ge0,
 \qquad\delta_k=\frac{e_k(x_1^2,\ldots,x_g^2)}{\binom gk}.
\]

The trace is bounded by the nuclear norm of the exterior power:
\(|a_m|\le e_m(x_1,x_1,\ldots,x_g,x_g)\). Choose uniformly a subset of
size \(m\) from two labeled copies of each index. Split it into sets of
distinct original indices \(A,B\), of sizes \(\lfloor m/2\rfloor\) and
\(\lceil m/2\rceil\), assigning each repeated index to both and splitting
the single indices uniformly. By permutation symmetry, each marginal
is uniform among subsets of its size. The associated monomial is
\(x_Ax_B\), irrespective of the split. Cauchy--Schwarz gives

\[
 \frac{e_m(x_1,x_1,\ldots,x_g,x_g)}{\binom{2g}{m}}
 \le\sqrt{\frac{e_{\lfloor m/2\rfloor}(x^2)}
                   {\binom g{\lfloor m/2\rfloor}}
             \frac{e_{\lceil m/2\rceil}(x^2)}
                   {\binom g{\lceil m/2\rceil}}}.
\]

This proves (9.1). Positive scalar endomorphisms attain equality, so both
constants are optimal. The \(m=1\) bound is exactly the elementary
quadratic inequality (7.1).

For \(m>1\), this report does not claim a Rosati/RR-free proof of the
sharp constants. One must not silently replace the weaker \(C_g\) by the
sharp binomial constant in the interpolation argument. For illustration,
the pointwise polynomial data

\[
 g=3,\quad(\delta_0,\ldots,\delta_3)=(1,1,1,1),\quad
 P(t)=t^6+24t^4+1
\]

satisfy degree nonnegativity, the monic and constant normalizations,
log-concavity of the single \(\delta\)-sequence, and even the symmetric
majorant (8.2), since

\[
 8(t^2+1)^3-2P(t)
 =6\bigl(t^2(t^2-2)^2+1\bigr)>0.
\]

Nevertheless its second coefficient is \(24>\binom62=15\). These are
not claimed to be realizable geometric data. They show that those
pointwise inequalities alone do not establish the sharp trace constant;
additional structure, such as Route II or stronger consequences of the
nef family, must actually be used.

## 10. What a fixed-eigenbasis argument can and cannot do

An arbitrary matrix coefficient is not a squared norm. Choosing an
eigenbasis does not make the polarization coefficient diagonal and
positive, and nonnormal operators require generalized eigenvectors.
Dropping off-diagonal terms is therefore unjustified without the positive
Hermitian realization and its mixed-degree/singular-value identity.

With that realization, the fixed-basis norm argument is valid and gives
the already stated sharp pointwise spectral bound
\(\chi_{2k}(u)\le\binom gk\delta_k(u)\). That is the stronger Route II,
with its additional prerequisites.

Without those prerequisites, the Vandermonde-window argument is an
elementary replacement for eigenvalue extraction in a fixed basis. It
uses only traces, isolates a maximal eigenvalue over finitely many
consecutive powers, and transfers the bound to the desired iterate by
nef dominance. It really does remove moving scales.

For \(k=1\) there is another legitimate fixed-space argument. The positive
quadratic form
\(Q_H(u)=u^*H\cdot H^{g-1}/H^g\) gives a norm on
\(\operatorname{End}^0(A)\otimes\mathbb R\). On the finite-dimensional
cyclic algebra generated by \(f\), evaluation at any characteristic root
is a bounded linear functional, so
\(|\alpha|^n\le C\sqrt{Q_H(f^n)}\). This gives the first-degree lower
bound directly. It requires the positive-definiteness and faithful
minimal-polynomial transfer to be proved; it does not automatically give
the analogous statement for higher mixed degrees.

## 11. Concrete corrections to the attachment

1. Define \(\log0=-\infty\) in the exponential-scale lemma, or use the
   root-limit formulation of Section 3, which avoids this issue entirely.
2. Keep the explicit ample-perturbation or image-dimension argument for
   contiguous positive support. Bare log-concavity is insufficient.
3. The non-isogeny remark identifies the positivity repair but does not
   itself finish the altered endpoint argument. Either supply that
   argument or use the coefficient/window proof.
4. In the strict-gap expansion, choose the error radius above all
   subdominant moduli to absorb their Jordan polynomials. The claimed
   positive leading constant is otherwise correct, and (8.4) sharpens it.
5. In Route II, Corollary (ii)'s polynomial-times-radius bound for every
   \(n\ge1\) needs \(\chi_{2k}>0\). For zero spectral radius state eventual
   vanishing. A nonzero nilpotent integer Jordan block on \(E^2\) is an
   immediate counterexample to the unsplit statement.
6. Corollary (iii) must say that the action on \(H^i\) is semisimple with
   root modulus \(d^{i/2}\). “The same holds” after the \(H^1\) modulus
   \(\sqrt d\) is ambiguous and is literally false for \(i\ne1\).
7. The stronger route is a finite-dimensional reformulation of classical
   positivity and Hu's singular-value identity. The sharp norm and trace
   consequences should not be advertised as new before a specific
   literature comparison.

## 12. Literature anchors checked in this audit

- F. Hu, *Eigenvalues and dynamical degrees of self-maps on abelian
  varieties*, arXiv:1909.12296v3, 15 March 2022; J. Algebraic Geom. 33
  (2024), 265--293. Theorem 1.1 is the parity theorem, Corollary 1.7 gives
  the mixed-intersection coefficients of the Rosati-square polynomial,
  and equation (5.5) gives the singular-value expression used in Route II.
  Its proof of Corollary 1.7 explicitly invokes RR.
  <https://arxiv.org/pdf/1909.12296>
- J. S. Milne, *The Riemann Hypothesis over Finite Fields: From Weil to the
  Present Day*, 2015. Page 2, footnote 1 already gives the power-sum/pole
  extraction argument; page 3 gives the discriminant argument for elliptic
  curves. These ingredients should be attributed to their classical
  history, not to the recent short Weil-II proof.
  <https://www.jmilne.org/math/xnotes/pRH.pdf>
- F. Hu and C. Jiang, *Uniform Turán estimates and sharp bounds for degree
  and mixed orbit growth*, arXiv:2609.29877v1, 24 September 2026. Theorem
  1.2 and Proposition 5.1 provide broader and stronger degree-growth
  results. The elementary fixed-spectrum window estimate above is not a
  claim to improve their uniform Turán theorem.
  <https://arxiv.org/pdf/2609.29877>

These checks establish overlap and attribution boundaries, not an
exhaustive priority search for the exact presentation proposed here.
