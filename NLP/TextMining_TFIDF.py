# 文字探勘流程大致如下 :
# Corpus PreProcess => Feature Engineering => ML Modeling

# TF-IDF : tf-idf(word x for certain doc) = freq(word x in doc) * log( total documents / # of docs having word x)
# TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]

# ngram  為設定是否以單一文字分析 也可雙單字綁一起
# min_df 表示次數低於指定值就忽略不計
model = TfidfVectorizer(analyzer='word', ngram_range=(1, 1), min_df=0)
tfidf = model.fit_transform(corpus)

word = model.get_feature_names()
print(word)


tfidf_weight = tfidf.toarray()
print(tfidf_weight)


# 針對每一個文本 show 出每一個單字的tfidf
for i in range(len(tfidf_weight)):
    print("-------output {}-th document tf-idf weight------".format(i))
    for j in range(len(word)):
        print(word[j],tfidf_weight[i][j])