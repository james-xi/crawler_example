#coding:utf-8
import requests
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
mycookie=dict(BAIDUID="zhadu") #模拟登陆，
r=requests.get("http://www.baidu.com",headers=headers,cookies=mycookie)
print r.cookies
for  cookie  in  r.cookies.keys():  #百度的所有的cookie
    print cookie ,r.cookies.get(cookie)

