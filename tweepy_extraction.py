from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

#consumer key, consumer secret, access token, access secret.
atoken = '783400224165199872-kgNb2YtnttraUcYzmU4iR50svxInBdx'
asecret = 'iekjm2cl7rDf7adqq9zpM3c6PtINrovchMTHSFXdrvnVi'
ckey = 'DlDUZRL2bue1Kw0Ld0nyrjWwk'
csecret = 'kySRM6sGxGGvNRfFH81So4Ue5C2e93cZSo1JLGiS5HkXrD5Pk0'
output_file = open("/home/vivek/Tweepy/travel_new10.txt", "a")
class listener(StreamListener):

    def on_data(self, data):
        print(data)
        output_file.write(data)
        #time.sleep(5)
        return(True)

    def on_error(self, status):
        print status
        time.sleep(900)
        return(True)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#travel"])