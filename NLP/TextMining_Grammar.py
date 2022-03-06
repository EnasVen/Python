# 語法包含以下技巧 :
# 1. word segmentation : 將詞語分割成單字 常用方法:Jieba
# 2. stemming : 衍生字轉成原始型態 (如:played / playing / plays => play) 常用方法: porter/snowball/lancaster
# 3. Lemmatization : 將變形字轉成同意的原始型態 (如:is/are/been => be)
# 4. Part-of-speech tagging : 根據語言學辨別每一個字的詞性 (動詞/名詞/主詞...)
# 5. Parsing : 根據語法樹辨別一個字句的文法，並做出正確判斷句子是哪種意思
# 6. Sentence breaking : 將文章的完整句子拆分出來 (又稱作 sentence tokenize)

# Chardet 套件 : 偵測文本編碼
import nltk

text = '哈'.encode('utf8')
print(text)

# 把未知編碼文件轉成UTF-8
import chardet

# 轉成binary二進位 rb = read binary的意思
with open('C:/Users/proph/PycharmProjects/NLP/sources/dict.txt' , 'rb') as f:
    text = f.read()
    en = chardet.detect(text)
    print(chardet.detect(text))

# 以utf-8形式寫出
with open('C:/Users/proph/PycharmProjects/NLP/sources/dict_utf8.txt' , 'w') as f:
    text_utf8 = text.decode(en['encoding'] , errors='ignore')
    f.write(text_utf8)

# OpenCC 套件 : 繁簡中文互相轉換的套件
# pip install opencc-python-reimplemented
from opencc import OpenCC

# s2t 表示 simple chinese => trad chinese
# 當然也可以繁轉簡 或者轉香港版中文 t2hk
# 相關指令查詢 : https://github.com/yichen0831/opencc-python
cc = OpenCC('t2s')
to_convert = '開放中文轉換'
converted = cc.convert(to_convert)
print(converted)

# 大小寫轉換
text = 'In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans'
print(text)
print('===================')
print('after lowercase')
#print(text.lower())
print(text.upper())

# 判斷是否全為大小寫  is.xxx
print('AABBC'.isupper())
print('aabbc'.islower())
print('AaBbC'.isupper())

# 1. word segmentation : 將詞語分割成單字 常用方法:Jieba
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
text = 'Backgammon is one of the oldest known board games. Its history can be traced back nearly 5,000 years to archeological discoveries in the Middle East. It is a two player game where each player has fifteen checkers which move between twenty-four points according to the roll of two dice.'
words = word_tokenize(text)
print(words)
type(words) # list

# 2. stemming : 衍生字轉成原始型態 (如:played / playing / plays => play) 常用方法: porter/snowball/lancaster
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
#nltk.download('all')
pst = PorterStemmer()
snowball = SnowballStemmer('english')

print(pst.stem('eating'))
print(pst.stem('passed'))

print(snowball.stem('eating'))
print(snowball.stem('passed'))

# 3. Lemmatization : 將變形字轉成同意的原始型態 (如:is/are/been => be)
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

wnl = WordNetLemmatizer()

# 後面要指定詞性
print(wnl.lemmatize('indexes','n'))  # noun名詞
print(wnl.lemmatize('struggling','v')) # verb動詞
print(wnl.lemmatize('saddest', 'a')) # adj形容詞

# 4. Part-of-speech tagging : 根據語言學辨別每一個字的詞性 (動詞/名詞/主詞...)
sentence = 'The brown fox is quick and he is jumping over the lazy dog'
tokens = nltk.word_tokenize(sentence)

# 將句子分詞後判斷每一個字元的詞性
tagged_sent = nltk.pos_tag(tokens)
print(tagged_sent)

# 不分詞直接判斷

# (錯誤作法!)
from nltk.book import  *
tagged_sent = nltk.pos_tag_sents(sentence)  # 必須是 list of string，不能只放單一string
print(tagged_sent)

# (正確做法!)
list_test = [text1 , text2]
tagged_sent = nltk.pos_tag_sents(list_test)
print(tagged_sent)


# 5. Parsing : 根據語法樹辨別一個字句的文法，並做出正確判斷句子是哪種意思

# 6. Sentence breaking :
from nltk.tokenize import sent_tokenize
text = 'Backgammon is one of the oldest known board games. Its history can be traced back nearly 5,000 years to archeological discoveries in the Middle East. It is a two player game where each player has fifteen checkers which move between twenty-four points according to the roll of two dice.'
sentences = sent_tokenize(text)
for sentence in sentences:
    print(sentence+'\n')

# 整合範例 : word_tokenize + pos_tag + lemmatize
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

sentence = 'football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal.'
tokens = word_tokenize(sentence)
tagged_sent = pos_tag(tokens)

wnl = WordNetLemmatizer()
lemmas_sent = []
for tag in tagged_sent:
    wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
    lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))
print(lemmas_sent)  # 整句話的單詞就被還原了

# Stopwords (如:a , an  , the ... 等等)
from nltk.corpus import stopwords
nltk.download('stopwords')
# nltk supports 22 languages for removing the stop words
print(stopwords.words("english"))

# 去除重複的用set
stop_words = set(stopwords.words("english"))
sentence = "Backgammon is one of the oldest known board games."

# 將句子tokenize後去除stopwords
words = nltk.word_tokenize(sentence)
without_stop_words = [word for word in words if not word in stop_words]
print(without_stop_words)