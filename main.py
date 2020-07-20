import access
import downloader

# ここでダウンロードする数を設定します。
# 入力した数字×40個のbookmarkが調べられます
# 例えば3を入力した場合120件ダウンロードされます
times = 3

token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

authorization = "Bearer " + str(token)
first = access.access(0, authorization)
next_id = first['next_id']
data = first['data']
downloader.downloader(data, authorization)

errors = 0

time = 1

while int(time) < int(times):
	loops = access.access(next_id, authorization)
	data = loops['data']
	downloaded = downloader.downloader(data, authorization)
	errors = int(errors) + int(downloaded['error'])
	if len(str(loops['next_id'])) == 'stop':
		print("登録されているbookmarkがなくなりました作業を終了しています")
		break
	else:
		next_id = loops['next_id']
	time += 1
	
print('作業終了しました')
print(str(errors) + '枚の画像がエラーになりました。')
