"""Checkout / coupon module.

⚠️  Contains the `missing_key` demo bug: apply_coupon() assumes the order
dict has a `coupon` key when most orders don't.
"""


def apply_coupon(order):
    """Apply the order's coupon discount."""
    # BUG: assumes order["coupon"] exists
    return order["coupon"]["amount"]


def finalize_order(order):
    """Compute the final total after coupons and tax."""
    subtotal = sum(i["price"] for i in order.get("items", []))
    discount = apply_coupon(order)
    return round(subtotal - discount, 2)
