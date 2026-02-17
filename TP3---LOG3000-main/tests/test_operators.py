"""Unit tests for arithmetic operator functions."""

import pytest

from operators import add, divide, multiply, subtract


def test_add_returns_sum():
    """`add` returns the arithmetic sum of two numbers."""
    assert add(2, 3) == 5


def test_subtract_returns_a_minus_b():
    """`subtract` should compute first operand minus second operand."""
    assert subtract(10, 4) == 6


def test_multiply_returns_product():
    """`multiply` should compute arithmetic product, not exponentiation."""
    assert multiply(3, 4) == 12


def test_divide_returns_true_division():
    """`divide` should preserve decimal precision for non-integer results."""
    assert divide(7, 2) == pytest.approx(3.5)


def test_divide_by_zero_raises():
    """Division by zero must raise ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
