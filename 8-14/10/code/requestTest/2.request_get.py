#coding:utf-8
import requests
data={"wd":"尹成"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
url="https://www.baidu.com/s?"
req=requests.get(url,params=data,headers=headers)
print req.text
