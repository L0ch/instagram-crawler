from lib import fetch
from lib import getfile
import sys


def main():

	try:
		user_name = sys.argv[1]
	except:
		print("Usage : python3",sys.argv[0],"[username]")
		return 0
	
	user_info = fetch.profile(user_name) 
	user_id = user_info[0]
	posts = user_info[1]
	
	shortcode = fetch.shortcode(str(user_id), posts)
	
	print(shortcode)
	

if __name__ == "__main__":
	main()
	
		