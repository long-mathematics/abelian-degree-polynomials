# Audit of the streamlined Rosati route and proposed refinements

Date: 27 November 2026.

Source reviewed: upload/abelian_comparison_streamlined.tex

Source SHA-256:

    4e9f92ec8f85bc5736cbe877670e576d19ab12a9f78ab0708abf1619e628603e

No repository or external resource was modified. This audit concentrates on Route II and the proposed quantitative consequences; it does not repeat the earlier curve audit.

## 1. Verdict and corrections required

**The Hermitian trace-form construction, the Riemann–Roch determinant identity, and the sharp norm sandwich are mathematically sound.** They give the proposed equality of the largest peripheral Jordan-block sizes when the spectral radius is positive, and equality of nilpotency indices when it is zero. The two further refinements sent during review—the sharp submultiplicativity constant and the explicit strict-gap leading coefficient—are also valid.

The submitted text nevertheless needs these corrections or explicit qualifications:

1. **Corollary (ii), the displayed polynomial upper bound, is false when the spectral radius is zero.** Its positive-radius and nilpotent cases must be stated separately. The symbol \(m\) also needs its precise definition as the largest Jordan-block size at the spectral radius of the even cohomological action.

2. **Corollary (iii) must state modulus \(d^{i/2}\) on \(H^i\).** The present words “all roots of modulus \(\sqrt d\), and the same holds on every \(H^i\)” literally suggest the wrong modulus outside degree one. Semisimplicity holds in every degree; the modulus changes with the degree.

3. **Make the polarization and quasi-endomorphism conventions explicit.** Take \(H\) to be the class of a symmetric ample line bundle, or an ample rational divisor after scaling. The determinant/degree identity must extend to \(\operatorname{End}^0(A)\), since \(u^\dagger u\) need not be integral. If divisor equalities are numerical, say that the usual map \(L\mapsto\varphi_L\) descends to numerical divisor classes with rational coefficients on an abelian variety. Under that convention the assertion \(f^\dagger f=d\) is justified.

4. For statements involving logarithms and non-isogenies, adopt \(\log 0=-\infty\). Give non-isogenies degree zero, as in the earlier manuscript.

5. The proposed Jordan and nilpotency comparisons are **consequences of already established stronger norm comparisons**, notably Hu, Corollary 5.6. They should be presented as consequences newly made explicit in this exposition, without a theorem-priority claim.

None of these corrections undermines the Route II mechanism.

## 2. Hermitian structure: no hidden classification step

Write \(B=\operatorname{End}^0(A)\) and let \(\tau\) denote the Tate-module trace. The stipulated identities imply that

\[
b(a,c)=\tau(a^\dagger c)
\]

is a symmetric rational bilinear form with \(b(a,a)>0\) for every nonzero rational \(a\).

The argument passing to \(B\otimes_{\mathbb Q}\mathbb R\) is correct. Density first gives positive semidefiniteness. A singular rational Gram matrix has a nonzero rational kernel vector; consequently the real form is positive definite. Complexification, with conjugate-linear extension of \(\dagger\), gives the positive Hermitian form

\[
\langle x,y\rangle=\tau(x^*y).
\]

Left multiplication satisfies \(L_x^*=L_{x^*}\). Its faithfulness is automatic from \(L_x(1)=x\). If \(r\) belongs to the Jacobson radical, then \(r^*r\) also belongs to the radical and is nilpotent. The operator \(L_{r^*r}\) is self-adjoint and nilpotent, hence zero. Faithfulness and positivity give \(r=0\). Thus the complex algebra is semisimple.

Every finite-dimensional simple module over this complex semisimple algebra is isomorphic to a minimal left ideal. Such an ideal is invariant under every left multiplication and its adjoint. Restricting the regular Hermitian form, transporting it to the simple summands of \(V\), and taking their orthogonal sum gives the asserted form on \(V\).

This is ordinary finite-dimensional semisimple-algebra theory, not Albert classification. It works for the abstract, generally discontinuous embedding of the coefficient field into \(\mathbb C\). It does not compare the regular trace with the Tate trace; it uses the Tate trace throughout. Finite dimensionality of \(B\), rationality and cyclicity of \(\tau\), and Rosati positivity are indispensable inputs.

## 3. Riemann–Roch identity and singular-value pairing

For an integer \(s\ge1\), \(L=sH+u^*H\) is ample, and

\[
\varphi_L=\varphi_H\circ(s+u^\dagger u).
\]

Extend degree to rational quasi-isogenies in the usual homogeneous way. Multiplicativity, the Tate determinant formula, and Riemann–Roch give

\[
\frac{\deg\varphi_L}{\deg\varphi_H}
=\det(s+u^\dagger u\mid V_\ell A)
=\left(\frac{L^g}{H^g}\right)^2.
\]

The factorials in \(\deg\varphi_L=(L^g/g!)^2\) cancel. Equality at the positive integers proves the polynomial identity

\[
M_u(s)^2=\det(s+U^*U).
\]

It applies to singular \(u\) as well. Positivity of \(U^*U\) and the fact that the right side is a square force every squared singular value to have even multiplicity. Since \(M_u\) is monic,

\[
M_u(s)=\prod_{j=1}^g(s+\tau_j),
\qquad
\binom gk\delta_k(u)=e_k(\tau_1,\ldots,\tau_g).
\]

There is no missing factorial, square root, or reciprocal in this normalization.

## 4. The sharp sandwich and exact vanishing

Fix the single Rosati-compatible Hermitian form constructed above and its induced exterior norms. Set

\[
B_k=\binom gk,\qquad T_k=\bigwedge^{2k}U.
\]

The paired singular values give

\[
\|T_k\|=\tau_1\cdots\tau_k.
\]

Because the largest summand of \(e_k(\tau)\) is this product and there are \(B_k\) summands,

\[
\delta_k(u)\le\|T_k\|\le B_k\delta_k(u).
\]

Both constants are sharp uniformly over abelian varieties: equal singular values attain the first inequality, and a rank-\(k\) scalar projection on a product-polarized \(E^g\) attains the second. The resulting spectral bound \(\chi_{2k}(u)\le B_k\delta_k(u)\) is therefore correct.

For any endomorphism, with no invertibility assumption,

\[
\delta_k(u)=0
\iff \bigwedge^{2k}U=0
\iff \operatorname{rank}U<2k
\iff \dim u(A)<k.
\]

The action on numerical classes is zero under exactly the same condition: one direction follows from the numerical quotient of algebraic cohomology; the other follows by applying that action to \(H^k\) and pairing with \(H^{g-k}\).

## 5. Gemini's Jordan and nilpotency proposals

Let \(T\) be the degree-\(2k\) cohomological operator and \(S\) the numerical codimension-\(k\) operator, after complex scalar extension. The transpose identification with the Tate exterior representation preserves the spectrum, Jordan sizes, and an appropriately induced operator norm.

### Positive spectral radius

Let \(\rho=\rho(T)>0\), and let \(m\) be the largest Jordan-block size among eigenvalues of \(T\) of modulus \(\rho\). Elementary Jordan theory gives constants \(c,C>0\) with

\[
c\,n^{m-1}\rho^n\le\|T^n\|\le C\,n^{m-1}\rho^n
\]

for all \(n\ge1\), after absorbing finitely many initial indices. The sandwich therefore proves

\[
\boxed{\delta_k(f^n)\asymp n^{m-1}\rho^n.}
\]

Gelfand's formula and the numerical matrix coefficient/quotient argument give \(\rho(S)=\rho(T)\). If \(m'\) denotes the corresponding largest peripheral Jordan size of \(S\), the quotient gives \(m'\le m\). On the other hand, \(\delta_k(f^n)\) is a fixed matrix coefficient of \(S^n\), so

\[
\delta_k(f^n)\le C' n^{m'-1}\rho^n.
\]

Together with the preceding lower bound, this forces \(m\le m'\). Hence

\[
\boxed{m=m'.}
\]

The action on the span of algebraic cohomology classes has the same maximum peripheral Jordan size, by placing it between the two operators.

A further correct consequence is that the **positive real number \(\rho\) itself has a Jordan block of this maximal size** on both numerical and even cohomological realizations. For example, the rational generating function \(\sum_n\delta_k(f^n)t^n\), together with positivity and the two-sided growth estimate, has a pole of order \(m\) at \(t=1/\rho\). This forces the indicated block at the positive eigenvalue.

### Zero spectral radius

If \(\rho(T)=0\), then \(T\) is nilpotent. For every \(n\ge1\),

\[
T^n=0
\iff \delta_k(f^n)=0
\iff S^n=0.
\]

Consequently their nilpotency indices are equal, with the convention that the zero operator has index one. More geometrically, when this index is finite it equals

\[
\min\{n\ge1:\dim f^n(A)<k\}.
\]

This proves the proposed nilpotency statement, including non-surjective maps.

The submitted polynomial estimate with \(\rho=0\), however, is false at the earlier nonzero iterates. On \(A=E^2\), with product polarization, take

\[
f(x,y)=(y,0),\qquad k=1.
\]

Then \(f^2=0\), \(\chi_2(f)=0\), but \(\delta_1(f)=1/2\). Thus no inequality \(\delta_1(f)\le C\,1^{m-1}0^1\) is possible. State the sandwich for every iterate, the polynomial estimate only for \(\rho>0\), and eventual exact vanishing separately.

### What this does not prove

Equality concerns the **maximum** peripheral block size, not the entire peripheral spectrum or all Jordan blocks with multiplicities. For example, let \(A=E_1\times E_2\) over \(\mathbb C\), with nonisogenous elliptic curves and \(E_2\) admitting multiplication by \(i\). For \(f=\mathrm{id}\times[i]\), the action on \(\mathsf N^1(A)\) is the identity, but the cross term in \(H^2(A)\) has eigenvalues \(i\) and \(-i\). All these eigenvalues are peripheral.

Likewise, the symbol \(\asymp\) cannot generally be strengthened to convergence of the normalized degree sequence. On \(E^2\) take the integer matrix

\[
F=\begin{pmatrix}1&1\\0&-1\end{pmatrix}.
\]

Here \(F^2=I\), \(\rho=1\), and \(m=1\), but the product-polarized sequence \(\delta_1(f^n)\) alternates between \(3/2\) and \(1\).

## 6. Sharp submultiplicativity

The proposed improvement

\[
\boxed{\delta_k(uv)\le \binom gk\,\delta_k(u)\delta_k(v)}
\]

is valid without commutativity.

Let \(a_j\) be the paired squared singular values of \(UV\), and put \(b_j=\tau_j(U)\tau_j(V)\). Both sequences are decreasing. Exterior-power norm submultiplicativity gives every partial-product inequality

\[
\prod_{j=1}^r a_j\le\prod_{j=1}^r b_j,\qquad 1\le r\le g.
\]

Thus \(a\) is weakly log-majorized by \(b\). For positive entries the function

\[
(x_1,\ldots,x_g)\longmapsto e_k(e^{x_1},\ldots,e^{x_g})
\]

is symmetric, convex, and coordinatewise increasing. These three properties, not Schur convexity alone, justify passage from weak log-majorization to \(e_k(a)\le e_k(b)\). Finally,

\[
e_k(b)
=\sum_{|I|=k}\prod_{i\in I}\tau_i(U)\tau_i(V)
\le e_k(\tau(U))e_k(\tau(V)).
\]

Dividing by \(B_k\) gives the claimed constant \(B_k\), rather than \(B_k^2\).

Zeros cause no problem. Within the abelian setting, first extend the inequality homogeneously to rational quasi-endomorphisms, replace \(u,v\) by \(u+\varepsilon\,1,v+\varepsilon\,1\) with rational \(\varepsilon\to0\) avoiding their finitely many singular parameters, and pass to the limit. This perturbation stays in the same algebra with the same Hermitian form. Alternatively, weak log-majorization has the same continuous extension to nonnegative vectors.

Take \(u=aP\) and \(v=bP\), with \(P\) the same rank-\(k\) product projection on \(E^g\) and \(a,b\ne0\). Then

\[
\delta_k(u)=a^{2k}/B_k,\quad
\delta_k(v)=b^{2k}/B_k,\quad
\delta_k(uv)=(ab)^{2k}/B_k.
\]

Equality proves sharpness of the submultiplicativity constant.

## 7. Exact leading constant at a strict gap

Suppose \(s_k>s_{k+1}\) and \(\chi=\chi_{2k}>0\). For \(T=\bigwedge^{2k}U\), the product of the top \(2k\) roots is the unique eigenvalue of modulus \(\chi\), is simple, and is the positive number \(\chi\). Let \(\Pi\) be its spectral projection. Then

\[
\chi^{-n}T^n\longrightarrow\Pi
\]

in operator norm. Write \(\tau_j(n)\) for the paired squared singular values of \(U^n\). Gelfand's formula on successive even exterior powers gives

\[
\left(\frac{\tau_{k+1}(n)}{\tau_k(n)}\right)^{1/n}
\longrightarrow\left(\frac{s_{k+1}}{s_k}\right)^2<1.
\]

If \(s_{k+1}=0\), the numerator is eventually zero; the same conclusion follows directly. Every nonleading summand of \(e_k(\tau(n))\), divided by \(\tau_1(n)\cdots\tau_k(n)\), is at most \(\tau_{k+1}(n)/\tau_k(n)\). Therefore

\[
\frac{e_k(\tau(n))}{\tau_1(n)\cdots\tau_k(n)}\longrightarrow1
\]

and

\[
\boxed{
\frac{\delta_k(f^n)}{\chi^n}
\longrightarrow
\frac{\|\Pi\|}{\binom gk}
\ge\frac1{\binom gk}.
}
\]

A nonzero projection has norm at least one. The lower constant is attained when the spectral projection is orthogonal, for example for suitably diagonal product endomorphisms. Endpoints \(k=0,g\) have constant one. This refinement requires no additional geometric hypothesis and also applies to a positive strict-gap block of a non-isogeny.

## 8. Prerequisites and attribution

Route II eliminates Khovanskii–Teissier, the strict-gap argument, power-sum amplification, and Albert case analysis from the comparison proof. It does **not** eliminate Rosati positivity, Riemann–Roch, the degree/determinant theorem, the polarization identities, finite-dimensional algebra, exterior-power cohomology, or cycle-class compatibility. The numerical quotient argument uses nondegeneracy of numerical intersection pairing, not Standard Conjecture D. No Deligne weight theorem is used.

The targeted primary-source check was Hu, arXiv:1909.12296v3:

- Corollary 1.7 already identifies the coefficients of the relevant square-root characteristic polynomial with the normalized mixed intersections.
- Corollary 5.6 gives a uniform bound of the even cohomological operator norm by the numerical operator norm for every self-morphism of an abelian variety. Combined with the invariant-subspace/quotient bound in the other direction, it already implies the Jordan and nilpotency comparisons above.

Primary source: https://arxiv.org/pdf/1909.12296v3

Accordingly, the proposed refinements are valuable explicit deductions and a clean presentation. The exact finite constants and spectral-projection expression may be highlighted as derived formulas, but their priority has not been established by this limited check.
