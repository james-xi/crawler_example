#coding:utf-8
import pyquery
import lxml.etree
#初始化各种网页
doc1=pyquery.PyQuery("<html></html>")
doc2=pyquery.PyQuery(  lxml.etree.fromstring("<html></html>"))
doc3=pyquery.PyQuery("http://www.baidu.com")
doc4=pyquery.PyQuery(filename="index.html")
print type(doc1)
print doc1.html()
print doc1,doc2,doc3,doc4