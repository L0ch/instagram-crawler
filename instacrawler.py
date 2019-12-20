from lib import fetch
from lib import getfile
import sys
import os
import time



def main():
	start = time.time()
	try:
		user_name = sys.argv[1]
	except:
		print("Usage : python3",sys.argv[0],"[username]")
		return 0
	
	user_info = fetch.profile(user_name) 
	user_id = user_info[0]
	posts = user_info[1]
	
	shortcode = fetch.shortcode(str(user_id), posts)
	
	
	img_url, video_url = getfile.source(shortcode)
	
	print(len(img_url))
	print(len(video_url))
	
	
	getfile.download(img_url)
	getfile.download(video_url)
	
	
	print("time :", time.time() - start)

if __name__ == "__main__":
	main()
	
		