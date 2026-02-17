"""Basic arithmetic operators used by the calculator backend."""

def add(a,b):
    """Return the sum of two numbers.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        Numeric sum of ``a`` and ``b``.
    """
    return a + b

def subtract(a,b):
    """Return the subtraction result between two numbers.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        Numeric subtraction result.
    """
    return b - a

def multiply(a,b):
    """Return the multiplication result between two numbers.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        Numeric multiplication result.
    """
    return a ** b

def divide(a,b):
    """Return the division result between two numbers.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        Numeric division result.
    """
    return a / b
