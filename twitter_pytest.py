import pytest

from twitter import Twitter


@pytest.fixture(scope='function')
def twitter(request):
    twitter = Twitter()

    def fin():
        twitter.delete()

    request.addfinalizer(fin)
    yield twitter
    twitter.delete()


def test_twitter_initialization(twitter):
    assert twitter


def test_tweet_single_message(twitter):
    twitter.tweet('Test message')
    assert twitter.tweets == ['Test message']


def test_tweet_log_message(twitter):
    assert twitter
    with pytest.raises(Exception):
        twitter.tweet('test' * 41)
        assert twitter.tweets == []


@pytest.mark.parametrize("message, expected", (
        ("Test #first message", ['first']),
        ("#first Test message", ['first']),
        ("#FIRST Test message", ['first']),
        ("Test message #first", ['first']),
        ("Test message #first #second", ['first', 'second'])
))
def test_tweet_with_hashtag(twitter, message, expected):
    assert twitter.find_hashtags(message) == expected
