from lib.user import User

"""
Artist constructs with an id, name and genre
"""
def test_user_constructs():
    user = User(1, "email@email.com", "Emma")
    assert user.id == 1
    assert user.email == "email@email.com"
    assert user.name == "Emma"

"""
We can format artists to strings nicely
# """
def test_user_format_nicely():
    user = User(1, "email@email.com", "Emma")
    assert str(user) == "User(1, Emma, email@email.com)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

# """
# We can compare two identical artists
# And have them be equal
# """
def test_users_are_equal():
    user1 = User(1, "email@email.com", "Emma")
    user2 = User(1, "email@email.com", "Emma")
    assert user1 == user2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
