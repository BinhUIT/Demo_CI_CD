import pytest
from src.math_utils import factorial

def test_factorial_basic():
    # Check familiar values
    assert factorial(0) == 1
    assert factorial(5) == 120

def test_factorial_raises_on_negative():
    # The function must raise on a negative input
    with pytest.raises(ValueError):
        factorial(-1)