import time,datetime

from time import sleep
from Keys import *
import tweepy
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME
# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(Access_Token, Access_Token_Secret)
api = tweepy.API(auth)
print("Twitter bot which retweets, like tweets and follow users")
print("Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)

for tweet in tweepy.Cursor(api.search, q=QUERY).items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        if LIKE:
            tweet.favorite()
            print('Favorited the tweet')

        # Follow the user who tweeted
        # check that bot is not already following the user
        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print('Followed the user')

        sleep(SLEEP_TIME)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

