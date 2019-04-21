#coding:utf-8
import  urllib2
import  jsonpath
import json
import chardet

url="https://www.lagou.com/lbs/getAllCitySearchLabels.json"
jsonstr=  urllib2.urlopen(url).read()  #抓取网页的json数据
jsontree=json.loads(jsonstr)#转化为json对象
#mylist= jsonpath.jsonpath(jsontree,"$..name") #$根节点..所有包含name的节点
#mylist= jsonpath.jsonpath(jsontree,"$..id")#$根节点..所有包含id的节点
#mylist= jsonpath.jsonpath(jsontree,"$..code")#$根节点..所有包含id的节点
mylist= jsonpath.jsonpath(jsontree,"$.content") #第一个节点
for line in mylist:
    print line
mylist= jsonpath.jsonpath(jsontree,"$.content.data")#第二个节点
for line in mylist:
    print line
mylist= jsonpath.jsonpath(jsontree,"$.content.data.allCitySearchLabels") #第三个节点
mylist= jsonpath.jsonpath(jsontree,"$..allCitySearchLabels") #第三个节点
mylist= jsonpath.jsonpath(jsontree,"$.content.data[]") #第二个节点的孩子节点
print mylist
mylist= jsonpath.jsonpath(jsontree,"$*name") #判断所有节点是否包含name
print mylist
mylist= jsonpath.jsonpath(jsontree,"$.content..allCitySearchLabels.*") #allCitySearchLabel后续所有节点

print mylist

mylist= jsonpath.jsonpath(jsontree,"$.content.data.allCitySearchLabels")
for line in mylist:
    print line
    for key  in line:
        print key,line[key]

mylist= jsonpath.jsonpath(jsontree,"$.content.data.allCitySearchLabels")
for line in mylist:
    print line
    for key  in line:
        print key,line[key]
        for  data  in line[key]:
            print data