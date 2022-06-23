import requests as rq
import json
import tweepy

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

ACCESS_TOKEN = '881550360757673985-eFAcMbmRp1hQAdj41RLOp1PToMuZjbN'
ACCESS_SECRET = 'czR8da1CAyLH8f1o1XJ9wcvrRxEHdF0fCpusTtLb1UYSb'
CONSUMER_KEY = 'qxTtBqM4pgzCjHuUXRdOPoyir'
CONSUMER_SECRET = 'B886ulQc0m8S2mrCExwTpuFCFlfHra31PfIx08hXgh6sQ4q1C0'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

for status in tweepy.Cursor(api.home_timeline).items(1):
	jprint(status._json)

# op = rq.get("https://discord.com/api/webhooks/872902943328862228/Vbze14OBdy3jNDvjYcLdgroSlv1MltYEMHhfPKnVsXpW8Rfgl9CNSW12FdIvlbo38CJi")
# print(op)