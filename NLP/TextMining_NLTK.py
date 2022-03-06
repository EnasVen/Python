import nltk
# nltk.download()
from nltk.book import *

# 尋找 包含 lived 的語句 (大小寫一視同仁)
text3.concordance("lived")
text3.concordance("LIVEd")
# 尋找相似詞
text1.similar('monstrous')
# 尋找這兩個詞前後最常出現的單字
text1.common_contexts(['monstrous','abundant'])
# 尋找有多少不同單字
set(text4)
sorted(set(text4))
# 定義詞語重複程度 (i.e.文章多元性)
def lexical_diversity(text):
    return len(set(text)) / len(text)
lexical_diversity(text4)

# 繪製特定詞語分布圖
import matplotlib.pyplot as plt
text4.dispersion_plot(['citizens','democracy','freedom','duties','America','liberty','constitution'])
# 統計詞頻 top15
fdist_1 = FreqDist(text1)
fdist_1.most_common(15)
fdist_1.plot(15)