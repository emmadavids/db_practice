from lib.post import Post


def test_post_constructs():
    post = Post(1, "hello world", "i am cool", 2, 0)
    assert post.user_id == 2
    assert post.id == 1
    assert post.title == "hello world"
    assert post.content == "i am cool"
    assert post.views == 0

def test_post_format_nicely():
    post = Post(1, "hello world", "i am cool", 2, 0)
    assert str(post) == "Post(1, hello world, i am cool, 0, 2)"
    
def test_posts_are_equal():
    post1 = Post(1, "hello world", "i am cool", 0, 2)
    post2 = Post(1, "hello world", "i am cool", 0, 2)
    assert post1 == post2

