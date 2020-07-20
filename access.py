import requests
import json
import re

def access(id, authorization):
	
	if id == 0:
		params = {'limit': '40'}
	else:
		params = {'limit': '40', 'max_id': str(id)}
	
	url = 'https://kirishima.cloud/api/v1/bookmarks'
	headers = {'Authorization': str(authorization)}
	
	r = requests.get(url, params = params, headers = headers).json()
	t = requests.get(url, params = params, headers = headers)
	
	next_id = t.links
	print(next_id)
	if 'next' in next_id :
		next_id = next_id['next']
		next_id = next_id['url']
		next_id = re.search('id=[0-9]*',next_id)
		next_id = next_id.group()
		next_id = re.search('[0-9][0-9]*', next_id)
		next_id = next_id.group()
		return {'next_id': next_id, "data": r}
	else:		
		return {'next_id': 'stop', 'data': r}
