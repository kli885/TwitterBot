import random
import tweepy #update_status
import json  #builtin
def tweet(api):
	with open('tweets.json', 'r') as f:
		all_message = f.readlines()
		while True:
			message = random.choice(all_message)
			json_data = json.loads(message)
			if 'text' in json_data:
				status = json_data['text']
				newstatus = status.replace("@","*")
				break	
		api.update_status(newstatus)