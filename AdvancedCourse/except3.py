# exception
try:
    num = eval(input('Enter a number: '))
    print('value is', num)    
except NameError as e:
    print('只能輸入數字')
    print('Error: ',e) # 顯示原始錯誤訊息


num = eval(input('Enter a number: '))
print('value is', num)

print('程式正常結束')