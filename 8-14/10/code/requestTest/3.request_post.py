#coding:utf-8
import requests
data={"emp_no":"1admin","password":"admin"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
url="http://demo.smeoa.com/index.php?m=&c=public&a=check_login"
req=requests.post(url, data=data,headers=headers)
print req.text