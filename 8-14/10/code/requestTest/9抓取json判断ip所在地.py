#coding:utf-8
import requests
import requests.auth

req=requests.get("https://api.ip2country.info/ip?113.88.65.106",verify=False)
print req.text
print req.json().get("countryName") #抓取json,实例化，返回国家名字