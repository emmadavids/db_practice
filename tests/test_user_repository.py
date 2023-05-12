from lib.users_repository import UserRepository
from lib.user import User 

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_users(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new ArtistRepository

    users = repository.all() # Get all artists

    # Assert on the results
    assert users == [
        User(1, 'John Doe', 'johndoe@example.com'),
        User(2, 'Jane Smith', 'janesmith@example.com'),

    ]

def test_create_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, "hello@iamcool.com", "Emma Davids"))
    result = repository.all()
    assert result == [
        User(1, 'John Doe', 'johndoe@example.com'),
        User(2, 'Jane Smith', 'janesmith@example.com'),
        User(3, "Emma Davids", "hello@iamcool.com")
    ]

def test_delete_user(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new ArtistRepository
    users = repository.delete(1) # Get all artists
    # Assert on the results
    result = repository.all()
    assert result == [
        User(2, 'Jane Smith', 'janesmith@example.com'),
    ]


