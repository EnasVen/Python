import twstock
stock = twstock.Stock('6277')

# 歷史股票提供以下方法查詢資訊 :
# 1.price : 回傳近31筆收盤價
# 2.high : 回傳近31筆盤中最高點
# 3.low : 回傳近31筆盤中最低點
# 4.date : 回傳近31筆日期資料
# 5.fetch(西元年,月) : 回傳參數指定時間的資料
# 6.fetch_from(西元年,月) : 回傳參數指定時間至今的資料

print(stock.price[-5:])

# 查詢即時股價
real = twstock.realtime.get('6277')
print(real['realtime']['latest_trade_price'])
print(real['realtime']['open'])

# success 為判斷回傳資訊是否正確，為True才會進行後續
real = twstock.realtime.get('2317')
if real['success']:
    print('及時股票資料:')
    print(real)
else:
    print('錯誤'+real['rtmessage'])

print('目前股價:'+real['realtime']['latest_trade_price'])

########################
import twstock
import time
import requests

counterLine = 0 # 儲存發送次數
counterError = 0 # 儲存錯誤次數

print('程式開始執行')
while True:
    realdata = twstock.realtime.get('2317')
    if realdata['success']:
        realprice = realdata['realtime']['latest_trade_price'] # 目前股價
        if float(realprice) >= 100:
            print('目前鴻海股價 : ' + realprice)
            counterLine = counterLine + 1
            # 發送LINE訊息網址
            url_ifttt = 'https://maker.ifttt.com/trigger/stockLINE/with/key/cVYAUoRMIU4q4VF-8c_PHH?value1='+realprice
            res1 = requests.get(url_ifttt) # 發送請求
            print('第'+str(counterLine)+'次發送LINE回傳訊息:'+res1.text)
        if counterLine>=2: # 設定最多發送次數就結束程序
            print('程序結束!')
            break
        for i in range(120):
            time.sleep(120) # 每2分鐘讀取一次股票資訊
    else:
        print('twstock 讀取錯誤，原因 :'+realdata['rtmessage'])
        counterError = counterError + 1
        if counterError >= 3:
            print('程式結束!')
            break
        for i in range(120):
            time.sleep(120) # 每2分鐘讀取一次股票資訊
