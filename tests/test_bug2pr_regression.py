import pytest
from app.pricing import average_price


def test_average_price_with_zero_count():
    """Regression test: ZeroDivisionError when count is 0."""
    # This should not raise ZeroDivisionError after fix
    result = average_price(100, 0)
    assert result == 0.0


def test_average_price_with_valid_count():
    """Verify normal operation still works."""
    result = average_price(100, 4)
    assert result == 25.0