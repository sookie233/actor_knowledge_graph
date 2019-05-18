import tweepy
from tweepy import OAuthHandler
import time
import json
import datetime


def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")





def getTwitterActor(name):

    user_info = []
    user = api.get_user(name)
    if user:

        keys = ['name','username','following','followers','likes','create_time','tweets','listed']
        user_info.extend([user.name, user.screen_name, user.friends_count, user.followers_count,\
         user.favourites_count, user.created_at,user.statuses_count,user.listed_count])
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
    file_name = 'part-00000'
    api = tweepy.API(auth, wait_on_rate_limit=True)
    with open( 'twitter_users_profile_new.jl','w') as output:
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

                    json.dump(ans, output,default=datetime_handler)
                    output.write('\n')
    output.close()


   
    print("--- %s seconds ---" % (time.time() - start_time))

'''
    test_list = ['taylorswift13']
    for name in test_list:
        ans = getTwitterActor(name)
        print(ans)
        print(ans['create_time'])
   # test_list = ['RobertDowneyJr','Renner4Real','ChrisEvans','chrishemsworth']
    


'''
    
    # 140/min
    # 21 name = ''
    # 117  #suspended  3times
    # 2242
