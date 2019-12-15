#-*- coding:utf-8 -*-
# 인자1 : username


from bs4 import BeautifulSoup
import requests
import sys



base_url = "https://www.instagram.com/"
user_name = sys.argv[1]
user_feed = "?__a=1" 	# to get public user feed

url = base_url+user_name + user_feed

r = requests.get(url)

print(r.text)
