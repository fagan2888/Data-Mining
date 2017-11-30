from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#consumer key, consumer secret, access token, access secret.
ckey=" "
csecret=" "
atoken=" "
asecret=" "

class listener(StreamListener):
    def on_data(self, data):
        print('\n',data)
        return(True)
    def on_error(self, status):
        print('Wait a few minutes and try again, Error Code:', status)
        return(False)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Adylkuzz"])  # keyword for live posts (est 30secs live)
