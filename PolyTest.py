import pytest
from Polynomial import Polynomial  # Import the Polynomial class from your module
import math

def test_init():
    poly = Polynomial([3, 0, 2])
    assert poly.coefficients == [3, 0, 2]

def test_str():
    poly = Polynomial([3, 0, 2])
    assert str(poly) == "3x^2 + 2"

    poly2 = Polynomial([1, -1])
    assert str(poly2) == "1x + -1"

    poly3 = Polynomial([0, 0, 0])
    assert str(poly3) == "0" or str(poly3) == ""

def test_add():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [3, 1, 1]

def test_sub():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_diff = poly1 - poly2
    assert poly_diff.coefficients == [3,-1, 3]

def test_mul():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_product = poly1 * poly2
    assert poly_product.coefficients == [3, -3, 2, -2]

def test_first_degree_polynomial():
    poly = Polynomial([2, -3])  # Represents 2x - 3
    root = poly.find_root_bisection(0, 5)
    assert abs(root - 1.5) < 1e-6

def test_second_degree_polynomial():
    poly = Polynomial([1, 0, -2])  # Represents x^2 - 2
    root = poly.find_root_bisection(1, 2)
    assert abs(root - 2.0**0.5) < 1e-6

def test_third_degree_polynomial():
    poly = Polynomial([1, 0, -2, 0])  # Represents x^3 - 2x
    root = poly.find_root_bisection(-2, 2)
    assert abs(root - 0.0) < 1e-6

def test_advanced_scenarios():
    # Advanced polynomial creation and manipulation
    poly1 = Polynomial([1, 2, 3])  # x^2 + 2x + 3
    poly2 = Polynomial([4, 5])      # 4x + 5

    # Test complex addition
    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [1, 6, 8]

    # Test more evaluation scenarios
    assert poly1.evaluate(0) == 3
    assert poly1.evaluate(1) == 6
    assert poly1.evaluate(-1) == 2

def test_edge_case_derivatives():
    # Test derivative calculations
    poly = Polynomial([1, 0, -2])  # x^2 - 2
    derivative_coeffs = poly.get_derivative_coefficients()
    assert derivative_coeffs == [0, 2]

def test_root_finding_variations():
    # More comprehensive root-finding tests
    # Polynomial with multiple potential roots
    poly = Polynomial([1, -6, 11, -6])  # x^3 - 6x^2 + 11x - 6
    
    # Test different interval ranges
    roots = []
    test_intervals = [(0, 3), (1, 4), (2, 5)]
    
    for a, b in test_intervals:
        try:
            root = poly.find_root_bisection(a, b)
            roots.append(root)
        except ValueError:
            pass
    
    # Verify at least one root is found
    assert len(roots) > 0, "No roots found in test intervals"

def test_boundary_conditions():
    # Test polynomials with zero coefficients
    zero_poly = Polynomial([0, 0, 0])
    assert str(zero_poly) == "0"
    assert zero_poly.evaluate(10) == 0

    # Test very large coefficients
    large_poly = Polynomial([1000000, -500000, 250000])
    assert large_poly.evaluate(2) == 1000000 * 4 - 500000 * 2 + 250000