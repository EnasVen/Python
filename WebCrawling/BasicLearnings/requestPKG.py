# 匯入模組
import requests # 如果沒有安裝就pip install requests

# GET 請求
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
html.encoding = 'utf-8'
if html.status_code == requests.codes.ok :
    print(html.text)
    print('Successfully get doc ! \n')

# URL 查詢參數
# payload = {'key1':'value1' , 'key2':'value2'}
# html = requests.get("YourURL" , params=payload)
# print(html.url)

# 自訂HTTP headers
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                        '64.0.3282.186 Safari/537.36'}
r = requests.get(url,headers=headers)

# POST 請求
# payload = {'key1':'value1' , 'key2':'value2'}
# html = requests.post("YourURL" , data=payload)
# print(html.text)

# 建立 Session
rs = requests.session()

# 爬取ptt八卦版
# F12查看網頁，會發現按鈕的<button>html tag 具備 class:btn-big / name:yes 屬性
payload = {
    'form':'https://www.ptt.cc/bbs/Gossiping/index.html',
    'yes':'yes'
}

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                        '64.0.3282.186 Safari/537.36'}

# 提交post請求，模擬瀏覽器進行
requests.post('https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html' , data=payload , headers=headers)

# 使用get請求抓取主頁面，並將結果儲存到res變數內
res = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html',headers=headers)
res

# 執行結果會發現res沒東西，因為兩次request使用的session不同
# 統一session便可解決這個問題

rs = requests.session()
rs.post('https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html' , data=payload , headers=headers)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html',headers=headers)

# 擷取網頁內容
from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text , 'html.parser')
items = soup.select('.r-ent')
for item in items:
    print(item.select('.date')[0].text,
          item.select('.author')[0].text,
          item.select('.title')[0].text)


