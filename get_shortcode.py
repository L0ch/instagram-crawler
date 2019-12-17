#-*- coding:utf-8 -*-
# 인자1 : username


from bs4 import BeautifulSoup
import requests
import re
import sys


# posts, user_id - from profile_crawl.py
# first - Post count by once request
posts = 455
user_id = str(1692800026)
first = 12


query_hash = "e769aa130647d2354c40ea6a439bfc08" #fixed
base_url = "https://www.instagram.com/"	
url = base_url+"graphql/query/?query_hash="+query_hash+"&variables={\"id\":\""+user_id+"\","  # GET param : query_hash, variables{id, first, after}


# Total posts / Post count by once request
req_cnt = int(posts/first) + bool(posts%first)

# Get next posts
end_cursor = ""
for i in range(0,req_cnt):
	d = url + "\"first\":"+str(first)+",\"after\":\""+end_cursor+"\"}"
	r = requests.get(d)
	print(d)

	# Get end_cursor for next requests
	pattern = "end_cursor\":\"\w+=="
	result = re.search(pattern, r.text)
	end_cursor = result.group().split('":"')[1]
	
	



