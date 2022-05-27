from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=O1Sx7B5WnDo')
print('START Download !')
yt.streams.first().download()  #未制定路徑則會下載到python檔案所在位置資料夾內
print('Download ok !')

print(yt.title)

# 為了避免出現路徑錯誤導致重載，先判斷是否存在路徑
import os
yt = YouTube('https://www.youtube.com/watch?v=O1Sx7B5WnDo')
print('START Download !')

path_dir = 'C:\\Users\\proph\\PycharmProjects\\YouTubeDownload\\VideoDownloads'
if not os.path.isdir(path_dir):
    os.mkdir(path_dir)
yt.streams.first().download()  #未制定路徑則會下載到python檔案所在位置資料夾內
print('Download ok !')

print(yt.title)

# streams方法內有許多操作下載影片格式的方法
# all : 傳回所有影片格式
# first() / last() :傳回第一個/最後一個影片格式
# filter() : 傳回指定條件的影片格式
# count() : 傳回影片格式的數量

print(yt.streams.count()) # 即將dprecate，用len()就好
print(len(yt.streams))
yt.streams.filter(subtype='mp4')
print(yt.streams.all()) # 即將deprecate
print(yt.streams)

# filter 條件如下 :
# 1. progressive : 篩選同時具備影像+聲音的格式 (progressive= True)
# 2. adaptive : 篩選只具有影像或聲音其中一個的格式 (adaptive = True)
# 3. subtype : 篩選指定格式的格式 (subtype= 'mp4')
# 4. res : 解析度 (res = 720p)
yt.streams.filter(adaptive=True).count() #20個

# download() 方法需要在 first() / last() 後面

# 範例練習 (下載指定的YT影片並擷取相關訊息)
from pytube import YouTube
import os

yt = YouTube('https://www.youtube.com/watch?v=O1Sx7B5WnDo')
print('影片名稱 = ' + yt.title)
print('影片格式種類數 = ' + str(len(yt.streams)) + ' 種!')
print('mp4影片並且具備聲音和影像 : ')
print(yt.streams.filter(subtype='mp4',progressive=True).all())
print('開始下載 mp4/360p 的影片!')
path_dir = 'C:\\Users\\proph\\PycharmProjects\\YouTubeDownload\\VideoDownloads'
if not os.path.isdir(path_dir):
    os.mkdir(path_dir)
yt.streams.filter(subtype='mp4' , res='360p' , progressive=True).first().download()
print('Download ok ! 檔案儲存於' + path_dir + ' 資料夾!' )
