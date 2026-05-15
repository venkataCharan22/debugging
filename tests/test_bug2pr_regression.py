from app.pricing import average_price

def test_average_price_division_by_zero():
    # Test with zero count
    prices = [10, 20, 30]
    count = 0
    try:
        average_price(prices, count)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        assert True

    # Test with non-zero count
    count = 3
    result = average_price(prices, count)
    assert result == sum(prices) / count