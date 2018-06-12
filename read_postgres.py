import psycopg2


class Tweet(object):
    """ Holds a Twitter tweet and its properties

    """
    def __init__(self, record):
        print("Created a tweet")
    
    def __repr__(self):
        return "Tweet"


def connect_to_db():
    try:
        conn = psycopg2.connect("dbname='my_postgres_db' user='postgres_user' host='localhost' password='password'")
    except:
        print("Unable to connect to the database")
    return conn.cursor()


def run():
    cursor = connect_to_db()
    cursor.execute("SELECT * FROM tweets")
    results = cursor.fetchall()

    tweets = []
    for record in results:
        tweets.append(Tweet(record))

    print(tweets)


if __name__ == '__main__':
    run()
