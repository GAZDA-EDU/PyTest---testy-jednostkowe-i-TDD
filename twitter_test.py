import unittest
from twitter import Twitter

class TwitterTest(unittest.TestCase):
    def test_initialization(self):
        twitter = Twitter()
        self.assertTrue(twitter)

    def test_tweet_single(self):
        # Given
        twitter = Twitter()
        # When
        twitter.tweet('Test message')
        # Then
        self.assertEqual(twitter.tweets, ['Test message'])

if __name__ == '__main__':
    unittest.main()
