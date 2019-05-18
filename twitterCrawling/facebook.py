import urllib2
import json
followers = json.loads(urllib2.urlopen("https://graph.facebook.com/JenniferLawrence/?fields=fan_count&access_token=1599431820077896%7CzcfOlsCUta___jzZsykrPzsUMdQ").read())['fan_count']
print "# of followers:",followers
url_str = "https://graph.facebook.com/JenniferLawrence/posts?fields=reactions.limit(1).summary(true)&access_token=1599431820077896|zcfOlsCUta___jzZsykrPzsUMdQ&limit=100"
print "Reaction counts"
while True:
	x = urllib2.urlopen(url_str).read()
	data = json.loads(x)
	counts = [d['reactions']['summary']['total_count'] for d in data['data']]
	print counts
	try:
		next = data['paging']['next']
		url_str = next
	except Exception as e:
		break