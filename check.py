def check(data):
	
	if len(str(data['remote_url'])) != 4:
		result = data['remote_url']
		print('リモート！')
		return result
	else:
		result =  data['url']
		print('ローカル！')
		return result
