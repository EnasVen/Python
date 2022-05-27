import requests
from bs4 import BeautifulSoup
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
sp = BeautifulSoup(html.text , 'html.parser')

# BeautifulSoup 型別物件(sp變數)底下的方法 :
# 找tag名稱 : sp.title
# 找網頁解析後的純文字內容 : sp.text()
# 回傳符合第一個條件的tag : sp.find('span')
# 回傳所有符合條件的tag : sp.find_all('h2')
# 回傳指定CSS selector (id/class) : sp.select("#id) / sp.select('.name')

# find / find_all
data1 = sp.find('a')
sp.find_all('a')
sp.find_all('a',{"id":"link2"})
sp.find_all('img',{"border":"0"})[0].text


type(sp.find_all('img',{"border":"0"}))
type(sp.find_all('img',{"border":"0"})[0])
type(sp.find_all('img',{"border":"0"})[0].text)

# select
data1 = sp.select('title') #讀取 <title> tag
sp.select("#fisrtdiv")
sp.select(".title")
sp.find('a').text
sp.select("html head title") #找html底下的head下的<title> tag內容

# 範例練習檔案
html2 = """
<html><head><title>網頁標題</title></head>
<p class="header"><h2>文件標題</h2></p>
<div class="content">
    <div class="item1">
        <a href="http:example.com/one" class="red" id="link1">First</a>
        <a href="http:example.com/two" class="red" id="link2">Second</a>
    </div>
    <a href="http://example.com/three" class="blue" id="link3">
        <img src="http://example.com/three.jpg">ThirdPic
    </a>
</div>
"""

sp2 = BeautifulSoup(html2 , 'html.parser')

print(sp2.title) # 直接取得title標籤內容
print(sp2.find('h2'))
print(sp2.find_all('a'))
print(sp2.find_all('a' , {"class":"blue"}))
print(sp2.find_all('a' , {"class":"red"}))

sp2.find('a' , {"class":"red"}).text  # .text好像只能做一個項目，但其實不是
d1 = sp2.find("a" , {"href":"http:example.com/one"})
d1.text

sp2.find_all('a' , {"class":"red"}).text() # 會出現error 因為回傳是 array

# 要用 for 迴圈抓取內容值，再用get_text方法
for t in sp2.find_all('a' , {"class":"red"}):
    #print(t.get_text())
    print(t.text)

d2 = sp2.select("#link1")
print(d2[0].text)

# 尋找多個 tag 內容
print(sp2.find_all(['title','h2']))
isinstance( sp2.find_all(['title','h2']) , list) # 回傳物件是 list 型別

# 2種方法執行多層過濾底下的屬性值
print( sp2.select('div img')[0]['src'])  # 以字典方式
print( sp2.select('div img')[0].get('src'))  # 以get方法抓



