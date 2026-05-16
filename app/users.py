"""User lookup module.

⚠️  Contains the `null_user` demo bug: get_username() crashes when the
user_id isn't in USERS because we don't check for None before
accessing `.username`.
"""

USERS = {
    1: {"id": 1, "username": "Alice",   "email": "alice@shopfast.com"},
    2: {"id": 2, "username": "Bob",     "email": "bob@shopfast.com"},
    3: {"id": 3, "username": "Charlie", "email": "charlie@shopfast.com"},
}


def get_username(user_id):
    """Return the lowercased username for a given user id."""
    user = USERS.get(user_id)
    # BUG: missing None check — crashes for unknown user_id
    return user["username"].lower()


def get_user_email(user_id):
    """Return the user's email address."""
    user = USERS.get(user_id)
    if user is None:
        return None
    return user["email"]
