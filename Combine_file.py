from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import re
import string
import os

# We use the file saved from last step as example
new_path='/home/vivek/Desktop/twitter_nlp-master/Text'
tweets_new_file = open(os.path.join(new_path, "combined_text"), "w")
for root, dirs, files in os.walk('/home/vivek/Desktop/twitter_nlp-master/Text'):
    for file in files:
        with open(os.path.join(root,file),'r') as tweets_file:
            for line in tweets_file:
                tweets_new_file.write(line)
tweets_new_file.close()