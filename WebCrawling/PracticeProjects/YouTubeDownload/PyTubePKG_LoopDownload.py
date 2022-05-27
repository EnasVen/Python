# 批次下載YT影片
# 取得網址的正規表達
import requests
import re
from bs4 import  BeautifulSoup

url = 'https://www.youtube.com/watch?v=w0dMz8RBG7g&list=PLX_eGK_AA0YiPOw37iYCmb7GdjsWPoe1s'
html = requests.get(url)
sp = BeautifulSoup(html.text , 'html.parser')

# 常規 BS4 功能失效
sp.find_all("a" , {"id":"wc-endpoint"})
sp.select('#wc-endpoint')

# 使用正規表達抓取 (仍然失敗)
# res1 = re.findall(r'/watch[-\w+&@#/%\?\=\~\_\|\!\:\,\.\;]+[-\w+&@#/%\?\=\~\_\|\!\:\,\.\;]]' , html.text)
# print(res1)

# Playlist 方法
from pytube import Playlist
pl = Playlist(url)

# download_all 方法已經 deprecate
i = 0
for video in pl.videos:
    i+= 1
    if i>5 :
        print('Overload!')
        break
    else :
        video.streams.filter(subtype='mp4',res='360p').first().download('./VideoLists')

# 顯示每一個影片標題

print(len(pl))
for link in pl:
    print(link)

for video in pl.videos:
    name = video.title
    print(name)

