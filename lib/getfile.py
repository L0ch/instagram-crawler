# parameter1 : shortcode
# parameter2 : crawlling option(pic, video, pic+video)

import requests
import re
import asyncio
import aiohttp

base_url = "https://www.instagram.com/p/"
user_feed = "/?__a=1" 	# to get public user feed

img_pattern = re.compile(r'"display_url":".+"')
video_pattern = re.compile(r'"video_url":".+"')	

async def get_media_url(shortcode, img_urls, video_urls):
	url = base_url + shortcode + user_feed
	
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as res:
			json = await res.text()
			json = json.replace(',',',\n')
			img_urls += img_pattern.findall(json)
			video_urls += video_pattern.findall(json)
			

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
def source(shortcodes):
	img_urls = []
	video_urls = []
	
	# Asynchronous call
	# Get image/video urls
	tasks = [get_media_url(shortcode, img_urls, video_urls) for shortcode in shortcodes]
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait(tasks))
	
	# split
	for i in range(0,len(img_urls)):
		img_urls[i] = img_urls[i].split('"')[3]
	
	for i in range(0,len(video_urls)):
		video_urls[i] = video_urls[i].split('"')[3]
	
	img_urls = list(set(img_urls))
	
	
	return img_urls, video_urls
	
	


