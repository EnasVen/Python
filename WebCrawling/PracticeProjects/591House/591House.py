import decimal
import re

import munch
import requests

import mylog



def search(rid, build_type, bid):
    url = f'https://newhouse.591.com.tw/home/housing/search?rid={rid}&sid=&build_type={build_type}&bid={bid}'
    response = requests.get(
        url=url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4400.0 Iron Safari/537.36'
        }
    )
    if response.status_code != 200:
        mylog.red(f'request: failure ({response.status_code})')
        return
    mylog.green(f'request: success')

    # with open('591.json', 'wb') as f:
    #     f.write(response.content)

    body = response.json()
    for item in body['data']['items']:
        #------------#
        # 取出建案名稱 #
        #------------#
        name = item['build_name']
        mylog.yellow(name)
        #------------#
        # 取出格局坪數 #
        #------------#
        room = item['room']
        # print(room)
        # 為了避免［N+N房］這樣的房型字串會導致我們切出 N 這個數字，使取出的坪數清單混入錯誤的數字
        # 因為坪數都放在 (...) 內，因此我們先取出所有 (...) 的字串，確保只有坪數資料而不會有房型資料
        sizes = re.findall(r'\(.+?\)', room)
        # print(sizes)
        # 然後再把坪數資料合併成字串，提供給後續切出所有整數和浮點數字串的處理流程
        room = ''.join(sizes)
        # print(room)
        #        \d*    \.?    \d+
        #       *=0+  ?=0/1   +=1+
        # 16       0      0      2
        # 16.25    2      1      2
        sizes = re.findall(r'\d*\.?\d+', room)
        # print(sizes)
        sizes = [
            decimal.Decimal(size)
            for size in sizes
        ]
        # 原來的 sizes 直接重新排序
        sizes.sort()
        # 原來的 sizes 不重新排序，另外複製一份重新排序後回傳
        # sizes1 = sorted(sizes)
        print(f'格局坪數：{sizes[0]} ~ {sizes[-1]}')
        #------------#
        # 取出每坪價格 #
        #------------#
        price = munch.munchify({
            'min': decimal.Decimal(0),
            'max': decimal.Decimal(0),
        })
        if item['price'] != '價格待定':
            # print(item['price'])
            parts = str(item['price']).split('~')
            if len(parts) == 2:
                price.min = decimal.Decimal(parts[0])
                price.max = decimal.Decimal(parts[1])
            if len(parts) == 1:
                price.min = decimal.Decimal(parts[0])
                price.max = decimal.Decimal(parts[0])
        print(f'每坪價格：{price.min} ~ {price.max}')
        #------------#
        # 計算每戶總價 #
        #------------#
        print(f'每戶總價：{sizes[0] * price.min} ~ {sizes[-1] * price.max}')



if __name__ == '__main__':
    rid = 3
    build_type = 1
    bid = 3216
    search(rid, build_type, bid)