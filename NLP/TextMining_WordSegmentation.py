import jieba
sentence = "足球運動需要大家一起來推廣，歡迎加入我們的行列！"
print("輸入： {}".format(sentence))
words1 = jieba.cut(sentence, cut_all=False)
words2 = jieba.cut(sentence, cut_all=True)
words3 = jieba.cut_for_search(sentence)

print("精確模式：", end=' ')
for word in words1:
    print(word+'/', end='')

print('')

print("全模式：", end=' ')
for word in words2:
    print(word+'/', end='')

print('')

print("搜索引擎模式：", end=' ')
for word in words3:
    print(word+'/', end='')

text = '考試即將結束'
words1 = jieba.cut(text, cut_all=False)
for word in words1:
    print(word+'/', end='')

print('')

# 加入字詞 jieba.add_word(word, freq=None, tag=None)
jieba.add_word('即將結束', freq=None, tag=None)

# 載入自定義詞庫 jieba.load_userdict(file_path)
jieba.load_userdict('dict.txt')

words1 = jieba.cut(text, cut_all=False)
for word in words1:
    print(word+'/', end='')