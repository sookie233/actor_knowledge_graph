#reference:
# http://docs.tweepy.org/en/v3.5.0/api.html
#https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json
#https://cmry.github.io/notes/twitter-python
#http://adilmoujahid.com/posts/2014/07/twitter-analytics/


# https://github.com/ckoepp/TwitterSearch


import time
from TwitterSearch import *
import json
import os
import sys



def searchTweetsByKeyWords(kw,name):

        tso = TwitterSearchOrder()  # create a TwitterSearchOrder object

        # crawl tweets either has the name or the # @ username
        #print(kw)
        tso.set_keywords(kw, or_operator=True)
        # add is AND operator
        #tso.add_keyword('BMW')
        tso.set_language('en')
        tso.set_include_entities(False)  # and don't give us all those entity information
        querystr = tso.create_search_url()
        if len(kw) != 0:
            tso.set_search_url(querystr +'-filter: retweets' )
        #print(tso.create_search_url())
        # it's about time to create a TwitterSearch object with our secret tokens
        # ts = TwitterSearch(
        #     consumer_key='9xVWHkeN4y8cb5oeP9hik4GFa',
        #     consumer_secret = 'loj6sQP5SInVScFivb6Yue8wdxlBRyxP7QKxoktXk3xpx91u9Z',
        #     access_token = '4694615197-DehCfpvwO75IZx3Du3gBegdqjZ6RN2bFKmhHgWm',
        #     access_token_secret = '3q8NDWy215iSVokDyGJrtEDwEMRd6eTN2GNXBg6lLeZwE'
        # )

        ts = TwitterSearch(
            consumer_key='8uuk3plC47kh3x0gn6we8mTPN',
            consumer_secret = 'HID1X3Ou4CB4NkSYGBGh1v7HzQBiHsxzMwrHFTdZSSRdFC3S6N',
            access_token = '928393174019538945-7qSMGouZkWs6Zu2F1s3lZaeigq9xzt7',
            access_token_secret = 'APXG9GVFn6C04bPzyBGppuBalMl6CPgI5dLmrJqwYLDMg'
        )


        filename = name + '.jl'
        filepath = os.path.join('new_tweets', filename)
        f = open(filepath, 'w')

        # avoid rate limitation manually
        sleep_for = 30  # sleep for 60 seconds
        last_amount_of_queries = 0  # used to detect when new queries are done

        tweetCount = 0
        for tweet in ts.search_tweets_iterable(tso):
            keys =['time','text']
            values = [tweet['created_at'],tweet['text']]
            tweets = dict(zip(keys,values))
            tweetCount += len(tweets)/2

            json.dump(tweets, f)
            f.write('\n')



        f.close()
        if tweetCount == 0:
            os.remove(filepath)
        print("--- %s mins passed ---" % ((time.time() - start_time) / 60.0))
        print("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fname))
        current_amount_of_queries = ts.get_statistics()[0]
        if not last_amount_of_queries == current_amount_of_queries:
            last_amount_of_queries = current_amount_of_queries
            time.sleep(sleep_for)
        #return tweet



if __name__ == '__main__':
    start_time = time.time()


    with open('twitter_names_all.jl', 'r') as f:
        for line in f:
            input = json.loads(line)

            # input['nick'] = [item.encode('ascii', 'ignore') for item in input['nick']]
            # input['name'] = input['name'].encode('ascii', 'ignore')

            input['nick'] = [item for item in input['nick']]
            input['name'] = input['name']

            name_list = []

            # if len(input['name'].split(' ')) != 1:
            name_list.append(input['name'])
            if len(input['nick']) == 1:

                for x in input['nick']:
                    if len(x.split(' ')) == 1:
                        print(name_list)


            else:
                name_list.extend(input['nick'])
                print( name_list)
            fname = input['id']
            searchTweetsByKeyWords(name_list,fname)


# 2000 tweets in 30 secs








'''




 # add # of page will get more tweets, 20 tweets(status) for each page
 for i in range(1,4):
     tweets= api.user_timeline(id =user.id,page = i)
     twitters.extend(tweets)



 print (len(twitters))

 i= 1
 for one_tweet in twitters:

     print('1111111111111111111111111111111\n')
     print(i)
     print(one_tweet)
     i=i+1

     #print(one_tweet.reply_count)
     print(one_tweet.retweet_count)
     #favorite_count == 0 if it's a retweet
     print(one_tweet.favorite_count)


'''


