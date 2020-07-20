# そもそもPythonがないとうごかない
とうぜんだよなぁ？  
まぁアレwindowsの人は頑張って、LinuxとかMacな人はそのまま動くかも、知らんけど
###### アスタルテにしか対応してない
これ非常に重要
中身書き換えれば何処の鯖でもたぶん動く保証はしないけど

##### 初回はは設定がいる(がんば)
アスタルテのwebから設定>開発>新規アプリってクリックしてアプリの名前だけ適当に入力  
アクセス権は絞りたいならどうぞ  
たぶんreadはbookmark  
writeもbookmarkがあれば十分  
分からないならスルーでおｋ  
送信してください

そうすると上のほうにアクセストークンってのがあるからそれをコピペして  
main.py ってファイルを適当なエディタで開いて上のほうの  
```
token = "xxxxxxxxxxxxxxxxxxxxxxxxx"
```  
ってところのx消してコピペしてあげれば動く

#### オプション
pythonistaで動かす人は downloader.py の  
```
# import photos
# import os
```
ってところと
```
#					photos.create_image_asset(name)
#					os.remove(name)
```
の # 消してあげと幸せになれるらしい(インデント注意)


保存した画像はbookmark外したいなら同じく downloader.py の  
```
#					unbookmark.unbookmark(status_id, authorization)
```
の # を外してあげると自動で保存できた投稿のbookmarkは外してくれる  
そもそも画像が無かったり、画像が保存できないとbookmarkは外れないから大丈夫。  

あと main.py でダウンロードできる件数が変更できたりする  
デフォルトだと120件  
正直これ以上増やすと迷惑になるからほどほどに利用してくれ。  
