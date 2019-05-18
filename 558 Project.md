# 558 Project

Notes

Crawl actors/actresses, movies and TV series information and reviews from IMDB, Netflix, Rotten tomato and Facebook by Scrapy, and NLP technologies; Wrap crawled data to extract structured data using BeautifulSoup/Kafka; Bind structured results with post trends from Twitter, Facebook by twitter API and Facebook API; Apply machine learning algorithms to rank potential popular movies stars in the future and build a knowledge graph for advising producers with queries and visualization analysis.



###Problem:

* help cast directors finding the right potential actors
* The resources are limited
* actors ranks like starMeters only shows popular ones
too much works for cast director to narrow down from thousands of demos, videos, profiles

example: backstage.com:  list of actors based on onlyphysical characteristics
			the life of Pi, Avy Kaufman，Suraj Sharma
			
###Our Solution:
Build a knowledge graph for actor recommendation for casting directors, give oppotunities for potiential movie stars.

Input -->  movie genre, character description
Output --> list of actors with ranks, and their profiles


###Our Unique stuff:


* expand sources: Amazon movie, netflix, stage actors, hbo original----> introduce unpopular ones

* combined with social media ---> people's posts

* profiling actors based on previous movies/works ---> meet the casting director's needs

* box office(gross, budgets) of actor's previous movie

###Sources:
for actors: 
Amazon movie, netflix, stage actors, hbo original (youtube)
wikipedia

for their movies:
(reviews, box office,awards, movie infor, actor character profile)
imdb, rottentomatos

for social media:
Facebook, Twitter

Structured reference source:
MovieLens

###Challeges: 
how to refer unpopular actors along with popular stars
how to build parameters for the ranks
nlp, review extraction
machine learning, how to build the model (training data:imdb all actor list, testing data: unpopular list)


			

