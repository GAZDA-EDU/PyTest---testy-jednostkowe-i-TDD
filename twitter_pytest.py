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


def test_tweet_with_hashtag():
    twitter = Twitter()
    message = "Test #first message"
    assert 'first' in twitter.find_hashtags(message)

def test_tweet_with_hashtag_on_beginning():
    twitter = Twitter()
    message = "#first Test message"
    assert 'first' in twitter.find_hashtags(message)

def test_tweet_with_hashtag_uppercase():
    twitter = Twitter()
    message = "#FIRST Test message"
    assert 'FIRST' in twitter.find_hashtags(message)