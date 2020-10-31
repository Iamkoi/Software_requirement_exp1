import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
txt = (open("closed.txt", "r", encoding='utf-8')).read()
file1 = open("closed.txt")
file2 = open("closed.txt")
ls1 = []
while 1:
    line = file1.readline()
    new_word = line.strip()
    if not line:
        break
    ls1.append(new_word)
ls2 = []
while 1:
    line = file2.readline()
    new_word = line.strip()
    if not line:
        break
    ls2.append(new_word)
ls = ls1+ls2
words = jieba.lcut(txt)
counts = {}
for word in words:
    for i in ls:
        if word == i:
            continue
    if (len(word)) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
string = ' '.join(words)
print(len(string))
img = Image.open('222.png') #打开图片
img_array = np.array(img) #将图片装换为数组
stopword=['in', 'to', 'the', 'not', 'on', 'is', 'when', 'for', 'with', 'and', 'of', 'vscode', 'eroor']
stopword=stopword+ls
wc = WordCloud(
    background_color='white',
    width=800,
    height=556,
    mask=img_array,
    stopwords=stopword
    #font_path='./fonts/simhei.ttf',
)
wc.generate_from_text(string)#绘制图片
plt.imshow(wc)
plt.axis('off')
plt.figure()
plt.show()  #显示图片
wc.to_file('final.png')  #保存图片'''
