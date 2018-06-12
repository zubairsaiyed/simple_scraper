import psycopg2
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""

TWEET_COUNT = 30



class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def __init__(self):
        super(StdOutListener, self).__init__()
        self.count = 0

    def on_status(self, status):
        print('{} [{}]'.format(status.text, status.user.screen_name))
        self.count += 1
        if self.count == TWEET_COUNT:
            return False

    def on_error(self, status):
        print(status)


class DBWriterListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a listener that persists tweets to a database.

    """
    def __init__(self):
        super(DBWriterListener, self).__init__()
        self.count = 0
        try:
            self.conn = psycopg2.connect("dbname='my_postgres_db' user='postgres_user' host='localhost' password='password'")
        except:
            print("Unable to connect to the database")
        self.cursor = self.conn.cursor()

    def on_status(self, status):
        print('{} [{}]'.format(status.text, status.user.screen_name))
        self.cursor.execute("""
            INSERT INTO tweets (screenname, text, lang, created_at)
            VALUES (%s,%s,%s,%s)
            """,
            (status.user.screen_name, status.text, status.lang, status.created_at))
        self.count += 1
        if self.count == TWEET_COUNT:
            self.conn.commit()
            return False

    def on_error(self, status):
        print(status)


def run():
    listener = StdOutListener()
    # listener = DBWriterListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listener)
    stream.filter(track=['disney'])


if __name__ == '__main__':
    run()
