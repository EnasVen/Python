# bag-of-word 產出過程如下
# Tokenize => Vocabulary Building => Ecoding
import jieba
sentence = "足球運動需要大家一起來推廣，歡迎加入我們的行列！"
words = jieba.tokenize(sentence)
for tk in words:
    print("word {}\t\t start: {} \t\t end:{}".format(tk[0],tk[1],tk[2]))

import jieba
import jieba.analyse # 讀取文章  讓jieba判斷重要詞彙


content = open('./sources/dataset/news.txt', 'r').read()

print("Input：{}".format(content))

tags = jieba.analyse.extract_tags(content, 10)

print("Output：")
print(",".join(tags))

# bag-of-word 缺點 : 過於稀疏 & 無法分辨順序造成的句子意思差異
# 例如 : am I good vs I am good
# 解決辦法 : lemmatize & stemming


# N-gram模型 : 文本中連續N個字
# 例如：this is a dog => [1,1,0,0,1]
# this is = (1)
# is a = (2)
# a sentence = (3)
# a book = (4)
# a dog = (5)

from sklearn.feature_extraction.text import CountVectorizer

bards_words =["The fool doth think he is wise,",
              "but the wise man knows himself to be a fool"]


vect = CountVectorizer()
#vect = CountVectorizer(stop_words="english")
vect.fit(bards_words)


print("Vocabulary size: {}".format(len(vect.vocabulary_)))
print("Vocabulary content:\n {}".format(vect.vocabulary_))

# 把文本轉換成向量的方法 : transform
bag_of_words = vect.transform(bards_words)
print("Features name:\n{}".format(vect.get_feature_names())) # 把重要詞彙依字母順序顯示
print("Dense representation of bag_of_words:\n{}".format(bag_of_words.toarray())) # 將文本轉成向量


from sklearn.feature_extraction.text import CountVectorizer
bards_words =["The fool doth think he is wise",
              "but the wise man knows himself to be a fool"]

vect1 = CountVectorizer(ngram_range=(1, 1)).fit(bards_words) # 1,1 代表N-gram為1 ; 1,2 則表示 1-gram和2-gram都要
print("Vocabulary size: {}".format(len(vect1.vocabulary_)))
print("Vocabulary:\n{}".format(vect1.get_feature_names()))

vect2 = CountVectorizer(ngram_range=(2, 2)).fit(bards_words)
print("Vocabulary size: {}".format(len(vect2.vocabulary_)))
print("Vocabulary:\n{}".format(vect2.get_feature_names()))
print("Transformed data (dense):\n{}".format(vect2.transform(bards_words).toarray()))


# 詞性標註
import jieba.posseg as pseg
words = pseg.cut("今天天氣很好")
for w in words:
    print('{} {}'.format(w.word, w.flag))