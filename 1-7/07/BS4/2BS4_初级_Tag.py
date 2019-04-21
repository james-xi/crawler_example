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

print soup.title #提取标签
print soup.head  #提取标签全部内容
#print soup.body
print soup.a  #多个标签提取第一个
print soup.p

print soup.name
print soup.title.name  #name就是标签的名字
print soup.head.name

print soup.title.attrs
print soup.p.attrs  #标签内部的属性
print soup.p["class"] #取出标签的内部属性
print soup.p["name"]

print soup.title.string #取出标签之间的内容