# Exact regression checks for the streamlined note

**Status: passed.** SymPy 1.14.0; 117 exact assertions. No numerical SVD or floating-point sign tests.

## Reproduce

```sh
python scripts/check_streamlined.py --report audit/streamlined/exact_checks.json --markdown audit/streamlined/exact_checks.md
```

The mixed degree is computed independently from squared minors:

\[\delta_k(M)=\binom{g}{k}^{-1}\sum_{|I|=|J|=k}\det(M_{I,J})^2.\]

This is the product-polarized elliptic-power matrix model.

## Composition and sharpness

Checked 41 codimension inequalities across 12 ordered pairs, including 8 noncommuting pairs and 9 pairs with a singular factor:

\[\delta_k(AB)\le\binom{g}{k}\delta_k(A)\delta_k(B).\]

| Pair | Dimension | Noncommuting | Singular factor | Codimensions |
|---|---:|:---:|:---:|---|
| opposite_shears_2 | 2 | yes | no | 0 through 2 |
| nonnormal_and_rotation_2 | 2 | yes | no | 0 through 2 |
| nilpotent_and_transpose_2 | 2 | yes | yes | 0 through 2 |
| skew_rank_one_2 | 2 | yes | yes | 0 through 2 |
| involution_and_rank_one_2 | 2 | yes | yes | 0 through 2 |
| complementary_projections_2 | 2 | no | yes | 0 through 2 |
| opposite_shears_3 | 3 | yes | no | 0 through 3 |
| nilpotent_and_transpose_3 | 3 | yes | yes | 0 through 3 |
| singular_and_dense_3 | 3 | yes | yes | 0 through 3 |
| sharp_projection_g2_k1 | 2 | no | yes | 0 through 2 |
| sharp_projection_g3_k1 | 3 | no | yes | 0 through 3 |
| sharp_projection_g3_k2 | 3 | no | yes | 0 through 3 |

For the rank-k projections below, A=B=P, P²=P, and equality holds. Thus the example requires the displayed binomial composition constant.

| g | k | δ_k(P) | Required constant |
|---:|---:|---:|---:|
| 2 | 1 | 1/2 | 2 |
| 3 | 1 | 1/3 | 3 |
| 3 | 2 | 1/3 | 3 |

## Zero-radius counterexample

For \(M=\begin{pmatrix}0&1\\0&0\end{pmatrix}\), \(\delta_1(M)=1/2\), while \(M^2=0\) and \(\delta_1(M^n)=0\) for \(n\ge2\).
The operator \(\wedge^2(M\oplus M)\) is nonzero and its square is zero. Its spectral radius is zero and its nilpotency index is two. Therefore an all-n estimate \(Cn^a\rho^n\) cannot cover nonzero nilpotent operators.

## Polynomial degrees and exterior Jordan blocks

For \(M=I+J_g\), with \(J_g\) the nilpotent shift, the power formula \(M^n=\sum_{j=0}^{g-1}\binom njJ_g^j\) is checked by its initial value and a symbolic recurrence. The largest exterior Jordan block is computed as the nilpotency index of \(\wedge^{2k}(M\oplus M)-I\), with the last nonzero power verified.

| g | k | Exact δ_k(Mⁿ) | Polynomial degree | Largest exterior Jordan block |
|---:|---:|---|---:|---:|
| 2 | 0 | $1$ | 0 | 1 |
| 2 | 1 | $\frac{n^{2}}{2} + 1$ | 2 | 3 |
| 2 | 2 | $1$ | 0 | 1 |
| 3 | 0 | $1$ | 0 | 1 |
| 3 | 1 | $\frac{n^{4}}{12} - \frac{n^{3}}{6} + \frac{3 n^{2}}{4} + 1$ | 4 | 5 |
| 3 | 2 | $\frac{n^{4}}{12} + \frac{n^{3}}{6} + \frac{3 n^{2}}{4} + 1$ | 4 | 5 |
| 3 | 3 | $1$ | 0 | 1 |

Every displayed polynomial degree equals the largest block size minus one.

## Strict-gap leading constants

Here q=2ⁿ. Spectral projections are checked exactly. Their exterior norms are read from exact Gram characteristic polynomials, not approximated singular values.

| Example | Exact δ₁(Mⁿ) | Limit δ₁(Mⁿ)/4ⁿ | Exterior projection norm | Norm/2 |
|---|---|---:|---:|---:|
| nonnormal | $q^{2} - q + 1$ | 1 | 2 | 1 |
| normal | $\frac{q^{2}}{2} + \frac{1}{2}$ | 1/2 | 1 | 1/2 |

The nonnormal matrix is \(\begin{pmatrix}2&1\\0&1\end{pmatrix}\), with \(P=\begin{pmatrix}1&1\\0&0\end{pmatrix}\). Its formula is \(4^n-2^n+1\), and the Gram polynomial of \(\wedge^2(P\oplus P)\) is \(x^5(x-4)\). For the normal matrix \(\operatorname{diag}(2,1)\), the formula is \((4^n+1)/2\) and the corresponding Gram polynomial is \(x^5(x-1)\).

## Nonconvergence without a gap

For \(M=\begin{pmatrix}1&1\\0&-1\end{pmatrix}\), the exact identity \(M^2=I\) gives \(\delta_1(M^n)=3/2\) for odd n and 1 for even n. The exterior characteristic polynomial is \((x-1)^2(x+1)^4\), so the spectral radius is one. The normalized mixed-degree sequence does not converge.

## Actual assertion counts

| Assertion category | Count |
|---|---:|
| composition_bound | 41 |
| composition_commutation_metadata | 12 |
| nilpotent_exterior_index | 1 |
| nilpotent_first_mixed_degree | 1 |
| nilpotent_second_mixed_degree | 1 |
| oscillation_distinct_subsequence_values | 1 |
| oscillation_exterior_spectral_radius_one | 1 |
| oscillation_period_two | 1 |
| polynomial_degree_equals_jordan_exponent | 7 |
| sharp_composition_equality | 3 |
| sharp_projection_normalization | 3 |
| sharp_projection_rank_and_idempotence | 3 |
| strict_gap_degree_formula | 2 |
| strict_gap_exact_leading_limit | 2 |
| strict_gap_exact_power_samples | 14 |
| strict_gap_projection_gram_spectrum | 2 |
| strict_gap_projection_norm_constant | 2 |
| strict_gap_spectral_projection | 2 |
| unipotent_exterior_nilpotency_index | 7 |
| unipotent_mixed_degree_polynomial | 7 |
| unipotent_power_initial_value | 2 |
| unipotent_power_symbolic_recurrence | 2 |
| **Total** | **117** |

## Scope

- Concrete integer-matrix endomorphisms of product-polarized E^g only.
- The unipotent and strict-gap closed formulas are checked symbolically; other composition cases are finite examples.
- These checks detect constants, conventions, and edge-case errors; they do not prove the general geometric claims.
- No claim of novelty, formal proof certification, or a full comparison of numerical and cohomological Jordan forms.
