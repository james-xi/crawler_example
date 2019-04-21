#coding:utf-8
import requests
import json
req=requests.get("https://www.12306.cn",verify=True) #默认用证书，，False,不会报错
req=requests.get("https://www.baidu.com/",verify=True)#true,不出错，需要可信安全证书
print req