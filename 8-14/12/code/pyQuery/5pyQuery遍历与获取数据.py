#coding:utf-8
import pyquery
doc=pyquery.PyQuery(filename="index.html")
print  doc(".item-0.active") #一个节点
print  doc(".item-0.active").find("a").attr.href
print  doc(".item-0.active").find("a").attr("href")
print  doc(".item-0.active").find("a").text()
print  doc(".item-0.active").html()
list=doc("li").items() #items（）返回所有的节点的文本，没有ｉｔｅｍ列表
for li  in list:
    print li
