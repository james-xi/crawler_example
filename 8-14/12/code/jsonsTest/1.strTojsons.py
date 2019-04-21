#coding:utf-8
import json


#json字符串，json类型根字符串有关系，平时最多是字典
mydict='{"name":"yincheng","QQ":["77025077","12345"]}'
mydict='[1,2,3,4,5,6]'
print( json.loads(mydict))
print( type(json.loads(mydict)))