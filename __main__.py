import tweepy, configparser, urllib.request, random

words = open('./words.txt').read().splitlines()

config = configparser.ConfigParser()
config.read('.config')

auth = tweepy.OAuthHandler(config['TWITTER']['consumer_key'], config['TWITTER']['consumer_secret'])
auth.set_access_token(config['TWITTER']['access_token'], config['TWITTER']['access_token_secret'])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
my_dms = api.list_direct_messages()

current_tweet = ""
current_dm = ""
tweets = {}

# while True:
if public_tweets[0].text != current_tweet:
  # generate random word
  random_key = random.choice(words)

  # add it to key-value pair
  tweets[random_key] = {'id': public_tweets[0].id, 'text': public_tweets[0].text}
  current_tweet = public_tweets[0].text

  # DM it to me
  api.send_direct_message(1450411, f'{random_key}: {current_tweet}')

# if DM does not equal most recent dm...
if my_dms[0].message_create['message_data']['text'] != current_dm:
  current_dm = my_dms[0].message_create['message_data']['text']
  # if DM word is in dict...
  print(current_dm)
  print("????")
  if current_dm in tweets.keys():
    # retweet the tweet
    api.retweet(tweets[current_dm]['id'])
    # reply with a thumbs up
    api.send_direct_message(1450411, f'👍 {current_dm}')


# sleep 1 seconds

