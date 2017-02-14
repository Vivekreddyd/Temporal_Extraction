from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import re
import string
import os

# We use the file saved from last step as example
new_path='/home/vivek/Desktop/twitter_nlp-master/Cleaned_NER'
for root, dirs, files in os.walk('/home/vivek/Desktop/twitter_nlp-master/Ner'):
    for file in files:
        with open(os.path.join(root,file),'r') as tweets_file:
            tweets_new_file = open(os.path.join(new_path, file), "w")
            for line in tweets_file:
                if 'geo-loc' in line or 'facility' in line:
                    clean_line1 = re.sub('(\/O)', '', line)
                    tweets_new_file.write(clean_line1)
tweets_new_file.close()