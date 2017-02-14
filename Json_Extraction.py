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
new_path='/home/vivek/tweepy_dataset/Text_cleaned'
for root, dirs, files in os.walk('/home/vivek/tweepy_dataset/Text_only'):
    for file in files:
        with open(os.path.join(root,file),"r") as tweets_file:
            #tweets_filename = '/home/vivek/tweepy_dataset/trip.009.txt'
            tweets_new_file = open(os.path.join(new_path,file), "w")
            prev_line=None
            for line in tweets_file:
                try:
                    # Read in one line of the file, convert it into a json object
                    tweet = json.loads(line.strip())
                    #print tweet['text'] # content of the tweet
                    if 'text' in tweet: # only messages contains 'text' field is a tweet
                        #print tweet['id'] # This is the tweet's id
                        #print tweet['created_at'] # when the tweet posted
                        line = tweet['text']
                        # Delete the tweet if it is a retweet
                        if 'RT' in line or not '#travel' in line:
                            continue
                        #clean_line=re.sub('#.* ?','',line)
                        clean_line=line
                        #print clean_line
                        # Replace the https with [URL]
                        clean_line1 = re.sub('(\n)', ' [NEW LINE] ', clean_line)
                        clean_line1=re.sub('(https.*?( |\t|\n|\r|\f|\v|$))',' [URL] ',clean_line1)
                        #printable = set(string.printable)
                        #clean_line2=filter(lambda x: x in printable, clean_line1)
                        clean_line2=clean_line1
                        length=len(clean_line2)
                        if (len(clean_line2.split())<3):
                            continue
                        #print clean_line2
                        tweets_new_file.write(clean_line2.encode('utf8'))
                        tweets_new_file.write("\n")
                        print clean_line2
                        #clean_line2=re.compile("["u"\U0001F600-\U0001F64F"u"\U0001F300-\U0001F5FF"u"\U0001F680-\U0001F6FF"u"\U0001F1E0-\U0001F1FF""]+", flags=re.UNICODE)
                        #print (clean_line2.sub(r'', clean_line1))

                        #print tweet['text'] # content of the tweet
                        #print tweet['user']['id'] # id of the user who posted the tweet
                        #print tweet['user']['name'] # name of the user, e.g. "Wei Xu"
                        #print tweet['user']['screen_name'] # name of the user account, e.g. "cocoweixu"

                    '''hashtags = []
                        for hashtag in tweet['entities']['hashtags']:
                            hashtags.append(hashtag['text'])
                        #print hashtags'''

                except:
                    # read in a line is not in JSON format (sometimes error occured)
                    continue
                prev_line=line
            tweets_new_file.close()

