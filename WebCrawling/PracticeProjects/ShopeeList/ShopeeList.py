# 爬取蝦皮購物關鍵字索引列表
import time
import requests
import munch
import mylog
import decimal

def search(keyword):
    cookie = None

    # 讀取個人 Cookie 檔內容
    with open('shopee.cookie', 'r') as f:
        cookie = f.read()
    if cookie is None or cookie == '':
        mylog.red(f'read cookie: failure')
        # return
    mylog.green(f'read cookie: success')

    # 主動維護 Cookie 的 Session 物件
    session = requests.Session()

    # 更新 Session 物件裡的 Headers
    session.headers.update({
        'referer':'https://shopee.tw/',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    })

    idx = 0
    while True:
        # 找到url規律
        # main_url = f'https://shopee.tw/search?keyword={keyword}&page={idx}'
        sub_url = f'https://shopee.tw/api/v4/search/search_items?by=relevancy&keyword={keyword}&limit=60&newest={idx*60}&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2'

        # 送出搜尋請求
        response = session.get(
            url=sub_url
        )
        if response.status_code != 200:
            mylog.red(f'request: failure ({response.status_code}).')
            return
        mylog.green(f'request: success')

        # with open('shopeeSCH.json', 'wb') as f:
        #     f.write(response.content)

        body = munch.munchify(response.json())
        # tmp = [body['items'][i]['item_basic'].name for i in range(0, 60)]
        # print(tmp)
        try:
            maxItem = len(body["items"])
            if maxItem == 0 :
                mylog.red(f'No items left in this page! Close Loop!')
                break
            else:
                for i in range(0, maxItem):
                    tmpName = body["items"][i]["item_basic"].name
                    tmpImgURL = 'https://cf.shopee.tw/file/' + body["items"][i]["item_basic"].image
                    tmpPrice = round(body["items"][i]["item_basic"].price/100000)
                    tmpSold= body["items"][i]["item_basic"].historical_sold
                    tmpStock = body["items"][i]["item_basic"].stock
                    tmpDiscount = body["items"][i]["item_basic"].discount
                    tmpShopLoc = body["items"][i]["item_basic"].shop_location
                    mylog.cyan(f'這是第 {idx + 1} 頁內的第 {i + 1} 個項目商品。')
                    print(f'搜尋結果: {idx * 60 + i + 1}')
                    print(f'商品名稱: {tmpName}')
                    print(f'圖片連結: {tmpImgURL} ')
                    print(f'商品產地: {tmpShopLoc}')
                    print(f'商品售價: {tmpPrice} TWD')
                    print(f'歷史銷量: {tmpSold}')
                    print(f'目前庫存: {tmpStock}')
                    print(f'目前折扣: {tmpDiscount}')
                    mylog.cyan('===================')
                time.sleep(0.5)
                idx += 1

        except IndexError:
            mylog.red('OOPS! End of Pages~')
            break
        else:
            if idx >= 30:
                mylog.red('避免占用過多系統資源，至多搜尋30頁~')
                break
            else:
                pass
        finally:
            pass

if __name__ == '__main__':
    keyword = '貓又小粥'
    search(keyword)
