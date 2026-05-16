"""Pricing calculations.

⚠️  Contains the `div_zero` demo bug: average_price() divides by count
without checking for zero, raising ZeroDivisionError on empty carts.
"""


def total_price(items):
    """Sum the prices of all items in the cart."""
    return sum(item.get("price", 0) for item in items)


def average_price(total, count):
    """Compute average price per item."""
    # BUG: no zero check on `count`
    return total / count


def apply_tax(amount, rate=0.08):
    """Apply tax to an amount."""
    return round(amount * (1 + rate), 2)
