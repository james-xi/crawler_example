#coding:utf-8
'''
import requests
import chardet
r=requests.get("http://www.baidu.cn")
print chardet.detect(r.content)
r.encoding=chardet.detect(r.content)['encoding']  #监测网页的编码
print r.text
print r.history
print r.url

'''
import requests
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
r=requests.get("http://www.baidu.cn",headers=headers)
print r.headers
print r.headers["BDQID"]
