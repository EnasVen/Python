# https://console.developers,google.com/
# 前置作業需要在Google Console 上建立API並取得金鑰 (需要OAuth認證設定)
# 建立金鑰後，會自動下載一份json檔案到local端，把它丟到 project路徑底下並重新命名 gs_key_0312.json
# 接著安裝 gspread & oauth2client 模組


# 從試算表網址取得該試算表的 ID
# https://docs.google.com/spreadsheets/d/1tjPKH2xFAdU6zL07aIxtnCiXu97hhpHRzsxUuT9mOqI/edit#gid=0
# 1tjPKH2xFAdU6zL07aIxtnCiXu97hhpHRzsxUuT9mOqI => 這個就是id

# 以ServiceAccountCredentials 模組的 from_json_keyfile_name方法建立憑證
# 之後就用這個憑證連線到雲端，並將資料寫入

import  gspread
from oauth2client.service_account import ServiceAccountCredentials
auth_json_path = 'gs_key_0312.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']

# 連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials)

# 開啟 Google Sheet 資料夾 (記得表單右上角點開共用，輸入共用者為gs服務帳戶ID)
# 例如: python-googlesheet@oceanic-hook-343900.iam.gserviceaccount.com
spreadsheet_key = '1tjPKH2xFAdU6zL07aIxtnCiXu97hhpHRzsxUuT9mOqI'
sheet = gss_client.open_by_key(spreadsheet_key)

# 新增母資料表
# sh = gss_client.create('New0312')

# 建立/刪除子資料表
# worksheet = sh.add_worksheet(title="A worksheet", rows=100, cols=20)
# sh.del_worksheet(worksheet)
sheet.add_worksheet(title='New0312' , rows=10 , cols=5)

# 分享資料表
# sh.share('otto@example.com', perm_type='user', role='writer')

# 選擇子資料表
# worksheet = sh.get_worksheet(0)  #索引
# worksheet = sh.worksheet("January") #用名稱
# worksheet = sh.sheet1 # 直接呼叫
# worksheet_list = sh.worksheets() #列出全部
worksheet = sheet.get_worksheet(0)

# 清除資料表內容
worksheet.clear()

# 新增資料
list_title = ['店家','商品','價格','地點','日期']
worksheet.append_row(list_title)
list_data = [['Service-A','goods_01','75 USD','California','2019.01.03 20:24:37'] , ['Service-B','goods_02','45 USD','SanDiego' , '2020.05.28 15:30:21']]
worksheet.append_rows(list_data)

# 更新子資料表內的值
# 指定儲存格
# worksheet.update('B1', 'Bingo!')
# 指定座標
# worksheet.update_cell(1, 2, 'Bingo!')
# 指定範圍
# worksheet.update('A1:B2', [[1, 2], [3, 4]])

# 變更字體粗細
worksheet.format('A3:B3', {'textFormat': {'bold': True}})

# 變更儲存格背景+粗體
worksheet.format("A2:B2", {
    "backgroundColor": {
      "red": 0.0,
      "green": 0.0,
      "blue": 0.0
    },
    "horizontalAlignment": "CENTER",
    "textFormat": {
      "foregroundColor": {
        "red": 1.0,
        "green": 1.0,
        "blue": 1.0
      },
      "fontSize": 12,
      "bold": True
    }
})

# 抓取資料表橫列/直行 的資料
values_list = worksheet.row_values(1)
values_list = worksheet.col_values(1)

# 尋找指定資料位置
cell = worksheet.find("SanDiego")
print("Found something at R%sC%s" % (cell.row, cell.col))

# 套用正規表達後搜尋
# amount_re = re.compile(r'(Big|Enormous) dough')
# cell = worksheet.find(amount_re)

# feat. pandas/numpy
import pandas as pd
dataframe = pd.DataFrame(worksheet.get_all_records())

import pandas as pd
worksheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())

import numpy as np
array = np.array(worksheet.get_all_values())

import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6]])
# Write the array to worksheet starting from the A2 cell
worksheet.update('A2', array.tolist())

# 參考資源
# https://docs.gspread.org/en/latest/user-guide.html#selecting-a-worksheet