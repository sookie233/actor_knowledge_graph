import tweepy
import sys
import json
import jsonpickle
import time
import os
# Replace the API_KEY and API_SECRET with your application's key and secret.
#https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./
#https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
#http://docs.tweepy.org/en/v3.5.0/api.html#status-methods
#https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/basic-operators
API_KEY ='9xVWHkeN4y8cb5oeP9hik4GFa'
API_SECRET = 'loj6sQP5SInVScFivb6Yue8wdxlBRyxP7QKxoktXk3xpx91u9Z'
auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

maxTweets = 2000 # Some arbitrary large number
tweetsPerQry = 100  # 100 is the max the API permits
start_time = time.time()

with open('twitter_names.jl', 'r') as f:
    for line in f:
        input = json.loads(line)
        # input['nick'] = [item.encode('ascii', 'ignore') for item in input['nick']]
        # input['name'] = input['name'].encode('ascii', 'ignore')

        name_list = []
        print(type(input['nick']),type(input['name']))
        name_list.append(input['name'])
        searchQuery = ''+ '"' + input['name'] + '"'
        if len(input['nick']) == 1:

            for x in input['nick']:
                if len(x.split(' ')) == 1:
                    print(name_list)
        else:
            #name_list.extend(input['nick'])
            #print(name_list)
            for nickname in input['nick']:
                searchQuery = searchQuery + ' ' + 'OR' + ' ' +  '"' + nickname + '"'


        searchQuery = searchQuery + ' -filter: retweets'
        print(searchQuery)

        tweetCount = 0
        print("Downloading max {0} tweets".format(maxTweets))
        fName = input['id']+ '.jl'
        filePath = os.path.join('restAPI_tweets', fName)


        with open(filePath, 'w') as f:
            while tweetCount < maxTweets:
                try:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,lang = 'en')
                    if not new_tweets:
                        print("No more tweets found")
                        break
                    for tweet in new_tweets:
                        #print(tweet._json)
                        keys = ['time', 'text']
                        values = [tweet._json['created_at'], tweet._json['text']]
                        tweets = dict(zip(keys, values))

                        json.dump(tweets, f)
                        f.write('\n')
                    tweetCount += len(new_tweets)
                    print("Downloaded {0} tweets".format(tweetCount))

                except tweepy.TweepError as e:
                    # Just exit if any error
                    print("some error : " + str(e))
                    break
            if tweetCount == 0:
                os.remove(filePath)

        print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))
        print("--- %s mins passed ---" % (time.time() - start_time))

