#!/usr/bin/env python3
"""Exact normalization checks on product-polarized E^g; not proof verification."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
import json
from pathlib import Path

import sympy as sp


REQUIRED_SYMPY = "1.14.0"
SHIFTS = (
    sp.Rational(-5, 2),
    sp.Integer(-1),
    sp.Rational(-1, 3),
    sp.Integer(0),
    sp.Rational(2, 3),
    sp.Integer(2),
    sp.Rational(7, 2),
)
ITERATES = (1, 2)


def run_checks() -> dict:
    if sp.__version__ != REQUIRED_SYMPY:
        raise RuntimeError(
            f"Use SymPy {REQUIRED_SYMPY}; found {sp.__version__}."
        )

    counts: Counter[str] = Counter()

    def ensure(condition: bool, check: str, context: str) -> None:
        if not bool(condition):
            raise AssertionError(f"{check}: {context}")
        counts[check] += 1

    def nonnegative(value: sp.Expr, check: str, context: str) -> None:
        # Refuse to substitute floating-point or undecidable sign tests.
        if value.is_Rational is not True:
            raise AssertionError(f"Non-rational sign test in {check}: {context}")
        ensure(value >= 0, check, context)

    def elementary_symmetric(gram: sp.Matrix) -> list[sp.Expr]:
        # Compute by principal minors, independently of charpoly coefficients.
        g = gram.rows
        values: list[sp.Expr] = [sp.Integer(1)]
        for j in range(1, g + 1):
            values.append(
                sum(
                    (gram.extract(indices, indices).det()
                     for indices in combinations(range(g), j)),
                    sp.Integer(0),
                )
            )
        return values

    def check_psd(matrix: sp.Matrix, context: str) -> None:
        ensure(matrix == matrix.T, "nef_bound_symmetry", context)
        # All principal minors characterize positive semidefiniteness of a
        # real symmetric matrix. Every minor here is an exact integer.
        for size in range(1, matrix.rows + 1):
            for indices in combinations(range(matrix.rows), size):
                nonnegative(
                    matrix.extract(indices, indices).det(),
                    "nef_bound_principal_minors",
                    f"{context}; principal indices={indices}",
                )

    # Preserve deterministic insertion order and merge duplicate matrices.
    cases: dict[tuple, dict] = {}

    def add_case(name: str, matrix: sp.Matrix) -> None:
        key = (matrix.rows, tuple(int(entry) for entry in matrix))
        if key in cases:
            cases[key]["labels"].append(name)
        else:
            cases[key] = {"matrix": matrix, "labels": [name]}

    rotation = sp.Matrix([[0, -2], [2, 0]])
    for g in range(1, 5):
        identity = sp.eye(g)
        shift = sp.Matrix(g, g, lambda i, j: int(j == i + 1))
        cycle = sp.zeros(g)
        for j in range(g):
            cycle[(j + 1) % g, j] = 1
        add_case("zero", sp.zeros(g))
        add_case("identity", identity)
        add_case("negative_identity", -identity)
        add_case("repeated_modulus_scalar", 2 * identity)
        add_case("strict_diagonal_gaps", sp.diag(*(2 * j + 1 for j in range(g))))
        add_case("signed_diagonal", sp.diag(*((-1) ** (j + 1) * (j + 2)
                                               for j in range(g))))
        add_case("singular_diagonal", sp.diag(*(0 if j == 0 else 2 * j + 1
                                                 for j in range(g))))
        add_case("nonnormal_jordan", 2 * identity + shift)
        add_case("nilpotent_shift", shift)
        add_case("scaled_cyclic_permutation", 2 * cycle)
        column = sp.Matrix([j + 1 for j in range(g)])
        row = sp.Matrix([[(-1) ** j * (j + 1) for j in range(g)]])
        add_case("rank_one", column * row)
        add_case("deterministic_dense", sp.Matrix(
            g, g, lambda i, j: ((i + 1) * (j + 2) + 3 * (i - j)) % 7 - 3
        ))
        if g >= 2:
            add_case("rotation_repeated_modulus", sp.diag(rotation, 2 * sp.eye(g - 2)))
            add_case("rotation_with_gaps", sp.diag(
                rotation, *(2 * j + 1 for j in range(2, g))
            ))
        if g == 4:
            add_case("two_equal_rotation_blocks", sp.diag(rotation, rotation))
            add_case("two_unequal_rotation_blocks", sp.diag(
                rotation, sp.Matrix([[0, -5], [5, 0]])
            ))

    t, x = sp.symbols("t x")
    dimensions: Counter[int] = Counter()
    for case in cases.values():
        matrix = case["matrix"]
        g = matrix.rows
        dimensions[g] += 1
        for n in ITERATES:
            power = matrix ** n
            identity = sp.eye(g)
            gram = power.T * power
            es = elementary_symmetric(gram)
            delta = [es[j] / sp.binomial(g, j) for j in range(g + 1)]
            determinant_polynomial = power.charpoly(t).as_expr()
            degree_polynomial = sp.Poly(determinant_polynomial ** 2, t)
            mixed_polynomial = sp.Poly(
                (-1) ** g * gram.charpoly(x).as_expr().subs(x, -t ** 2), t
            )
            mixed_expansion = sum(
                (sp.binomial(g, j) * delta[j] * t ** (2 * (g - j))
                 for j in range(g + 1)),
                sp.Integer(0),
            )
            context = f"g={g}; labels={','.join(case['labels'])}; n={n}"

            ensure(degree_polynomial.degree() == 2 * g,
                   "characteristic_degree", context)
            ensure(degree_polynomial.nth(2 * g - 1) == -2 * sp.trace(power),
                   "trace_coefficient", context)
            ensure(sp.expand(mixed_polynomial.as_expr() - mixed_expansion) == 0,
                   "mixed_polynomial_normalization", context)
            ensure(delta[0] == 1, "endpoint_delta_zero", context)
            ensure(delta[g] == power.det() ** 2,
                   "endpoint_delta_top", context)
            ensure(delta[g] == matrix.det() ** (2 * n),
                   "endpoint_iterate_degree", context)
            ensure(delta[1] == sp.trace(gram) / g,
                   "first_mixed_degree_normalization", context)
            nonnegative(
                4 * g ** 2 * delta[1] - (2 * sp.trace(power)) ** 2,
                "trace_inequality", context,
            )
            for j in range(1, g):
                nonnegative(delta[j] ** 2 - delta[j - 1] * delta[j + 1],
                            "khovanskii_teissier", f"{context}; j={j}")

            for shift_value in SHIFTS:
                shifted = shift_value * identity - power
                plus_shifted = shift_value * identity + power
                gram_shifted = shifted.T * shifted
                p_value = degree_polynomial.eval(shift_value)
                mixed_value = mixed_polynomial.eval(shift_value)
                shift_context = f"{context}; t={shift_value}"
                ensure(p_value == shifted.det() ** 2,
                       "degree_determinant_identity", shift_context)
                ensure(p_value == gram_shifted.det(),
                       "degree_gram_identity", shift_context)
                nonnegative(p_value, "degree_nonnegativity", shift_context)
                ensure(
                    2 * (shift_value ** 2 * identity + gram) - gram_shifted
                    == plus_shifted.T * plus_shifted,
                    "parallelogram_gram_identity", shift_context,
                )
                nonnegative(2 ** g * mixed_value - p_value,
                            "mixed_degree_inequality", shift_context)

    jordan = sp.Matrix([[2, 1], [0, 2]])
    for n in range(1, 9):
        power = jordan ** n
        actual = sp.trace(power.T * power) / 2
        expected = sp.Integer(4) ** n * (1 + sp.Rational(n ** 2, 8))
        ensure(actual == expected, "jordan_exact_growth", f"n={n}")

    similitude_cases = ((2, 2, 3), (3, 1, 4), (4, 2, 5), (2, 3, 3))
    for g, r, s in similitude_cases:
        identity = sp.eye(g)
        permutation = sp.zeros(g)
        for j in range(g):
            permutation[(j + 1) % g, j] = 1
        signs = sp.diag(-1, *([1] * (g - 1)))
        u, v = r * permutation, s * signs
        context = f"g={g}; multipliers=({r}^2,{s}^2)"
        ensure(u * v != v * u, "similitude_noncommutation", context)
        ensure(u.T * u == r ** 2 * identity,
               "similitude_u_normalization", context)
        ensure(v.T * v == s ** 2 * identity,
               "similitude_v_normalization", context)
        difference_gram = (u - v).T * (u - v)
        check_psd(difference_gram - (r - s) ** 2 * identity,
                  f"lower Gram bound; {context}")
        check_psd((r + s) ** 2 * identity - difference_gram,
                  f"upper Gram bound; {context}")
        degree = (u - v).det() ** 2
        nonnegative(degree - (r - s) ** (2 * g),
                    "two_map_degree_lower", context)
        nonnegative((r + s) ** (2 * g) - degree,
                    "two_map_degree_upper", context)

    # A symbolic normalization check, with no sign assumptions on the entries.
    a, b, c, d = sp.symbols("a b c d")
    symbolic_matrix = sp.Matrix([[a, b], [c, d]])
    trace_defect = (
        8 * sp.trace(symbolic_matrix.T * symbolic_matrix)
        - (2 * sp.trace(symbolic_matrix)) ** 2
    )
    ensure(sp.expand(trace_defect - 4 * ((a - d) ** 2 + 2 * b ** 2 + 2 * c ** 2)) == 0,
           "symbolic_trace_sum_of_squares", "generic 2-by-2 matrix")

    return {
        "status": "passed",
        "arithmetic": "exact integers, rationals, and symbolic polynomials",
        "sympy_version": sp.__version__,
        "dimensions": [1, 2, 3, 4],
        "distinct_base_matrices": len(cases),
        "base_matrices_by_dimension": {str(g): dimensions[g] for g in range(1, 5)},
        "iterate_exponents": list(ITERATES),
        "matrix_iterate_cases": len(cases) * len(ITERATES),
        "rational_shifts": [str(value) for value in SHIFTS],
        "shifted_cases": len(cases) * len(ITERATES) * len(SHIFTS),
        "jordan_exponents": list(range(1, 9)),
        "noncommuting_similitude_cases": len(similitude_cases),
        "checks": dict(sorted(counts.items())),
        "total_checks": sum(counts.values()),
        "scope_limitations": [
            "Finite sanity checks on integer-matrix endomorphisms of product-polarized E^g.",
            "Checks normalizations and examples; does not verify the general geometric proofs.",
            "No floating-point spectral comparisons, novelty claims, or formal proof certification.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path,
                        help="also save the deterministic JSON result to this file")
    args = parser.parse_args()
    report = json.dumps(run_checks(), indent=2, sort_keys=True) + "\n"
    if args.report is not None:
        args.report.write_text(report, encoding="utf-8")
    print(report, end="")


if __name__ == "__main__":
    main()
