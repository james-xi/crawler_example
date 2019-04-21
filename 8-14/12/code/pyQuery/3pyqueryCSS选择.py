#coding:utf-8
import pyquery
import lxml.etree
doc=pyquery.PyQuery(filename="index.html")
print type(doc)
print doc('head')  #head标签
print doc('head  title')  #head标签  title标签
print doc('head  title').text()  #标签中间的文本
print "---------------------------"

print type(doc("#container")) #list,1个，多个
print doc("#container")[0]

print doc("#container").attr["class"] #list第一个 ,取标签内部属性


#print doc("#container  .list")  按照类型取出class=list
#print doc("#container  .list li")