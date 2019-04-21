#coding:utf-8
import pyquery
print pyquery.PyQuery("http://www.baidu.com",headers={"user-agent":"pyquery"})
print pyquery.PyQuery("http://httpbin.org/post",{"user":"name"},method="post",verify=False)

