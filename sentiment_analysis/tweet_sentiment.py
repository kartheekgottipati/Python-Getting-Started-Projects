import tweepy
from textblob import TextBlob
import re


class TweetSentiment(object):
	
	def __init__(self, access_control=None):
		consumer_key = access_control['consumer_key']
		consumer_secret = access_control['consumer_secret']
		access_token = access_control['access_token']
		access_token_secret = access_control['access_token_secret']

		try:
			auth = tweepy.OAuthHandler(consumer_key, consumer_secret)	
			auth.set_access_token(access_token, access_token_secret)
			self.api = tweepy.API(auth)
		except tweepy.TweepError:
			print(TweepError.message[0]['code'])

	def clean_tweet(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

	def get_tweet_sentiment(self, tweet):
		analysis = TextBlob(self.clean_tweet(tweet))
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'

	def get_tweets(self,tag):
		tweets = []
		try:
			fetched_tweets = self.api.search(q=tag,count = 1000)
			for tweet in fetched_tweets:
				parsed_tweet = {}
				parsed_tweet['text'] = tweet.text
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
				
				if tweet.retweet_count > 0:
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)
			return tweets

		except tweepy.TweepError as e:
			print("Error : " + str(e))

def main():
	access_control = {}
	access_control['consumer_key'] = "vlqIOTCPSUa16Jpd2HAxnIDMB"
	access_control['consumer_secret'] = "IMXn7Px0DiF3n3IGhY69XY1wSbhupAtN33eiaeIw3brW3u1cEe"
	access_control['access_token'] = "446967813-tgnc1K4QuzSEb6RVkOGy1R1NY2LmDP52MapkFAWa"
	access_control['access_token_secret'] = "c1MZGPsNGQvgn1MkeT5uwZJpU2W4pkScYA0doR0z1xCT3" 	

	api = TweetSentiment(access_control=access_control) 
	tweets = api.get_tweets('MeToo')
	positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

	print("Positive tweets percentage: {} %".format(100*len(positive_tweets)/len(tweets)))
    
	negative_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    
	print("Negative tweets percentage: {} %".format(100*len(negative_tweets)/len(tweets)))
    
	print("Neutral tweets percentage: {} % \
        ".format(100*(len(tweets) - len(positive_tweets) - len(negative_tweets))/len(tweets)))

if __name__ == "__main__":
    main()