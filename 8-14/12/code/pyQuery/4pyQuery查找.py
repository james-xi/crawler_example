#coding:utf-8
import pyquery
import lxml.etree
doc=pyquery.PyQuery(filename="index.html")
print type(doc)
items=doc(".list")
print type(items)
print items
print "---------------------------------"
print items.parent() #父亲节点， items.parent函数名  items.parent函数调用
print "---------------------------------"
print items.parents()#祖先节点
print "---------------------------------"
li = doc('.list .item-0.active') #兄弟节点
print(li.siblings())
print "---------------------------------"
li=  items.children() #遍历所有孩子节点
for line in li:
    print line ,line.text




'''
list=items.find("li") #find查找所有子节点
for line in list:
    print line ,line.text
'''





