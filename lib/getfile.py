# parameter1 : shortcode
# parameter2 : crawlling option(pic, video, pic+video)

import requests
import re

base_url = "https://www.instagram.com/p/"
user_feed = "/?__a=1" 	# to get public user feed

def download(urls):
	
	for url in urls:
		pattern = r'\d+_\d+_\d+.+\?'
		file_name = re.search(pattern, url).group().replace('?','')
		print(file_name)
		with open('result/'+file_name, "wb") as file:	# open in binary mode
			response = requests.get(url)					# get request
			file.write(response.content)
		
		
# parameter : shortcode list
# return : img url list
def source(shortcode):
	cnt = 0
	img_url = []
	video_url = []
	
	
	img_pattern = re.compile(r'"display_url":".+"')
	video_pattern = re.compile(r'"video_url":".+"')
	
	for short in shortcode:
		url = base_url + short + user_feed
		r = requests.get(url)
		json = r.text.replace(',',',\n')
		img_url += img_pattern.findall(json)
		
		video_url += video_pattern.findall(json)
		print(cnt)
		cnt+=1
	
	# split
	for i in range(0,len(img_url)):
		img_url[i] = img_url[i].split('"')[3]
	
	for i in range(0,len(video_url)):
		video_url[i] = video_url[i].split('"')[3]
	
	img_url = list(set(img_url))
	
	
	return img_url, video_url
	
	


