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
	parser.add_argument("--op", required=False, default = "all", choices = ["all", "img", "video"], help=op_help)
	args = parser.parse_args()
	
	target = args.target
	op = args.op
	
	# Make result directory
	if not os.path.isdir(target):
		os.mkdir(target)
	
	
	user_info = fetch.profile(target) 
	user_id = user_info[0]
	post_cnt = user_info[1]
	
	
	print("user_id :", user_id)
	print("Total post :", post_cnt,'\n')
	
	time.sleep(2)
	
	print("Get post urls...")
	shortcodes = fetch.shortcode(str(user_id), post_cnt)
	print(len(shortcodes), "post_cnt load Complete.\n")
	time.sleep(2)
	
	print("Get media source urls...")
	img_urls, video_urls = getfile.source(shortcodes)
	print(len(img_urls), "images,", len(video_urls), "videos.\n")
	time.sleep(2)

	
	if op=="all":
		print("downloading images...")
		getfile.download(img_urls, target)
		print("downloading videos...")
		getfile.download(video_urls, target)
	elif op=="img":
		print("downloading images...")
		getfile.download(img_urls, target)
	elif op=="video":
		print("downloading videos...")
		getfile.download(video_urls, target)
	
	
	
	
	print("time :", time.time() - start)

if __name__ == "__main__":
	main()
	
		