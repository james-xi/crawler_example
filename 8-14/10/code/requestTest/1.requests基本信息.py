#coding:utf-8
import requests
r=requests.get("http://www.baidu.com")
print r.url #链接
print r.status_code #状态
print r.headers  #请求头
print r.text  #网页内容
print r.cookies #cookie
print r.content  #网页内容
print r.history #历史
print r.encoding  #编码
print r.is_redirect #是否重定向
print r.links  #是否子链接
