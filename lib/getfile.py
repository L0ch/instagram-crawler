# parameter1 : shortcode
# parameter2 : crawlling option(pic, video, pic+video)

import requests
import re
import asyncio
import aiohttp
import aiofiles
from tqdm import tqdm
from tqdm import trange


base_url = "https://www.instagram.com/p/"
user_feed = "/?__a=1" 	# to get public user feed

img_pattern = re.compile(r'"display_url":".+"')
video_pattern = re.compile(r'"video_url":".+"')	



# Asynchronous request
async def get_media_url(shortcode, img_urls, video_urls):
	url = base_url + shortcode + user_feed
	
	# Find source url
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as res:
			json = await res.text()
			json = json.replace(',',',\n')
			img_urls += img_pattern.findall(json)
			video_urls += video_pattern.findall(json)

			
			
async def download_media(url, target, limit):
	pattern = r'\d+_\d+_\d+.+\?'
	file_name = re.search(pattern, url).group().replace('?','')
	
	# Write to file
	async with aiohttp.ClientSession() as session, limit:
		async with session.get(url) as res:
			async with aiofiles.open(target+'/'+file_name, 'wb') as file:
				await file.write(await res.read())
				await file.close()
		
		
			
# Parameter : image/video url list
def download(urls, target):
	# Set limit read/write to file
	limit = asyncio.Semaphore(10)
	# Asynchronous call
	# Download image/video 
	tasks = [download_media(url, target, limit) for url in urls]
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait(tasks))

	
		
# Parameter : shortcode list
# Return : img/video url list
def source(shortcodes):
	img_urls = []
	video_urls = []
	
	# Asynchronous call
	# Get image/video url
	tasks = [get_media_url(shortcode, img_urls, video_urls) for shortcode in shortcodes]
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait(tasks))
	
	# Split
	for i in range(0,len(img_urls)):
		img_urls[i] = img_urls[i].split('"')[3]
	
	for i in range(0,len(video_urls)):
		video_urls[i] = video_urls[i].split('"')[3]
	
	# Deduplication
	img_urls = list(set(img_urls))
	
	
	return img_urls, video_urls
	
	


