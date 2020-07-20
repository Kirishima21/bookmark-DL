import requests

def unbookmark(id, authorization):
	
	headers = {'Authorization': str(authorization)}
	
	url = 'https://kirishima.cloud/api/v1/statuses/' + str(id) + '/unbookmark'
	
	requests.post(url, headers = headers)
	
	print('ブックマーク解除！')
