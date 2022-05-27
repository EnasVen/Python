# 下載米其林餐廳的各項資訊(名稱/位置/餐廳類別/經緯度/地址...etc)
from bs4 import BeautifulSoup
import requests

# 解析整個網頁
url = "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurants"
html = requests.get(url).text
soup = BeautifulSoup(html , "html.parser")
items = soup.select('.card__menu.js-restaurant__list_item.js-map')
#items = soup.select('.col-md-6.col-lg-6.col-xl-3')

# 找到各圖片的超連結
itemurl =  ['https://guide.michelin.com/' + s for s in [i.select('.link')[0].get('href') for i in items ] ]
#itemurl2 = [ i.select('.card__menu.js-restaurant__list_item.js-map:has(a)')[0].get('href') for i in items]

#################
siteurl =  itemurl[0]

# 定義解析函數
def showsite(siteurl):
    html=requests.get(siteurl).text
    soup=BeautifulSoup(html,'html.parser')
    # 取得餐廳名稱
    name = soup.select('.restaurant-details__heading--title')[0].text
    # 取得地址
    #location = soup.select('.restaurant-details__heading--list')[0].text.replace('\n',"")
    location = soup.find('ul').find('li').text.strip()
    # 取得分類
    kind = soup.select('.restaurant-details__heading-price')[1].text.replace('\n',"").replace(" ","")
    # 取得說明文字
    description = soup.select('.js-show-description-text p')[0].text
    # 取得電話
    if not len(soup.select('.link.js-dtm-link'))>0:
        phone = "No phone number."
    else:
        phone = soup.select('.link.js-dtm-link')[0]['href']
    # 取得網址
    if not len(soup.select('.link.js-dtm-link'))>=2:
        link = "No web link."
    else:
        link = soup.select('.link.js-dtm-link')[1]['href']
    # 取得圖片
    pic = soup.select('noscript')[3].select('img')[0].attrs['src']
    print("餐廳名稱:" , name)
    print("餐廳地點:", location)
    print("分類:", kind)
    print("說明文字:" , description)
    print("電話:", phone)
    print("網址:", link)
    print("圖片:", pic)


def getpageurl(page,url):
    global n,totpages
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    # 搜尋首頁有幾個店家區塊div
    #items = soup.select('.col-md-6.col-lg-6.col-xl-3')
    items = soup.select('.card__menu.js-restaurant__list_item.js-map')
    print('第'+str(page)+"頁，共有"+str(len(items))+"間")
    for item in items:
        n+=1
        print('n=',n)
        #siteurl = 'https://guide.michelin.com/' + items[max(n-20,n%20,n)-1].select('.card__menu.js-restaurant__list_item.js-map')[0].select('.link')[0].get('href')
        siteurl = 'https://guide.michelin.com/' + item.select('.link')[0].get('href')
        showsite(siteurl)
        # 第一次到首頁的時候要找到下標最大頁數
        if n==1:
            totpages=int(soup.select(".btn.btn-outline-secondary.btn-sm")[-2].text)

import requests
from bs4 import BeautifulSoup
n=0
homeurl = 'https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurants'
getpageurl(1,homeurl)

# 迴圈跑每一頁
for page in range(2,totpages+1):
    html = requests.get(homeurl).text
    soup = BeautifulSoup(html, 'html.parser')
    nextpage = homeurl + '/page/' + str(page)
    getpageurl(page,nextpage)


for item in items:
    print('https://guide.michelin.com/' + item.select('.link')[0].get('href'))