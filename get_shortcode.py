#-*- coding:utf-8 -*-
# parameter1 : posts
# parameter2 : user_id

# return : shortcode(list)

import requests
import re
import sys


# posts, user_id - from profile_crawl.py
# first - Post count by once request
posts = 455
user_id = str(1692800026)
first = 50
shortcode = []

query_hash = 'e769aa130647d2354c40ea6a439bfc08' #fixed
base_url = 'https://www.instagram.com/'

# Get json from graphql API 
url = base_url+'graphql/query/?query_hash='+query_hash+'&variables={"id":"'+user_id+'",'  # GET param : query_hash, variables{id, first, after}


# Total posts / Post count by once request
req_cnt = int(posts/first) + bool(posts%first)




# Get json
end_cursor = ''
for i in range(0,req_cnt):
	req_url = url + '"first":'+str(first)+',"after":"'+end_cursor+'"}'
	r = requests.get(req_url)
	
	print(req_url)
	json = r.text.replace(',',',\n')
	
	# Get end_cursor for next requests
	p = re.compile(r'"end_cursor":".+==')
	end_cursor = p.search(json)
	
	if(end_cursor):
		end_cursor = end_cursor.group().split('":"')[1]
		
	# Get each post shortcode
	p = re.compile(r'"shortcode":".+"')
	shortcode += p.findall(json)
	
	
	print(len(shortcode),"/",posts)

# split
for j in range(0,posts):
	shortcode[j] = shortcode[j].split('"')[3]
	print(shortcode[j])
	
	



