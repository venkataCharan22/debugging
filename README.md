# debugging — ShopFast Buggy App for Bug2PR Demos

A deliberately buggy Flask app used as the target repository for
[**Bug2PR**](https://github.com/yourorg/AI_Debugging) — an autonomous
bug-to-PR pipeline powered by IBM Bob.

When the user pastes a stack trace into the Bug2PR War Room, the agents:
1. Locate the bug in this repo
2. Write a fix
3. Generate a regression test
4. Audit for security issues
5. **Open a pull request HERE** — see [Pull requests tab](../../pulls).

## Five staged bugs

| File              | Function        | Bug type            | Trigger              |
|-------------------|-----------------|---------------------|----------------------|
| `app/users.py`    | `get_username`  | `AttributeError`    | `GET /user/99`       |
| `app/pricing.py`  | `average_price` | `ZeroDivisionError` | `GET /price/0`       |
| `app/checkout.py` | `apply_coupon`  | `KeyError`          | `GET /coupon`        |
| `app/orders.py`   | `latest_item`   | `IndexError`        | `GET /items/5`       |
| (combined)        |                 |                     | many                 |

## Run locally

```bash
pip install -r requirements.txt
python main.py
# open http://127.0.0.1:5050
```

Hit any of the buggy routes — the traceback is printed to your terminal
between `===` banners. Copy that traceback into the Bug2PR War Room and
watch IBM Bob open a real PR here that fixes it.

## Run the (working) smoke tests

```bash
pytest tests/ -v
```

These pass — they only cover the happy paths. The bugs remain so Bug2PR
can find them.

---

*PRs in this repository are generated automatically by Bug2PR.*
*See the parent project: `AI_Debugging/Bug2PR`.*
