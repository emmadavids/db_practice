from lib.post_repository import PostRepository
from lib.post import Post 


def test_get_all_posts(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new ArtistRepository

    posts = repository.all() # Get all artists

    # Assert on the results
    assert posts == [
        Post(1, 'My First Post', 'This is my first post.', 10, 1),
        Post(2, 'Second Post', 'This is my second post.', 5, 2)

    ]

def test_create_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.create(Post(3, "third post", "i am cool", 1, 10))
    result = repository.all()
    print(result)
    assert result == [
        Post(1, 'My First Post', 'This is my first post.', 10, 1),
        Post(2, 'Second Post', 'This is my second post.', 5, 2),
        Post(3, "third post", "i am cool", 10, 1) 
    ]

def test_delete_post(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new ArtistRepository
    repository.delete(1) # Get all artists
    # Assert on the results
    result = repository.all()
    assert result == [
        Post(2, 'Second Post', 'This is my second post.', 5, 2)]


