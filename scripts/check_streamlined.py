#!/usr/bin/env python3
"""Exact regression examples for the streamlined note; not a general proof."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
import json
from pathlib import Path

import sympy as sp

from check_identities import REQUIRED_SYMPY


def compound(matrix: sp.Matrix, degree: int) -> sp.Matrix:
    """Matrix of an exterior power in increasing-index wedge bases."""
    indices = list(combinations(range(matrix.rows), degree))
    if degree == 0:
        return sp.ones(1)
    return sp.Matrix([
        [matrix.extract(rows, columns).det() for columns in indices]
        for rows in indices
    ])


def delta(matrix: sp.Matrix, degree: int) -> sp.Expr:
    """Normalized mixed degree on product-polarized E^g, by squared minors."""
    exterior = compound(matrix, degree)
    return sp.expand(sum((entry ** 2 for entry in exterior), sp.Integer(0))
                     / sp.binomial(matrix.rows, degree))


def nilpotency_index(matrix: sp.Matrix) -> int:
    """Least positive r with matrix**r=0; refuse a nonnilpotent input."""
    power = sp.eye(matrix.rows)
    zero = sp.zeros(matrix.rows)
    for exponent in range(1, matrix.rows + 1):
        power = power * matrix
        if power == zero:
            return exponent
    raise AssertionError("Expected a nilpotent matrix")


def matrix_data(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(entry) for entry in row] for row in matrix.tolist()]


def run_checks() -> dict:
    if sp.__version__ != REQUIRED_SYMPY:
        raise RuntimeError(f"Use SymPy {REQUIRED_SYMPY}; found {sp.__version__}.")

    counts: Counter[str] = Counter()

    def ensure(condition: bool, check: str, context: str) -> None:
        if not bool(condition):
            raise AssertionError(f"{check}: {context}")
        counts[check] += 1

    def nonnegative(value: sp.Expr, check: str, context: str) -> None:
        if value.is_Rational is not True:
            raise AssertionError(f"Non-rational sign test: {check}; {context}")
        ensure(value >= 0, check, context)

    shift2 = sp.Matrix([[0, 1], [0, 0]])
    shift3 = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    involution = sp.Matrix([[1, 1], [0, -1]])
    composition_cases = [
        ("opposite_shears_2", sp.eye(2) + shift2,
         sp.eye(2) + shift2.T, True),
        ("nonnormal_and_rotation_2", sp.Matrix([[2, 1], [0, 1]]),
         sp.Matrix([[0, -1], [1, 0]]), True),
        ("nilpotent_and_transpose_2", shift2, shift2.T, True),
        ("skew_rank_one_2", sp.Matrix([[1, 2], [0, 0]]),
         sp.Matrix([[0, 1], [0, 3]]), True),
        ("involution_and_rank_one_2", involution,
         sp.Matrix([[2, 0], [1, 0]]), True),
        ("complementary_projections_2", sp.diag(1, 0),
         sp.diag(0, 1), False),
        ("opposite_shears_3", sp.eye(3) + shift3,
         sp.eye(3) + 2 * shift3.T, True),
        ("nilpotent_and_transpose_3", shift3, shift3.T, True),
        ("singular_and_dense_3", sp.Matrix([[1, 1, 0], [0, 0, 1], [0, 0, 0]]),
         sp.Matrix([[2, 0, 1], [0, 1, 0], [1, 0, 0]]), True),
    ]
    sharp_cases = []
    for g in (2, 3):
        for k in range(1, g):
            projection = sp.diag(*([1] * k + [0] * (g - k)))
            name = f"sharp_projection_g{g}_k{k}"
            composition_cases.append((name, projection, projection, False))
            sharp_cases.append((name, g, k, projection))

    composition_results = []
    for name, left, right, expected_noncommuting in composition_cases:
        g = left.rows
        noncommuting = left * right != right * left
        ensure(noncommuting == expected_noncommuting,
               "composition_commutation_metadata", name)
        rows = []
        for k in range(g + 1):
            actual = delta(left * right, k)
            upper = sp.binomial(g, k) * delta(left, k) * delta(right, k)
            defect = sp.expand(upper - actual)
            nonnegative(defect, "composition_bound", f"{name}; k={k}")
            rows.append({
                "k": k,
                "delta_product": str(actual),
                "binomial_delta_left_delta_right": str(upper),
                "nonnegative_defect": str(defect),
            })
        composition_results.append({
            "name": name,
            "g": g,
            "left": matrix_data(left),
            "right": matrix_data(right),
            "noncommuting": noncommuting,
            "has_singular_factor": left.det() == 0 or right.det() == 0,
            "codimensions": rows,
        })

    sharp_results = []
    for name, g, k, projection in sharp_cases:
        normalizer = sp.binomial(g, k)
        ensure(projection ** 2 == projection and projection.rank() == k,
               "sharp_projection_rank_and_idempotence", name)
        value = delta(projection, k)
        ensure(value == 1 / normalizer, "sharp_projection_normalization", name)
        ensure(delta(projection ** 2, k) == normalizer * value ** 2,
               "sharp_composition_equality", name)
        sharp_results.append({
            "g": g, "k": k, "delta": str(value),
            "required_composition_constant": str(normalizer),
        })

    # A nonzero nilpotent exterior action makes the all-n radius-zero bound fail.
    nilpotent_exterior = compound(sp.diag(shift2, shift2), 2)
    ensure(delta(shift2, 1) == sp.Rational(1, 2),
           "nilpotent_first_mixed_degree", "n=1")
    ensure(shift2 ** 2 == sp.zeros(2) and delta(shift2 ** 2, 1) == 0,
           "nilpotent_second_mixed_degree", "n=2")
    ensure(nilpotent_exterior != sp.zeros(6)
           and nilpotent_exterior ** 2 == sp.zeros(6),
           "nilpotent_exterior_index", "wedge^2(M direct_sum M)")
    nilpotent_result = {
        "matrix": matrix_data(shift2),
        "delta_1_n1": "1/2", "delta_1_n_ge_2": "0",
        "exterior_spectral_radius": "0", "exterior_nilpotency_index": 2,
        "consequence": "A bound C*n**a*rho**n for every n>=1 fails when rho=0.",
    }

    # Symbolic recurrence proves the displayed power formulas for all n>=0.
    n = sp.symbols("n", integer=True, nonnegative=True)
    jordan_results = []
    expected_polynomials = {
        (2, 0): sp.Integer(1),
        (2, 1): 1 + n ** 2 / 2,
        (2, 2): sp.Integer(1),
        (3, 0): sp.Integer(1),
        (3, 1): 1 + 2 * n ** 2 / 3 + n ** 2 * (n - 1) ** 2 / 12,
        (3, 2): 1 + 2 * n ** 2 / 3 + n ** 2 * (n + 1) ** 2 / 12,
        (3, 3): sp.Integer(1),
    }
    for g, shift in ((2, shift2), (3, shift3)):
        matrix = sp.eye(g) + shift
        symbolic_power = sp.zeros(g)
        for j in range(g):
            coefficient = sp.prod(n - r for r in range(j)) / sp.factorial(j)
            symbolic_power += coefficient * shift ** j
        ensure(symbolic_power.subs(n, 0) == sp.eye(g),
               "unipotent_power_initial_value", f"g={g}")
        recurrence_defect = (symbolic_power.subs(n, n + 1)
                             - matrix * symbolic_power).applyfunc(sp.expand)
        ensure(recurrence_defect == sp.zeros(g),
               "unipotent_power_symbolic_recurrence", f"g={g}")
        for k in range(g + 1):
            polynomial = sp.Poly(delta(symbolic_power, k), n)
            expected = expected_polynomials[g, k]
            ensure(sp.expand(polynomial.as_expr() - expected) == 0,
                   "unipotent_mixed_degree_polynomial", f"g={g}; k={k}")
            exterior = compound(sp.diag(matrix, matrix), 2 * k)
            nilpotent_part = exterior - sp.eye(exterior.rows)
            index = nilpotency_index(nilpotent_part)
            ensure(nilpotent_part ** index == sp.zeros(exterior.rows)
                   and nilpotent_part ** (index - 1) != sp.zeros(exterior.rows),
                   "unipotent_exterior_nilpotency_index", f"g={g}; k={k}")
            ensure(polynomial.degree() == index - 1,
                   "polynomial_degree_equals_jordan_exponent", f"g={g}; k={k}")
            jordan_results.append({
                "g": g, "k": k,
                "delta_polynomial": str(polynomial.as_expr()),
                "delta_polynomial_latex": sp.latex(polynomial.as_expr()),
                "polynomial_degree": int(polynomial.degree()),
                "largest_exterior_jordan_block": index,
                "exterior_dimension": exterior.rows,
            })

    # For each spectral projection, compute its exterior norm by an exact
    # Gram characteristic polynomial. No singular-value approximation is used.
    q = sp.symbols("q", real=True)
    # Matrix.charpoly uses an assumption-free generator; match it exactly.
    x = sp.symbols("x")
    gap_results = []
    gap_cases = (
        ("nonnormal", sp.Matrix([[2, 1], [0, 1]]),
         sp.Matrix([[1, 1], [0, 0]]), q ** 2 - q + 1, sp.Integer(1), sp.Integer(4)),
        ("normal", sp.diag(2, 1), sp.diag(1, 0),
         (q ** 2 + 1) / 2, sp.Rational(1, 2), sp.Integer(1)),
    )
    for name, matrix, projection, expected, leading, gram_eigenvalue in gap_cases:
        identity = sp.eye(2)
        ensure(projection ** 2 == projection
               and matrix == 2 * projection + (identity - projection),
               "strict_gap_spectral_projection", name)
        power_formula = q * projection + (identity - projection)
        actual = delta(power_formula, 1)
        ensure(sp.expand(actual - expected) == 0,
               "strict_gap_degree_formula", name)
        for exponent in range(7):
            power = matrix ** exponent
            ensure(power == power_formula.subs(q, 2 ** exponent),
                   "strict_gap_exact_power_samples", f"{name}; n={exponent}")
        ensure(sp.limit(actual / q ** 2, q, sp.oo) == leading,
               "strict_gap_exact_leading_limit", name)
        exterior_projection = compound(sp.diag(projection, projection), 2)
        gram = exterior_projection.T * exterior_projection
        ensure(exterior_projection.rank() == 1
               and sp.expand(gram.charpoly(x).as_expr()
                             - x ** 5 * (x - gram_eigenvalue)) == 0,
               "strict_gap_projection_gram_spectrum", name)
        exact_norm = sp.sqrt(gram_eigenvalue)
        ensure(exact_norm / 2 == leading,
               "strict_gap_projection_norm_constant", name)
        gap_results.append({
            "name": name, "matrix": matrix_data(matrix),
            "projection": matrix_data(projection),
            "q_definition": "q=2**n",
            "delta_polynomial_in_q": str(sp.expand(actual)),
            "delta_polynomial_in_q_latex": sp.latex(sp.expand(actual)),
            "limit_delta_over_4_to_n": str(leading),
            "exterior_projection_gram_characteristic_polynomial": str(
                sp.factor(gram.charpoly(x).as_expr())),
            "exterior_projection_norm": str(exact_norm),
            "projection_norm_divided_by_2": str(exact_norm / 2),
            "sample_exponents": list(range(7)),
        })

    ensure(involution ** 2 == sp.eye(2), "oscillation_period_two", "involution")
    ensure(delta(involution, 1) == sp.Rational(3, 2)
           and delta(sp.eye(2), 1) == 1,
           "oscillation_distinct_subsequence_values", "odd=3/2; even=1")
    involution_exterior = compound(sp.diag(involution, involution), 2)
    ensure(sp.expand(involution_exterior.charpoly(x).as_expr()
                     - (x - 1) ** 2 * (x + 1) ** 4) == 0,
           "oscillation_exterior_spectral_radius_one", "wedge^2(M direct_sum M)")
    oscillation_result = {
        "matrix": matrix_data(involution), "matrix_squared": "identity",
        "delta_1_odd": "3/2", "delta_1_even": "1",
        "exterior_spectral_radius": "1",
        "exterior_characteristic_polynomial": "(x - 1)**2 * (x + 1)**4",
        "consequence": "delta_1(M**n)/rho**n has no limit outside a strict gap.",
    }

    return {
        "status": "passed",
        "sympy_version": sp.__version__,
        "arithmetic": "exact integer/rational matrices and symbolic polynomials; no numerical SVD",
        "command": "python scripts/check_streamlined.py --report audit/streamlined/exact_checks.json --markdown audit/streamlined/exact_checks.md",
        "composition_pair_count": len(composition_results),
        "noncommuting_composition_pair_count": sum(
            case["noncommuting"] for case in composition_results),
        "composition_pairs_with_singular_factor": sum(
            case["has_singular_factor"] for case in composition_results),
        "composition_cases": composition_results,
        "sharp_composition_cases": sharp_results,
        "nilpotent_counterexample": nilpotent_result,
        "unipotent_jordan_cases": jordan_results,
        "strict_gap_cases": gap_results,
        "outside_gap_nonconvergence": oscillation_result,
        "checks": dict(sorted(counts.items())),
        "total_checks": sum(counts.values()),
        "scope_limitations": [
            "Concrete integer-matrix endomorphisms of product-polarized E^g only.",
            "The unipotent and strict-gap closed formulas are checked symbolically; other composition cases are finite examples.",
            "These checks detect constants, conventions, and edge-case errors; they do not prove the general geometric claims.",
            "No claim of novelty, formal proof certification, or a full comparison of numerical and cohomological Jordan forms.",
        ],
    }


def markdown_report(report: dict) -> str:
    lines = [
        "# Exact regression checks for the streamlined note", "",
        f"**Status: {report['status']}.** SymPy {report['sympy_version']}; "
        f"{report['total_checks']} exact assertions. No numerical SVD or floating-point sign tests.",
        "", "## Reproduce", "", "```sh", report["command"], "```", "",
        "The mixed degree is computed independently from squared minors:", "",
        r"\[\delta_k(M)=\binom{g}{k}^{-1}\sum_{|I|=|J|=k}\det(M_{I,J})^2.\]",
        "", "This is the product-polarized elliptic-power matrix model.", "",
        "## Composition and sharpness", "",
        f"Checked {report['checks']['composition_bound']} codimension inequalities across "
        f"{report['composition_pair_count']} ordered pairs, including "
        f"{report['noncommuting_composition_pair_count']} noncommuting pairs and "
        f"{report['composition_pairs_with_singular_factor']} pairs with a singular factor:", "",
        r"\[\delta_k(AB)\le\binom{g}{k}\delta_k(A)\delta_k(B).\]", "",
        "| Pair | Dimension | Noncommuting | Singular factor | Codimensions |",
        "|---|---:|:---:|:---:|---|",
    ]
    for case in report["composition_cases"]:
        lines.append(f"| {case['name']} | {case['g']} | "
                     f"{'yes' if case['noncommuting'] else 'no'} | "
                     f"{'yes' if case['has_singular_factor'] else 'no'} | "
                     f"0 through {case['g']} |")
    lines += [
        "", "For the rank-k projections below, A=B=P, P²=P, and equality holds. "
        "Thus the example requires the displayed binomial composition constant.", "",
        "| g | k | δ_k(P) | Required constant |", "|---:|---:|---:|---:|",
    ]
    for case in report["sharp_composition_cases"]:
        lines.append(f"| {case['g']} | {case['k']} | {case['delta']} | "
                     f"{case['required_composition_constant']} |")
    lines += [
        "", "## Zero-radius counterexample", "",
        r"For \(M=\begin{pmatrix}0&1\\0&0\end{pmatrix}\), "
        r"\(\delta_1(M)=1/2\), while \(M^2=0\) and \(\delta_1(M^n)=0\) for \(n\ge2\).",
        r"The operator \(\wedge^2(M\oplus M)\) is nonzero and its square is zero. "
        r"Its spectral radius is zero and its nilpotency index is two. "
        r"Therefore an all-n estimate \(Cn^a\rho^n\) cannot cover nonzero nilpotent operators.",
        "", "## Polynomial degrees and exterior Jordan blocks", "",
        r"For \(M=I+J_g\), with \(J_g\) the nilpotent shift, the power formula "
        r"\(M^n=\sum_{j=0}^{g-1}\binom njJ_g^j\) is checked by its initial value and "
        "a symbolic recurrence. The largest exterior Jordan block is computed as the "
        r"nilpotency index of \(\wedge^{2k}(M\oplus M)-I\), with the last nonzero power verified.",
        "", "| g | k | Exact δ_k(Mⁿ) | Polynomial degree | Largest exterior Jordan block |",
        "|---:|---:|---|---:|---:|",
    ]
    for case in report["unipotent_jordan_cases"]:
        lines.append(f"| {case['g']} | {case['k']} | "
                     f"${case['delta_polynomial_latex']}$ | {case['polynomial_degree']} | "
                     f"{case['largest_exterior_jordan_block']} |")
    lines += [
        "", "Every displayed polynomial degree equals the largest block size minus one.",
        "", "## Strict-gap leading constants", "",
        "Here q=2ⁿ. Spectral projections are checked exactly. Their exterior norms are "
        "read from exact Gram characteristic polynomials, not approximated singular values.",
        "", "| Example | Exact δ₁(Mⁿ) | Limit δ₁(Mⁿ)/4ⁿ | Exterior projection norm | Norm/2 |",
        "|---|---|---:|---:|---:|",
    ]
    for case in report["strict_gap_cases"]:
        lines.append(f"| {case['name']} | ${case['delta_polynomial_in_q_latex']}$ | "
                     f"{case['limit_delta_over_4_to_n']} | {case['exterior_projection_norm']} | "
                     f"{case['projection_norm_divided_by_2']} |")
    lines += [
        "",
        r"The nonnormal matrix is \(\begin{pmatrix}2&1\\0&1\end{pmatrix}\), "
        r"with \(P=\begin{pmatrix}1&1\\0&0\end{pmatrix}\). Its formula is "
        r"\(4^n-2^n+1\), and the Gram polynomial of \(\wedge^2(P\oplus P)\) is \(x^5(x-4)\). "
        r"For the normal matrix \(\operatorname{diag}(2,1)\), the formula is "
        r"\((4^n+1)/2\) and the corresponding Gram polynomial is \(x^5(x-1)\).",
        "", "## Nonconvergence without a gap", "",
        r"For \(M=\begin{pmatrix}1&1\\0&-1\end{pmatrix}\), the exact identity "
        r"\(M^2=I\) gives \(\delta_1(M^n)=3/2\) for odd n and 1 for even n. "
        r"The exterior characteristic polynomial is \((x-1)^2(x+1)^4\), so the "
        "spectral radius is one. The normalized mixed-degree sequence does not converge.",
        "", "## Actual assertion counts", "",
        "| Assertion category | Count |", "|---|---:|",
    ]
    lines.extend(f"| {name} | {count} |" for name, count in report["checks"].items())
    lines.append(f"| **Total** | **{report['total_checks']}** |")
    lines += ["", "## Scope", ""]
    lines.extend(f"- {limitation}" for limitation in report["scope_limitations"])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="save the full exact JSON report")
    parser.add_argument("--markdown", type=Path, help="save the readable report")
    args = parser.parse_args()
    report = run_checks()
    if args.report is not None:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n",
                               encoding="utf-8")
    if args.markdown is not None:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(markdown_report(report), encoding="utf-8")
    print(json.dumps({
        "status": report["status"], "total_checks": report["total_checks"],
        "checks": report["checks"],
        "report": str(args.report) if args.report else None,
        "markdown": str(args.markdown) if args.markdown else None,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
