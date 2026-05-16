"""ShopFast Flask app — buggy on purpose for Bug2PR demos.

Run:
    pip install -r requirements.txt
    python main.py

Then visit http://127.0.0.1:5050/ for the route list.
"""

import sys
import traceback

from flask import Flask, request, jsonify

from app.users import get_username, USERS
from app.pricing import average_price
from app.checkout import apply_coupon
from app.orders import latest_item, ORDERS

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "app": "ShopFast",
        "version": "0.1.0-buggy",
        "routes": [
            {"path": "/user/99",   "bug": "AttributeError on None.username"},
            {"path": "/price/0",   "bug": "ZeroDivisionError"},
            {"path": "/coupon",    "bug": "KeyError on 'coupon'"},
            {"path": "/items/5",   "bug": "IndexError"},
        ],
    })


@app.route("/user/<int:user_id>")
def user_endpoint(user_id):
    return jsonify({"username": get_username(user_id)})


@app.route("/price/<int:count>")
def price_endpoint(count):
    return jsonify({"avg": average_price(100, count)})


@app.route("/coupon")
def coupon_endpoint():
    order = {"id": 42, "items": [{"price": 9.99}]}  # no 'coupon' key
    return jsonify({"discount": apply_coupon(order)})


@app.route("/items/<int:idx>")
def items_endpoint(idx):
    return jsonify({"item": latest_item(ORDERS[102]["items"], idx)})


@app.errorhandler(Exception)
def on_error(exc):
    tb = traceback.format_exc()
    print("\n" + "=" * 60, file=sys.stderr)
    print("🐛 Copy this traceback into Bug2PR:", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    print(tb, file=sys.stderr)
    return jsonify({"error": str(exc), "traceback": tb}), 500


if __name__ == "__main__":
    print("🛒 ShopFast running at http://127.0.0.1:5050")
    app.run(host="127.0.0.1", port=5050, debug=False)
