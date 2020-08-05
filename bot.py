import twitter
import config 

api = twitter.Api(consumer_key=config.CONSUMER_KEY,
                  consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_TOKEN_KEY,
                  access_token_secret=config.ACCESS_TOKEN_SECRET)

status = api.PostUpdate('Stonk', media='./tendies.jpeg')  
print(status)
print(status.text)