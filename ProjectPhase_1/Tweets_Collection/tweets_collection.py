from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json, time, sys , tweepy
import re
import unicodedata
import codecs
#customer keys
consumer_key = 'yGRxlXyDG39iHr1akrN0zRU9F'
consumer_secret = '4LiY6VeolUtPPaV9dmEsh6jJvvXCAcGpHXIrbQZaxHpcc0ANMt'
access_key = '3700831395-31MrA3aG8vPRWlKzA2eu8dONZ7GhGfso2AuUe9g'
access_secret = 'ft3LSqsjk8hEe7AABYG5uga9320mLoOTZIA0yPGI6iwY1'
#auth keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
#stream listener
class StdOutListener(StreamListener):

    def on_status(self, status):
        twit_id = status.id

        text = status.text

        created = status.created_at

        time_zone = status.user.time_zone

        location = status.user.location

        language = status.lang

        hashtags = re.findall(r"#(\w+)" , text)

        for tag in hashtags:
           record = unicode(twit_id) + '\t' +  unicode(created) + '\t' + unicode(language) + '\t' + unicode(location)  + '\t' + unicode(time_zone) + '\t' +  unicode(tag) + '\t' + unicode(text) + '\t'

           tweetfile = codecs.open('sampletweets4.txt' , 'a' , 'utf8')

           tweetfile.write(unicode(record))
           #new line for every tweet
           tweetfile.write('\n')
           #close tweet file
           tweetfile.close()

        return True

    def on_error(self, status):
        print 'Error on status', status

    def on_limit(self, status):
        print 'Limit threshold exceeded', status

    def on_timeout(self, status):
        print 'Stream disconnected; continuing...'

stream = Stream(auth, StdOutListener())

stream.filter(track = ['#NFL', '#football', '#baseball', '#royals', '#seattlemariners', '@tamba', '#Orioles', '#Yankees', '#marlins', '#redsox', '#MLB', '@StarSports', '#FMRedHawks', '@USABaseball', '@ForrestWhitley', '@MickeyMoniak', '@colestobbe', '#USAbaseball', '@baseball', 'Bryce Harper', 'Albert Pujols', 'David Ortiz', 'Alex Rodriguez', 'Derek Jeter', 'Clayton Kershaw', 'Andrew McCutchen', 'Yasiel Puig', 'Miguel Cabrera', 'Mike Trout', 'Johnny Bench', '#sports', '#kcroyals', 'pirates', 'rockies', 'sports', '#indians', '#twins', '#gaints', '#padres', '#marlins', '#phillies', '#royals', '#mariners', '#cardinals', '#brewers', '#mets', '#reds', '#pirates', '#rockies', '#rangers', '#athletics', '#whitesox', '#yankees', '#orioles', '#nationals', '#dodgers', '#diamondbacks', '#rays', '#redsox', '#mariners', '#angels', '#LaMarcus Aldridge', '#Carmelo Anthony', '#Harrison Barnes', '#Boston Celtics', '#brooklyn nets', '#houston rockets', '#new york knicks'
])
