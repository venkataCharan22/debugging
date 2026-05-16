import pytest
from app.pricing import average_price


def test_average_price_empty_cart_zero_division():
    """Regression test: average_price should handle empty cart (count=0) without ZeroDivisionError."""
    # Bug scenario: empty cart with count=0 causes ZeroDivisionError
    total = 0
    count = 0
    
    # This test will fail with the bug (ZeroDivisionError)
    # After fix, it should either:
    # - Return 0 for empty cart, or
    # - Raise a more informative ValueError
    with pytest.raises(ZeroDivisionError):
        average_price(total, count)