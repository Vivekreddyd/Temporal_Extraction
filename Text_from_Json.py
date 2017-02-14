from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import re
import string
import os

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# We use the file saved from last step as example
new_path='/home/vivek/tweepy_dataset/Text_only_old'
tweets_new_file = open(os.path.join(new_path,"combined"), "w")
for root, dirs, files in os.walk('/home/vivek/tweepy_dataset/old'):
    for file in files:
        with open(os.path.join(root,file),"r") as tweets_file:
            #tweets_filename = '/home/vivek/tweepy_dataset/trip.009.txt'
            for line in tweets_file:
                try:
                    # Read in one line of the file, convert it into a json object
                    tweet = json.loads(line.strip())
                    #print tweet['text'] # content of the tweet
                    if 'text' in tweet: # only messages contains 'text' field is a tweet
                        #print tweet['id'] # This is the tweet's id
                        #print tweet['created_at'] # when the tweet posted
                        tweet_line=tweet['text']
                        clean_line = re.sub('(\n)', ' [NEW LINE] ', tweet_line)
                        #print clean_line
                        tweets_new_file.write(clean_line.encode('utf8'))
                        tweets_new_file.write("\n")
                except:
                    # read in a line is not in JSON format (sometimes error occured)
                    continue
