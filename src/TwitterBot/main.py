import tweepy
import schedule
import time
import random
import os
from dotenv import load_dotenv

def main():
	load_dotenv("APIKEY.env")
	CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
	CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
	ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
	ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

	api = tweepy.API(auth)
	public_tweets = api.update_status("Testing %d" % random.randint(1,100))

def my_time():
	schedule.every(5).seconds.do(main)
	while True:
		schedule.run_pending()
		time.sleep(1)

my_time()

	# try:
	# 	redirect_url = auth.get_authorization_url()
	# except tweepy.TweepError:
	# 	print('Error! Failed to get request token.')

	# session.set('request_token', auth.request_token['oauth_token'])



