# WordNet 屬於 Lemmatize 的方法，把字詞還原成同意詞

from nltk.corpus import wordnet as wn

# 找出詞語屬於 wordnet 裡面哪一種 syn 分類
wn.synsets('motorcar')
wn.synsets('trunk')

# show出每個car.n.01這個 wordnet syn 類別類包含哪些同意單詞
wn.synset('car.n.01').lemma_names()

# 單字 trunk 有很多意思，我們把不同意義的trunk，其同意詞show出來
for synset in wn.synsets('trunk'):
    print(synset.lemma_names())

# 查詢 car.n.01 這個分類在WordNet裡面的定義
wn.synset('car.n.01').definition()

# 查詢 trunk.n.01 這個分類在WordNet裡面的定義
wn.synset('trunk.n.01').definition()

# 找出 car.n.01 分類的上位分類 hyper = 上
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hypernyms()
types_of_motorcar

# 找出 car.n.01 分類的下位分類
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
types_of_motorcar

# 找到下位詞組後後，再從 synset 找出單詞（以詞為中心）
sorted( lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas() )

# 完整路徑（上位詞組再往上走）
motorcar = wn.synset('car.n.01')
motorcar.hypernym_paths()

# 直指頂端上位詞組
motorcar = wn.synset('car.n.01')
motorcar.root_hypernyms()

# 以鯨魚為例
right = wn.synset("right_whale.n.01")
minke = wn.synset("minke_whale.n.01")
# 「露脊鯨」與「小鬚鯨」在上位詞組中最低位的詞組
right.lowest_common_hypernyms(minke)

# 露脊鯨 vs 虎鯨
orca = wn.synset("orca.n.01")
right.lowest_common_hypernyms(orca)

# 露脊鯨 vs 陸龜
tortoise = wn.synset("tortoise.n.01")

# 露脊鯨 vs 小說
novel = wn.synset("novel.n.01")
right.lowest_common_hypernyms(novel)

# 計算由當前 synset 而上的階層數 (離 root 幾層)
print(wn.synset('baleen_whale.n.01').min_depth())
print(wn.synset('whale.n.02').min_depth())
print(wn.synset('vertebrate.n.01').min_depth())
print(wn.synset('entity.n.01').min_depth())

# 上下位詞組結構的相似程度 (數字接近1代表path越像)
print(right.path_similarity(right))     #露脊鯨和自己本身
print(right.path_similarity(minke))     #露脊鯨和小鬚鯨
print(right.path_similarity(orca))      #露脊鯨和虎鯨
print(right.path_similarity(tortoise))  #露脊鯨和陸龜
print(right.path_similarity(novel))     #露脊鯨和小說