#coding:utf-8
import requests
import json
#url="http://httpbin.org/post"     #data     textfile
newurl="http://pythonscraping.com/pages/processing2.php" #任意文件。-文件名根据php接口
data={"hello":"world"}
textfile={"file":open("test.txt","r")}
zipfile={"uploadFile":open("1.rar","rb")}
#r1=requests.post(url,data=data)
#print r1.text
print "--------------------------------------"
r2=requests.post(newurl,files=zipfile)
print r2.text
