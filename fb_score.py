       # {"username": "Film.Yahrzeit", "talking_about": 0, "about": 
       # "Zwei j\u00fcdische Schwestern sind w\u00e4hrend des 2. Weltkrieges auf 
       # der Flucht und erfahren die Willk\u00fcr des menschlichen Handelns am eigenen
       #  Leib.", "name": "Yahrzeit", "page_likes": 142, "id": "tt5357848"} 
import json
w_page_likes = 0.7
w_talking_about = 0.3
fb_file = "facebook_movies.jl"
fb_output = "fb_movie_score.jl"
def facebook_score(fb_file,fb_output,w_talking_about,w_page_likes):
    with open(fb_output,'a') as f:
        with open(fb_file , 'r') as f1:  	
            for line in f1:
                row = json.loads(line)
                fb_score =  w_talking_about*row['talking_about']+ \
                + w_page_likes*row['page_likes']
                print (fb_score)
                print("\n")
                d = {}
                d['id'] = row['id']
                d['score'] = fb_score/1000
                print(d)
                json.dump(d,f)
                f.write('\n')
facebook_score(fb_file,fb_output,w_talking_about,w_page_likes)