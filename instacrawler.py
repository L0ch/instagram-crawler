from lib import fetch
from lib import getfile
import sys
import os
import time
import argparse



def main():
	start = time.time()
	
	mode_help = "Searching user or hashtag\n  "
	target_help = "mode user : Instagram user's name \nmode tag  : Instagram hashtag\n  "
	number_help = "Number of posts to download\n "
	op_help = "Kind of media to download(default = all)"
	
	parser = argparse.ArgumentParser(description="Instagram media crawler by dw0rdptr", formatter_class=argparse.RawTextHelpFormatter)
	
	parser.add_argument("--mode", required=True, choices = ["user", "tag"], help=mode_help)
	parser.add_argument("--target", required=True, help = target_help)
	parser.add_argument("--number", required=False, help = number_help)
	parser.add_argument("--media", required=False, default = "all", choices = ["img", "video"], help=op_help)
	args = parser.parse_args()
	
	mode = args.mode
	
	if mode == "tag":
		tag_mode(args)
	elif mode == "user":
		user_mode(args)

	print("time :", time.time() - start)
	
	
# Mode user
def user_mode(args):
	target = args.target
	media = args.media
	number = args.number
	
	
	if number==None or int(number) > 2000:
		number = 2000 # Max count
		
	print(number)
	#exit(1)
	
	user_info = fetch.profile(target) 
	user_id = user_info[0]
	post_cnt = user_info[1]
	
	# Make result directory
	if not os.path.isdir(target):
		os.mkdir(target)
	
	
	print("user_id :", user_id)
	print("Total post :", post_cnt,'\n')
	
	time.sleep(2)
	
	print("Get post urls...")
	shortcodes = fetch.shortcode(str(user_id), post_cnt)
	print(len(shortcodes), "posts load Complete.\n")
	time.sleep(2)
	
	print("Get media source urls...")
	img_urls, video_urls = getfile.source(shortcodes)
	print(len(img_urls), "images,", len(video_urls), "videos.\n")
	time.sleep(2)

	
	if media == "img":
		print("downloading images...")
		getfile.download(img_urls, target)
	elif media == "video":
		print("downloading videos...")
		getfile.download(video_urls, target)
	else:
		print("downloading images...")
		getfile.download(img_urls, target)
		print("downloading videos...")
		getfile.download(video_urls, target)
		
		
# Mode hashtag
def tag_mode(args):
	print("tag")

	
	
if __name__ == "__main__":
	main()
	
		