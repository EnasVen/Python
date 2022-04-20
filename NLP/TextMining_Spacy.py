# pip install spacy
# python -m spacy download en

import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood. Everyone has the right to life, liberty and security of person.")

# 分出句子
for item in doc.sents:
    print(item.text)
# 把句子存成list物件
sentences_as_list = list(doc.sents)
len(sentences_as_list)

import random
random.choice(sentences_as_list)

# 還原每一個詞語的同型態
for word in doc:
    print(word.text, word.lemma_)

sentence = list(doc.sents)[1]
# show出句子內每一個單詞
for word in sentence:
    print(word.text)

# show出每一個單詞的性質(詞語/詞性/tag)
for item in doc:
    print(item.text, item.pos_, item.tag_)

# 篩選動詞的詞語
verbs = []
for item in doc:
    if item.pos_ == 'VERB':
        verbs.append(item.text)
print(verbs)

doc2 = nlp("John McCain and I visited the Apple Store in Manhattan.")
# 辨識實體(entity)
for item in doc2.ents:
    print(item)
# 查看辨識的entity為哪一種實體命名
for item in doc2.ents:
    print(item.text, item.label_)