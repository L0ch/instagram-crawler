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
try:
	posts = int(re.findall('\d+',result.group())[0])
except:
	print("Account does not exist")
	exit(1)

#Parse userid
pattern = r"owner.:\D+\d+"
result = re.search(pattern, r.text)
try:
	user_id = int(re.findall('\d+',result.group())[0])
except:
	print("Private account")
	exit(1)
	
print("posts:",posts)
print("userid:",user_id)
