from lib import fetch
from lib import getfile
import sys
import os
import time
import argparse

	

def main():
	
	start = time.time()
	
	target_help = "Instagram user's name"	
	op_help = "Crawling media format(image or video, default = all)"
	
	parser = argparse.ArgumentParser(description="Instagram media crawler by dw0rdptr")
	parser.add_argument("--target", required=True, help=target_help)
	
	parser.add_argument("--op", required=False, default = "all", choices = ["all", "img", 
"video"], help=op_help)
	
	args = parser.parse_args()
	
	target = args.target
	op = args.op
	
	print(target)
	if op=="all":
		print("all")
	elif op=="img":
		print("img")
	elif op=="video":
		print("video")
	
	
	
	user_info = fetch.profile(user_name) 
	user_id = user_info[0]
	posts = user_info[1]
	
	
	print("user_id :", user_id)
	print("Total post :", posts,'\n')
	
	time.sleep(2)
	
	print("Get post urls...")
	shortcode = fetch.shortcode(str(user_id), posts)
	print(len(shortcode), "posts load Complete.\n")
	time.sleep(2)
	
	print("Get media source urls...")
	img_url, video_url = getfile.source(shortcode)
	print(len(img_url), "images,", len(video_url), "videos.\n")
	time.sleep(2)
	
	print("downloading images...")
	getfile.download(img_url)
	print("\ndownloading videos...")
	getfile.download(video_url)
	
	
	print("time :", time.time() - start)

if __name__ == "__main__":
	main()
	
		