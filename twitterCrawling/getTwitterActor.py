import tweepy
from tweepy import OAuthHandler
import time
import json



def getTwitterActor(name):

    user_info = []
    user = api.get_user(name)
    if user:

        keys = ['name','screenname','following','followers','likes']
        user_info.extend([user.name, user.screen_name,  user.friends_count, user.followers_count, user.favourites_count])
        user_info = dict(zip(keys, user_info))
        return user_info
    else :return None




if __name__ == '__main__':
    start_time = time.time()
    consumer_key = '9xVWHkeN4y8cb5oeP9hik4GFa'
    consumer_secret = 'loj6sQP5SInVScFivb6Yue8wdxlBRyxP7QKxoktXk3xpx91u9Z'
    access_token = '4694615197-DehCfpvwO75IZx3Du3gBegdqjZ6RN2bFKmhHgWm'
    access_secret = '3q8NDWy215iSVokDyGJrtEDwEMRd6eTN2GNXBg6lLeZwE'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)


    test_list = ['realbritt_rob']
    test_list = ['RobertDowneyJr','Renner4Real','ChrisEvans','chrishemsworth']
    file_name = 'part-00000'



    with open( 'twitter_users4.jl','w') as output:
        with open (file_name,'r') as f:
            for line in f:
                input = json.loads(line)

                if input['name']:
                    if '?' in input['name']:

                        pos = input['name'].index('?')
                        input['name'] = input['name'][:pos]
                    ans = getTwitterActor(input['name'])
                    d = {}
                    d['id'] = input['id']
                    ans.update(d)
                    print(ans)
                    json.dump(ans, output)
                    output.write('\n')
    output.close()
    # for name in test_list:
    #     ans = getTwitterActor(name)
    #     print(ans.append(user_id))
    print("--- %s seconds ---" % (time.time() - start_time))

    # 140/min
    # 21 name = ''
    # 117  #suspended  3times
    # 2242
