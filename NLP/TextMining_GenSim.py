import gensim
from gensim import corpora


# How to create a dictionary from a list of sentences?
documents = ["The Saudis are preparing a report that will acknowledge that",
             "Saudi journalist Jamal Khashoggi's death was the result of an",
             "interrogation that went wrong, one that was intended to lead",
             "to his abduction from Turkey, according to two sources."]

documents_2 = ["One source says the report will likely conclude that",
                "the operation was carried out without clearance and",
                "transparency and that those involved will be held",
                "responsible. One of the sources acknowledged that the",
                "report is still being prepared and cautioned that",
                "things could change."]

# Tokenize(split) the sentences into words
texts = [[text for text in doc.split()] for doc in documents]

# Create dictionary
dictionary = corpora.Dictionary(texts)

# Get information about the dictionary
print(dictionary)
#> Dictionary(33 unique tokens: ['Saudis', 'The', 'a', 'acknowledge', 'are']...)

dictionary.token2id

documents_2 = ["The intersection graph of paths in trees",
               "Graph minors IV Widths of trees and well quasi ordering",
               "Graph minors A survey"]

texts_2 = [[text for text in doc.split()] for doc in documents_2]

dictionary.add_documents(texts_2)


# If you check now, the dictionary should have been updated with the new words (tokens).
print(dictionary)
#> Dictionary(45 unique tokens: ['Human', 'abc', 'applications', 'computer', 'for']...)
print(dictionary.token2id)


# 訓練詞向量
import gzip
import gensim
import logging # 紀錄系統資訊，預定呈現格式
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

data_file="./sources/dataset/reviews_data.txt.gz"

# 使用 gzip.open gz檔案
with gzip.open (data_file, 'rb') as f:
    for i,line in enumerate (f):
        print(line)
        break


def read_input(input_file):
    """This method reads the input file which is in gzip format"""

    print("reading file {0}...this may take a while".format(input_file))

    with gzip.open(input_file, 'rb') as f:
        for i, line in enumerate(f):

            if (i % 10000 == 0):
                print("read {0} reviews".format(i))
            # do some pre-processing and return a list of words for each review text
            yield gensim.utils.simple_preprocess(line)


# read the tokenized reviews into a list
# each review item becomes a serries of words
# so this becomes a list of lists
documents = list(read_input(data_file))
print("Done reading data file")

documents[0]

'''
Word2Vec model parameters

size:
The size of the dense vector to represent each token or word. If you have very limited data, then size should be a much smaller value. If you have lots of data, its good to experiment with various sizes. A value of 100-150 has worked well for me.

window: 考慮前後幾個英文單字，影響演算法學習結果
The maximum distance between the target word and its neighboring word. If your neighbor's position is greater than the maximum window width to the left and the right, then, some neighbors are not considered as being related to the target word. In theory, a smaller window should give you terms that are more related. If you have lots of data, then the window size should not matter too much, as long as its a decent sized window.

min_count: 小於幾次就忽略，代表出現次數太少就當作不重要詞彙
Minimium frequency count of words. The model would ignore words that do not statisfy the min_count. Extremely infrequent words are usually unimportant, so its best to get rid of those. Unless your dataset is really tiny, this does not really affect the model.

workers: 指派核心
How many threads to use behind the scenes?

sg: sg=1 means skip-gram and sg=0 menascbow 指定演算法模式
'''
model = gensim.models.Word2Vec (documents, vector_size=150, window=10, min_count=2, workers=5, sg=0)
model.train(documents,total_examples=len(documents),epochs=10)

# 訓練後查看每一個單字最相似的詞語
w1 = "happy"
model.wv.most_similar (positive=w1)

# look up top 6 words similar to 'france'
w1 = ["france"]
model.wv.most_similar (positive=w1,topn=6)

# get everything related to stuff on the bed
w1 = ["bed",'sheet','pillow']
w2 = ['couch']
model.wv.most_similar (positive=w1,negative=w2,topn=10)

# similarity between two different words
model.wv.similarity(w1="dirty",w2="smelly")

# Which one is the odd one out in this list?
model.wv.doesnt_match(["cat","dog","france"])

# print word vector
model.wv['dirty']