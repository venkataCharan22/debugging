from app.users import get_username

def test_get_username():
    user = {"username": "test_user"}
    assert get_username(user) == "test_user"

def test_get_username_none():
    user = None
    try:
        get_username(user)
        assert False, "Expected AttributeError"
    except AttributeError as e:
        assert str(e) == "'NoneType' object has no attribute 'username'"