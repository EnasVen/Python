# 作業 : 爬取蘋果頭條新聞+內容

# 方法1 -- request + bs4 模組
# 匯入模組
import time
import requests # 如果沒有安裝就pip install requests
import re
from bs4 import BeautifulSoup

# GET 請求
url = 'https://tw.appledaily.com/realtime/new/'
# html = requests.get(url)
# html.encoding = 'utf-8'
# if html.status_code == requests.codes.ok :
#     print(html.text)
#     print('Successfully get doc ! \n')

# 自訂HTTP headers
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                        '64.0.3282.186 Safari/537.36'}
# 建立 Session
rs = requests.session()
res = rs.get(url,headers=headers)

# 解析網頁
sp = BeautifulSoup(res.text , 'html.parser')

# 擷取新聞標題
title_list = [ x.text.replace(u'\u3000',u' ') for x in sp.select("span.truncate--3")]
type(title_list)
hasattr(title_list , "__iter__")

# 擷取新聞超連結
tmpObj = sp.select("div.flex-feature>a.story-card")
hyp_list = ['https://tw.appledaily.com/' + x.get("href")[1:] for x in tmpObj]

# 擷取新聞發布時間
tmpObj = sp.select("div.timestamp")
reObj = re.compile(r'(?P<dte> \d{4}\/\d{2}\/\d{2}\s\d{2}:\d{2})')
time_list = [reObj.search(x.text).group('dte').strip() for x in tmpObj]

# m = re.search('(?P<dte> \d{4}\/\d{2}\/\d{2}\s\d{2}:\d{2})','出版時間: 2022/05/20 18:52').string
# m.group('dte').strip()

# 擷取新聞內容
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()

para_list = []
for a in hyp_list:
    tmp_storage = ""
    driver.get(a)
    tmpPara = driver.find_elements(By.CLASS_NAME, 'tw-max_width')
    for p in tmpPara:
        tmp_storage += p.text
    print(tmp_storage)
    para_list.append(tmp_storage)
    time.sleep(0.1)

driver.close()

