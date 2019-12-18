# parameter1 : username


import requests
import re
import sys


base_url = "https://www.instagram.com/"
contry_code = "/?hl=en"
try:
	user_name = sys.argv[1]
except:
	print("Usage : python3",sys.argv[0],"[username]")
	exit(1)
	
url = base_url+user_name+contry_code
r = requests.get(url)

#Parse Posts
pattern = r"\d+.Posts"
result = re.search(pattern, r.text)
try:
	posts = int(re.findall('\d+',result.group())[0])
except:
	print("Account does not exist")
	exit(1)

#Parse userid
pattern = r"owner.:\D+\d+"
result = re.search(pattern, r.text)
try:
	user_id = int(re.findall('\d+',result.group())[0])
except:
	print("You cannot crawl private account")
	exit(1)
	
print("posts:",posts)
print("userid:",user_id)
