# Pandas模組使用 data.frame的plot方法繪圖
# DataFrame變數.plot(key1=value1 , key2=value2 ...)
# kind : 指定繪圖模式(如折線圖/長條圖...) (line/hist/scatter/bar/barh/pie)
# title : 圖形標題
# legend : 是否顯示圖示說明
# grid : 是否顯示格線
# xlim :x軸刻度範圍
# ylim : y軸刻度範圍
# xsticks : x軸刻度值
# ysticks : y軸刻度值
# x : 指定x軸資料的變數
# y : 指定y軸資料的變數
# fontsize : xy軸字體大小
# figsize : 設定繪製圖形長寬

import pandas as pd
import matplotlib.pyplot as plt
datas = [[65,92,78,83,70] , [90,72,76,93,56] , [81,85,91,89,77] , [79,53,47,94,80]]
indexes = ['A','B','C','D']
columns = ['m','n','p','q','r']
df = pd.DataFrame(datas , columns=columns , index=indexes)
df.plot(kind='bar',title='測試',fontsize=12,)
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.legend(loc='upper right')
plt.xticks(rotation=0)