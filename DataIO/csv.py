# csv 模組可以協助匯入csv檔案
import csv
# newline代表換行字元
with open('test.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    # 寫入欄位名稱
    writer.writerow(['Name','Height','Weight'])
    # 寫入資料
    writer.writerow(['A',170,65])
    writer.writerow(['B',180,80])

# 以Dictionary寫入csv
import csv
with open('test2.csv','w',newline='') as csvfile:
    # 定義欄位
    fieldnames = ['Name','Height','Weight']

    # 寫入csv
    writer = csv.DictWriter(csvfile , fieldnames=fieldnames)

    # 寫入欄位名稱
    writer.writeheader()
    # 寫入資料
    writer.writerow({'Name':'Peter' , 'Height':170 , 'Weight':73})
    writer.writerow({'Name':'Josh', 'Height': 168, 'Weight': 85})

# 利用reader方法實現csv檔案讀取
import csv
with open('./test2.csv' , 'r' , newline='') as csvfile:
    # 讀取檔案內容
    rows = csv.reader(csvfile)
    # 迴圈顯示每一列
    for i in rows:
        print(i)

# 將讀取的檔案轉為 dictionary 格式
import csv
with open('./test.csv' , 'r' , newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    for j in rows:
        print(j['Name'] , j['Height'] , j['Weight'])

#