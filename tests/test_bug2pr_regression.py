import pytest
from app.pricing import average_price


def test_average_price_empty_cart_no_division_error():
    """Regression test: average_price should handle empty cart (count=0) without ZeroDivisionError."""
    # Given an empty cart with zero items
    total = 0
    count = 0
    
    # When computing average price
    # Then it should NOT raise ZeroDivisionError
    try:
        result = average_price(total, count)
        # After fix, expect 0 or None for empty cart
        assert result == 0 or result is None
    except ZeroDivisionError:
        pytest.fail("average_price raised ZeroDivisionError on empty cart (count=0)")