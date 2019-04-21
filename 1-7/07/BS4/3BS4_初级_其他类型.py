#coding:utf-8
from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;
and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- E
lsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie<
/a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tilli
e</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soupx=BeautifulSoup(html,"lxml") #"lxml解析方式"
soup1=BeautifulSoup(html,"html.parser") #常规网页解析，
soup=BeautifulSoup(html,"html5lib") #HTML5解析 ,只是解析方法不一样，结果一样


print soup.title.string #取出标签之间的内容
print type(soup.name) #编码
# <type 'unicode'>
print soup.name #文档
# [document]
print soup.attrs # ⽂档本身的属性为空
# {}
print soup.a
print soup.a.string #清理了注释  显示注释信息
print type(soup.a.string)