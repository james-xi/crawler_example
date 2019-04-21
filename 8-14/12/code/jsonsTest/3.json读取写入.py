#coding:utf-8
import json
'''
#写入
listStr = [{"city": "北京"}, {"name": "⼤刘"}]
json.dump(listStr, open("listStr.json","w"), ensure_ascii=False)
dictStr = {"city": "北京", "name": "⼤刘"}
json.dump(dictStr, open("dictStr.json","w"), ensure_ascii=False)
'''

strList = json.load(open("listStr.json"))
print strList
# [{u'city': u'\u5317\u4eac'}, {u'name': u'\u5927\u5218'}]
strDict = json.load(open("dictStr.json"))
print strDict
for  data in strDict:
    print data,strDict[data]