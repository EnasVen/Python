import random

import matplotlib.pyplot as plt
listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]

# 基本繪圖
plt.plot(listx , listy)
plt.show()

# plot方法參數設定
# color : 設定線條顏色(預設藍色)
# linewidth : 設定線條寬度(預設1.0)
# linestyle : 線條樣式(預設-)
# label : 設定圖例名稱 (設定label後需要執行legend方法才能執行: plt.legend() )

# 繪製多個圖形in one plot
listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
plt.plot(listx1 , listy1)

listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
plt.plot(listx2 , listy2)

plt.show()

# 設定標題/xy軸標題
plt.title("Test Plot")
plt.xlabel("No.")
plt.ylabel("Grades")

# 設定xy軸範圍
plt.xlim(0,100)
plt.ylim(0,50)

# 整合圖形
import matplotlib.pyplot as plt
listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
plt.plot(listx1 , listy1 , label = 'Male')
listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
plt.plot(listx2 , listy2 , color='red' , linewidth=5 , linestyle='--' ,label='Female')
plt.legend()
plt.xlim(0,20)
plt.ylim(0,100)
plt.title("Test Plot 01")
plt.xlabel("No.")
plt.ylabel("Grades")
plt.show()

# BarPlot
# plt.bar( x座標list , y座標list , 其他參數)
plt.bar(listx1,listy1,label='Male')
plt.bar(listx2,listy2,label='FeMale',color='red')
plt.title('Test Plot 02')
plt.xlabel("Age")
plt.ylabel("Counts")

# Pie Chart
# plt.pie( data list[,選擇參數列])
# 可用參數如下 :
# labels : 每一個項目標題組成的list
# colors : 每一個項目顏色組成的list
# explode : 每一個凸出數值組成的串列 0表示未凸出 數值越大凸出越明顯
# labeldistance : 項目標題與圓心的距離是半徑的多少倍 (i.e. 每一子塊標題與圓心距離)
# autopct : 項目百分比的格式 ( %格式%% 例如: %2.1f%%)
# shadow : T/F值  True表示圖形有陰影
# startangle : 繪圖起始角度，逆時針跑
# pctdistance : 百分比文字與圓心的距離是半徑的多少倍

import matplotlib.pyplot as plt
labels = ['A','B','C','D']
sizes = [5,10,20,15]
colors = ['red','green','blue','yellow']
explode = [0,0.02,0.05,0]

plt.pie(sizes,explode=explode,labels=labels,colors=colors,
        labeldistance=1.1,pctdistance=0.6,autopct="%3.1f%%",
        shadow=True,startangle=90)
plt.axis('equal')
plt.legend()
plt.show()

# 顯示中文
import matplotlib
print(matplotlib.__file__)
from matplotlib.font_manager import FontProperties

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
labels = ['A','B','C','測試中文']
sizes = [5,10,20,15]
colors = ['red','green','blue','yellow']
explode = [0,0.02,0.05,0]

plt.pie(sizes,explode=explode,labels=labels,colors=colors,
        labeldistance=1.1,pctdistance=0.6,autopct="%3.1f%%",
        shadow=True,startangle=90)
plt.axis('equal')
plt.legend( loc='upper left')
plt.show()

import random
for i in range(random.randint(0,5)):
        print('current index is', i ,' Test123')