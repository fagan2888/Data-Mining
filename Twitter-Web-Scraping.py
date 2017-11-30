from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#consumer key, consumer secret, access token, access secret.
ckey=" "
csecret=" "
atoken=" "
asecret=" "

class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        user = all_data["user"]
        screen_name = user["screen_name"]
        tweet = all_data["text"]
        print(screen_name, ' -> ', tweet)
        return True
    
    def on_error(self, status):
        print('Wait a few minutes and try again, Error Code:', status)
        return(False)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Adylkuzz"])  # keyword for live posts (est 30secs live)
