"""Smoke tests for ShopFast.

These verify the happy paths only. The bugs deliberately remain so Bug2PR
can find and fix them.
"""

import pytest

from app.users import get_username, get_user_email
from app.pricing import total_price, average_price, apply_tax
from app.checkout import finalize_order
from app.orders import latest_item, order_summary, ORDERS


def test_get_username_existing():
    assert get_username(1) == "alice"


def test_get_user_email_existing():
    assert get_user_email(1) == "alice@shopfast.com"


def test_get_user_email_missing():
    assert get_user_email(999) is None


def test_total_price():
    items = [{"price": 10.0}, {"price": 20.0}]
    assert total_price(items) == 30.0


def test_average_price_normal():
    assert average_price(100, 4) == 25.0


def test_apply_tax():
    assert apply_tax(100) == 108.0


def test_latest_item_normal():
    items = [{"name": "A"}, {"name": "B"}]
    assert latest_item(items) == {"name": "A"}


def test_order_summary():
    assert "2 items" in order_summary(101)
