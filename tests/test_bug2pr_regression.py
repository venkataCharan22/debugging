from app.users import User

def test_user_object_initialization():
    user = User("test_username", "test_email")
    assert user.username is not None
    assert user.username == "test_username"

    user = None
    try:
        print(user.username)
        assert False, "Expected AttributeError"
    except AttributeError as e:
        assert True

    user = User(None, None)
    assert user.username is not None or user.username == ""