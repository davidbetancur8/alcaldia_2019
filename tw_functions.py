import tweepy
import time
import re
import io
import csv


def autenticar():
    keys = dict(
        consumer_key =          'consumer_key',
        consumer_secret =       'consumer_secret',
        access_token =          'access_token',
        access_token_secret =   'access_token_secret',
    )

    CONSUMER_KEY = keys['consumer_key']
    CONSUMER_SECRET = keys['consumer_secret']
    ACCESS_TOKEN = keys['access_token']
    ACCESS_TOKEN_SECRET = keys['access_token_secret']

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

