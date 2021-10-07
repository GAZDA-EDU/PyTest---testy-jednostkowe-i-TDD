import pytest

from twitter import Twitter

def test_twitter_initialization():
    twitter = Twitter()
    assert twitter

def test_tweet_single_message():
    twitter = Twitter()
    twitter.tweet('Test message')
    assert twitter.tweets == ['Test message']

def test_tweet_log_message():
    twitter = Twitter()
    assert twitter
    with pytest.raises(Exception):
        twitter.tweet('test'*41)
        assert twitter.tweets == []

