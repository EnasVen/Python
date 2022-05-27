# open(檔案名稱 , [,模式] , [,編碼])

# 模式參數
# r/w/a :讀取/寫入/附加
# f = open('file1.txt' , 'w')
# ...
# f.close()

content = """Hello Python
    中文測試
    welcome!"""
f = open('file1.txt','w')
f.write(content)
f.close()

# 編碼參數
content = """Hello Python
    中文測試
    welcome!"""
f = open('file1.txt','w',encoding='UTF-8')
f.write(content)
f.close()

# 測試讀取並指定編碼
f = open('file1.txt' , 'r' , encoding='utf-8')
for line in f:
    print(line,end="")
f.close()

# 使用with自動關閉檔案
with open('file1.txt' , 'r' , encoding='utf-8') as f:
    for line in f:
        print(line, end="")

# 使用錯誤編碼讀取檔案會有error
with open('file1.txt' , 'r' , encoding='cp950') as f:
    for line in f:
        print(line, end="")


# 常用檔案處理方法 :
# close() : 關閉檔案，關閉後就不能進行讀寫
# flush() : ' 檔案在關閉時會自動寫入檔案內
# read([size]) : 測試指定長度的字元，未指定則讀取所有字元
# readable() : 測試是否可讀取
# readline([size]) : 讀取文字指標所在列中指定size長度的文字內容，未指定則default一整列
# readlines() : 讀取所有列，回傳list
# next() : 移動到下一行
# seek(0) : 將指標移動到文件最前端
# tell() : 傳回文件目前位置
# write(str) : 將檔案寫入路徑，無回傳值
# writable() : 測試是否寫入

# read()
with open('file1.txt' , 'r' , encoding='utf-8') as f:
    str1 = f.read(5)
    print(str1)

# readlines()
with open('file1.txt' , 'r' , encoding='utf-8') as f:
    content = f.readlines()
    print( (type(content) , content))

# BOM開頭  \ufeff 會出現在 f.read 模式下 (現在會內建去除，已經不會出現啦)
f = open('file2.txt' , 'r' , encoding='UTF-8') # 過往要用 UTF-8-sig 來避免
str2 = f.read(5) # 讀取前5個字元
print(str2)
f.close()

# readline([size]) : 省略size會內建讀取整列 (包括換行符號\n)
f = open('file2.txt' , 'r' , encoding='UTF-8')
str3 = f.readline()
str4 = f.readline(3)
print(str3)
print(str4)
# print('這是有指定參數的結果 :' , str4 ,  '\n這是沒有指定參數的結果 :' , str3)
f.close()

# readline() 讀取整列後會移到下一列，因此第二個print會產出dog文字
