import json

tw = open('farmers-protest-tweets-2021-03-5.json', 'r')

data = json.load(tw)

for tweet in data:
    print(tweet)

tw.close()