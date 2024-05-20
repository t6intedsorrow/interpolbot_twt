import os
import tweepy
import json
import random

with open('quotes.json', 'r', encoding='utf-8') as quotes_file:
    data = json.load(quotes)
except UnicodeDecodeError as e:
    print(f"Error decoding file: {e}")
    data = {}
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    data = {}
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    data = {}
def post_quote():
    if not data:
        print("No data to post.")
        return
    
    key = random.choice(list(data.keys()))
    quotes = data[key]
    random_index = random.randint(0, len(quotes) - 1)
    quote = quotes[random_index]
    
    try:
        r = bot.create_tweet(text=quote)
        print("Tweet posted successfully.")
    except tweepy.TweepError as e:
        print(f"Error posting tweet: {e}")
        if e.api_code == 401:
            print("Unauthorized error: Check your credentials and permissions.")
        else:
		
bot = tweepy.Client(
    #Consumer Keys
    consumer_key= os.environ['CONSUMER_KEY'],
    consumer_secret= os.environ['CONSUMER_SECRET'],
    # Access Token and Secret
    access_token= os.environ['ACCESS_TOKEN'],
    access_token_secret= os.environ['ACCESS_TOKEN_SECRET'])

def post_quote():
	key = random.choice(list(data.keys()))
	quotes = data[key]
	random_index = random.randint(0, len(quotes)-1)
	quote = quotes[random_index]
	try:
		r = bot.create_tweet(text=quote)
	except:
		random_index = random.randint(0, len(quotes)-1)
		quote = quotes[random_index]
		r = bot.create_tweet(text=quote)
	return None
