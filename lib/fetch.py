# parameter1 : username


import requests
import re
import sys
from tqdm import tqdm
from tqdm import trange


def hashtag(tag_name):
	bas_url = "https://www.instagram.com/explore/tags/"
	


def profile(user_name):
	base_url = "https://www.instagram.com/"
	contry_code = "/?hl=en"
	
	url = base_url+user_name+contry_code
	r = requests.get(url)

	#Parse Total post count
	pattern = r'"edge_owner_to_timeline_media":{"count":\d+,'
	result = re.search(pattern, r.text)
	try:
		post_cnt = int(result.group().split('"count":')[1].replace(',',''))
		
	except:
		print("Account does not exist")
		exit(1)

	if post_cnt == 0:
		print("Post does not exist, nothing to download")
		exit(1)
	
	#Parse userid
	pattern = r"owner.:\D+\d+"
	result = re.search(pattern, r.text)
	try:
		user_id = int(re.findall('\d+',result.group())[0])
	except:
		print("Cannot access private account")
		exit(1)
	
	return user_id, post_cnt
	

################################################################
# parameter1 : userid
# parameter2 : post_cnt

# return : shortcode(list)

def shortcode(user_id, post_cnt):
	
	
	first = 50			#Post count by once request
	shortcodes = []

	query_hash = 'e769aa130647d2354c40ea6a439bfc08' #fixed
	base_url = 'https://www.instagram.com/'

	# Get json from graphql API 
	# GET param : query_hash, variables{id, first, after}
	url = base_url+'graphql/query/?query_hash='+query_hash+'&variables={"id":"'+user_id+'",'  


	# Total post_cnt / Post count by once request
	req_cnt = int(post_cnt/first) + bool(post_cnt%first)

	# Get json
	end_cursor = ''
	for i in tqdm(range(0,req_cnt)):
		req_url = url + '"first":'+str(first)+',"after":"'+end_cursor+'"}'
		r = requests.get(req_url)
	
		#print(req_url)
		json = r.text.replace(',',',\n')
	
		# Get end_cursor for next requests
		p = re.compile(r'"end_cursor":".+==')
		end_cursor = p.search(json)
	
		if end_cursor:
			end_cursor = end_cursor.group().split('":"')[1]
			
		# Get each post shortcode
		p = re.compile(r'"shortcode":".+"')
		shortcodes += p.findall(json)
	


	# split
	for j in range(0,len(shortcodes)):
		shortcodes[j] = shortcodes[j].split('"')[3]
	
	print(len(shortcodes))
	
	return shortcodes

		
		
		