import schedule #download
import time
import os
import sys 
from dotenv import load_dotenv #download
import webbrowser #builtin
import requests_oauthlib #API
import tweepy #API
from tweet import tweet 
from markov_tweet import markov_tweet

def main():
	load_dotenv("APIKEY.env")
	CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
	CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
	callback_uri="https://127.0.0.1.com?source=twitter"
	url = "https://api.twitter.com/oauth/request_token"
	oauth = requests_oauthlib.OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET)
	fetch_response = oauth.fetch_request_token(url)
	base_authorization_url = 'https://api.twitter.com/oauth/authorize'
	access_token_url = 'https://api.twitter.com/oauth/access_token'
	authorization_url = oauth.authorization_url(base_authorization_url)

	while True:
		webbrowser.open(authorization_url)
		user_url = input("Copy url down below after authenticating\n")
		if user_url == authorization_url:
			print("Please authorize first")
		elif user_url == base_authorization_url:
			print("You have cancelled it, please run the program again")
		else:
			break
		time.sleep(1)
		os.system("clear")

	response_oauth = oauth.parse_authorization_response(user_url)
	info = oauth.fetch_access_token(access_token_url)
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(info.get("oauth_token"), info.get("oauth_token_secret"))
	api = tweepy.API(auth)
	format_continue = True
	while format_continue is True:
		tweet_format = input("Which tweet pattern would you like to use?\n1.Random line selection\n2.Markov Chain\n")
		if tweet_format == "1":
			print("Posting...")
			schedule.every(5).seconds.do(tweet,api=api)
			break
		elif tweet_format == "2":
			print("Posting...")
			schedule.every(5).seconds.do(markov_tweet,api=api)
			break
		else:
			print("Please enter a valid answer")
			os.system("clear")
	while True:
		schedule.run_pending()
		time.sleep(1)
main()

#alternative approach
	# consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
	# client = oauth.Client(consumer)
	# request_token_uri="https://api.twitter.com/oauth/request_token"
	# body = urllib.parse.urlencode(dict(oauth_callback=callback_uri))
	# resp, content = client.request(request_token_uri,'POST',body=body)
	# info = content.decode("utf-8")
	# info_list = str.split(info,"&")
	# authorization_url = "https://api.twitter.com/oauth/authorize?%s" % (info_list[0])



