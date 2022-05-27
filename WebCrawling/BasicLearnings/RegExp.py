# Python RegExp網站 http://pythex.org/
import re
m = re.search(r'[0-9]+' , 'temp123BB')
print(m)

# match方法 : match(string)
# 從字串開頭開始傳回所有符合模式的字串，直到不符合字元，並把結果儲存為match物件，沒東西則傳回None
m = re.match(r'[a-z]+' , 'temp123BB')

# match 物件內包含許多方法讓我們呼叫值
# group() : 由字首到不符合字元為止，所有符合模式的字串list
# start() : 起始字元位置
# end() : 結束字元位置
# span() : 回傳 (開始位置,結束位置) 的tuple

if m != None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())

# search方法 : search(string)
# 傳回字串中第一個符合模式的字串，沒東西則傳回None，注意仍為match物件
m = re.search(r'[a-z]+' , '3tem12pBB')
print(m)
if m != None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
# findall方法 : findall()
# 傳回字串中所有符合模式的字串，回傳型別為list
m = re.findall(r'[a-z]+' , '3tem12pBB')
print(m)

# compile() 將常用的 regExp 製作成物件，提供前面所述的方法使用
reobj = re.compile(r'[a-zA-Z]+')
m = reobj.findall('3tem12PQ')
print(m)

# 範例練習檔案
html = """
<div class='content'>
    E-Mail1:<a href='mailto:mail1@test.com.tw'>mail1</a><br>
    E-Mail2:<a href='mailto:mail2@test.com.tw'>mail2</a><br>
    <ul class='price'>定價:360元</ul>
    <img src="http://test.com.tw/p1.jpg">
    <img src="http://test.com.tw/p2.jpg">
    <img src="http://test.com.tw/p3.jpg">
</div>
"""

import re
from bs4 import BeautifulSoup
sp = BeautifulSoup(html , 'html.parser')

# 搜尋所有電子郵件格式字串
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+' , html)
for i in emails:
    print(i)

# 搜尋價格
price = re.findall(r'\d+', sp.select('.price')[0].text)[0]
print(price)

# 搜尋 jpg
regex = re.compile('.*\.jpg')
imglist = sp.find_all("img" , {'src':regex})
for i in imglist:
    print(i)