"""Orders module.

⚠️  Contains the `index_error` demo bug: latest_item() indexes a list
without checking length, raising IndexError on empty carts.
"""

ORDERS = {
    101: {"items": [{"name": "Widget", "price": 9.99},
                    {"name": "Gadget", "price": 14.99}]},
    102: {"items": []},  # empty — triggers the bug
}


def latest_item(items, idx=0):
    """Return the item at position `idx` in the items list."""
    # BUG: no bounds check
    return items[idx]


def order_summary(order_id):
    """Return a one-line summary of an order."""
    order = ORDERS.get(order_id)
    if not order:
        return f"Order #{order_id} not found"
    return f"Order #{order_id}: {len(order['items'])} items"
