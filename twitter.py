"""
Never Again Twitter client.
"""
import logging
import tweepy

def _limit_handled(cursor):
    """ Handles Twitter API rate limits. """
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError as err:
            logging.warning('Twitter API RATE LIMIT exceeced.')
            raise err
        except StopIteration:
            # No more items to handle, stream ended
            break

class Twitter():

    def __init__(self, auth) -> None:
        self.api = tweepy.API(auth)

    def _get_tweet_html(self, tweet_id):
        """ Gets the tweet idenfitied by given tweet_id in HTML format. """
        logging.info('rendering tweet ' + str(tweet_id))
        oembed = self.api.get_oembed(id=tweet_id, hide_media=False, hide_thread=True, omit_script=True)
        tweet_html = oembed['html'].strip("\n")
        return tweet_html

    def show_tweets(self, limit=10):
        """ Renders the HTML for most recent tweets of the user."""
        for tweet in _limit_handled(tweepy.Cursor(self.api.user_timeline).items(limit=limit)):
            yield (self._get_tweet_html(tweet.id))
