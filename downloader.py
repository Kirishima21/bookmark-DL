import re
import urllib.request
# import photos
# import os
import unbookmark
import check
import os

def downloader(data, authorization):
	
	n = 0
	datas = data
	headers = headers = {'User-Agent': 'Mozilla/5.0'}
	count = 0
	
	while n < len(data):
		
		info = datas[n]
		media_attachments = info["media_attachments"]
		status_id = info['id']
		
		if len(media_attachments) == 0:
			
			print("画像がない投稿でした")
			count += 1
			print("---------------------------")
			n += 1
			
		else:
			
			m = 0
			
			while m < len(media_attachments):
				
				media = media_attachments[m]
				media_url = check.check(media)
				
				print(media_url)
					
				name = re.search("[a-zA-Z0-9][a-zA-Z0-9]*.(png|PNG|jpg|JPG|jpeg|JPEG|gif|GIF|mp4|MP4)", media_url)
				
				if name == None:
					print("処理に失敗しました")
					m += 1
					count += 1
					print("---------------------------")	
				else:
					name = name.group()
					
					print(name)
					print(media_url)
					
					try: urllib.request.urlopen(urllib.request.Request(media_url, headers = headers))
					except urllib.error.URLError as e:
						print(e.reason)
						if len(e.reason) != 0:
							m += 1
							n += 1
							count += 1
							print('保存できませんでした')
							print("---------------------------")
							continue
					
					os.chdir("media")
					opener = urllib.request.build_opener()
					opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
					urllib.request.install_opener(opener)
					urllib.request.urlretrieve(media_url, name)	

# Pythonista3 で使うときは下の二つをコメント外すことでフォトライブラリに保存してくれる
# ただし上のimportの二つもコメントアウトを外すこと

#					photos.create_image_asset(name)
#					os.remove(name)


					print('保存できました')
					os.chdir("../")
					print("---------------------------")

# 一度保存した画像をbookmarkから解除したいときにはここのコメントアウトを外してください
# 何かしらのエラーで保存されなかった場合はbookmarkが解除されることはありません

#					unbookmark.unbookmark(status_id, authorization)


					print("---------------------------")
					m += 1
					
			
			n += 1
			
	return {"error": count}
