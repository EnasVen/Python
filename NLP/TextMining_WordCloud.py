# 2022.03.27 安裝wordcloud的時候發現error
# 記得去更新 MicroSoft  VC++

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

ret = open("./sources/dataset/speech.txt", "r").read().strip() # 去掉換行
seglist = jieba.cut(ret, cut_all=False)
text = ''
for i in seglist:
    text = text + ' ' + i
print(text)

wordcloud = WordCloud(font_path='simhei.ttf', width=800, height=800,
                      background_color='white', min_font_size=10).generate(text) # 產生wordcloud

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()