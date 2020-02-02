# parameter1 : username


import requests
import re
import json
import sys
from tqdm import tqdm
from tqdm import trange


#def hashtag(tag_name):
	#base_url = "https://www.instagram.com/explore/tags/"
	#country_code = 
	#return 20


def profile(user_name):
	base_url = "https://www.instagram.com/"
	get_feed = "?__a=1"
	
	url = base_url+user_name+get_feed
	response = requests.get(url).text

	try:
		json_source = json.loads(response)
	except:
		print("Account does not exist")
		exit(1)
		
	json_user = json_source['graphql']['user']
	
	# User ID
	user_id = json_user['id']
	# Total post count
	post_cnt = json_user['edge_owner_to_timeline_media']['count']
	
	
	is_private = json_user['is_private']
	if is_private == True:
		print("Cannot access private account")
		exit(1)
		
	if post_cnt == 0:
		print("Post does not exist, nothing to download")
		exit(1)
		
	return user_id, post_cnt
	

################################################################
# parameter1 : userid
# parameter2 : post_cnt

# return : shortcode(list)

def shortcode(user_id, post_cnt, mode_flag):
	
	
	first = 50			#Post count by once request
	shortcodes = []

	query_hash_tag = '90cba7a4c91000cf16207e4f3bee2fa2'
	query_hash_user = 'e769aa130647d2354c40ea6a439bfc08' #fixed
	base_url = 'https://www.instagram.com/'

	# Get json from graphql API 
	# GET param : query_hash, variables{id, first, after}
	# mode_flag : user = 1, hashtag = 0
	if(mode_flag):
		url = base_url+'graphql/query/?query_hash='+query_hash_user+'&variables={"id":"'+user_id+'",'  
	else:
		url = base_url+'graphql/query/?query_hash='+query_hash_tag+'&variables={"tag_name":"'+user_id+'",'  
	
		
	# Total post_cnt / Post count by once request
	req_cnt = int(post_cnt/first) + bool(post_cnt%first)

	# Get json
	end_cursor = ''
	for i in tqdm(range(0,req_cnt)):
		req_url = url + '"first":'+str(first)+',"after":"'+end_cursor+'"}'
		

		response = requests.get(req_url).text
		json_source = json.loads(response)
		
		json_user = json_source['data']['user']
		json_edge_owner_to_timeline_media = json_user['edge_owner_to_timeline_media']
		
		json_edges = json_edge_owner_to_timeline_media['edges']
		json_page_info = json_edge_owner_to_timeline_media['page_info']
		

		for nodes in json_edges:
			shortcodes.append(nodes['node']['shortcode'])

		# Get end_cursor for next requests
		end_cursor = json_page_info['end_cursor']
	
	

	return shortcodes

		
		