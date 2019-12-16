#-*- coding:utf-8 -*-
# 인자1 : username


from bs4 import BeautifulSoup
import requests
import re
import sys


base_url = "https://www.instagram.com/"
user_name = sys.argv[1]
#user_feed = "?__a=1" 	# to get public user feed

url = base_url+user_name
r = requests.get(url)

#Parse Posts
pattern = r"\d+.Posts"
result = re.search(pattern, r.text)
posts = int(re.findall('\d+',result.group())[0])
print("posts:",posts)


#Parse userid
pattern = r"owner.:\D+\d+"
result = re.search(pattern, r.text)
user_id = int(re.findall('\d+',result.group())[0])
print("userid:",user_id)

