import tweepy
import sys
import json
#import jsonpickle
import time
import os

API_KEY ='nXYbUBiJ6pV6yjvBn6p1F7bZj'
API_SECRET = 'TgQji0DpvMe6Ly1nPbLsZnwohaXTCcoUxBoEk0tGahIdTorJuE'

auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
                   wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

maxTweets = 2000 # Some arbitrary large number
tweetsPerQry = 100  # 100 is the max the API permits
start_time = time.time()

with open('xaa1', 'r') as f:
    for line in f:
        input = json.loads(line)
        # input['nick'] = [item.encode('ascii', 'ignore') for item in input['nick']]
        # input['name'] = input['name'].encode('ascii', 'ignore')
        all_list = []
        if len(input['name'].split(' ')) > 1:
            all_list.append(input['name'].encode('ascii', 'ignore'))
        
        c = 0
        for x in input['nick']:
            print "X",x
            if len(x.split(' ')) > 1 and c <= 2 :
                c += 1
                y = x.encode('ascii', 'ignore')
                all_list.append(y)
    
        hashtag_list = []
        
        for item in all_list:
        
            item = item.replace(" ", "")
            tag_item = "#" + item
  
            hashtag_list.append(tag_item)
        print hashtag_list
        
      
    
        all_list = list(set(all_list))
        hashtag_list = list(set(hashtag_list))
        searchQuery = ''+ '"' + all_list[0] + '"'
        # if len(input['nick']) >2:
        #     input['nick'] = input['nick'][:2]

        
        for x in all_list[1:]:
            searchQuery = searchQuery + ' ' + 'OR' + ' ' +  '"' + x + '"'

        for it in hashtag_list:
            searchQuery = searchQuery + ' ' + 'OR' + ' ' +  '"' + it + '"'
        

        #searchQuery = searchQuery + ' -filter: retweets'
        print(searchQuery)

        tweetCount = 0
        print("Downloading max {0} tweets".format(maxTweets))
        fName = input['id']+ '.jl'
        filePath = os.path.join('xxaa1', fName)


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
                    #print("Downloaded {0} tweets".format(tweetCount))

                except tweepy.TweepError as e:
                    # Just exit if any error
                    print("some error : " + str(e))
                    break
            if tweetCount == 0:
                os.remove(filePath)

        print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))
        print("--- %s mins passed ---" % (time.time() - start_time))

