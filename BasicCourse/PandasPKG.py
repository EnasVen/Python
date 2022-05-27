# data.frame 為 Pandas主要資料型態
# pandas 輸出方法 :
# to_csv() : 將資料儲存為表格資料 (.csv)
# to_excel() : 將資料儲存為Excel (.xlsx)
# to_sql() : 將資料儲存為SQLite資料 (.sqlite)
# to_json() : 將資料儲存為json資料 (.json)
# to_html() : 將資料儲存為網頁格式資料 (.html)

# 利用pandas建立d.f.並設定編碼UTF-8 (去除BOM)
import pandas as pd
datas = [ [65,92,78,83,70] , [90,72,76,93,56] , [81,85,91,89,77] , [79,53,47,94,80]  ]
indexs = ["A","B","C","D"]
cols = ["2018","2019","2020","2021","2022"]

df = pd.DataFrame(datas , columns=cols , index=indexs)
print(df)

import os
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))
# Change the current working directory
# os.chdir('/tmp')

# 使用pandas輸出資料
df.to_csv('out.csv',encoding='utf-8-sig')


# 使用pandas讀取資料
# pandas 讀取方法 :
# read_csv() : 匯入csv資料
# read_excel() : 匯入xlsx資料
# read_sql() : 匯入SQLite資料
# read_json() : 匯入json資料
# read_html() : 匯入html資料

# 利用pandas 讀取csv並儲存成 d.f. (index_col為去除索引欄位)
data = pd.read_csv("out.csv" , encoding="utf-8-sig" , index_col=0)
print(data)