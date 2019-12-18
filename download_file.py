# parameter1 : shortcode(list)

import requests
import re

def download(url):
	file_name = url.split('/')[7].split('?')[0]
	with open(file_name, "wb") as file:	# open in binary mode
		response = requests.get(url)					# get request
		file.write(response.content)


			# various pic   # video       # pic+video
shortcode = ['B6CcWBTAMAB']#,'B6FNKePAHP-','Bvg77ZHn5uG']
base_url = "https://www.instagram.com/p/"
user_feed = "/?__a=1" 	# to get public user feed
download_url = []

# Get donwload url
for short in shortcode:
	url = base_url+short+user_feed
	r = requests.get(url)
	json = r.text.replace(',',',\n')
	p = re.compile(r'"display_url":".+"')
	download_url += p.findall(json)

# download
for i in range(0,len(download_url)):
	download_url[i] = download_url[i].split('"')[3]
	download(download_url[i])
