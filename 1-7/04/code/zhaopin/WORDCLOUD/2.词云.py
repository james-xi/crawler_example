# coding:utf-8
import jieba  #分词
import  matplotlib.pyplot as plt #数据可视化
import wordcloud
from  wordcloud import WordCloud,ImageColorGenerator,STOPWORDS #词云
import numpy  as np  #科学计算
from PIL import Image  #处理图片

#打开文本
textfile=open("3.txt").read() #读取文本内容
wordlist=jieba.cut_for_search(textfile)
space_list=" ".join(wordlist)#链接词语
backgroud=np.array(Image.open("2.jpg")) #背景图片
mywordcloud=WordCloud(background_color="black", #背景颜色
                      mask=backgroud,#写字用的背景图，从背景图取颜色
                      max_words=50,  #最大词语数量
                      stopwords=STOPWORDS, #停止的默认词语
                      font_path="simkai.ttf", #字体
                      max_font_size=200, #最大字体尺寸
                      random_state=50,#随机角度
                      scale=2).generate(space_list) #生成词云

image_color=ImageColorGenerator(backgroud) #生成词云的颜色
plt.imshow(mywordcloud) #显示词云
plt.axis("off") #关闭保存
plt.show()
