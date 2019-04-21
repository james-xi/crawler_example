# encoding:utf-8
import  urllib2

'''
httpproxy=urllib2.ProxyHandler({"http":"10.36.132.41:808"})#代理无需账号
opener=urllib2.build_opener(httpproxy)#创建一个打开器
request=urllib2.Request("http://www.baidu.com") #访问百度
response=opener.open(request)#打开网页，内置代理服务器
print response.read()
'''

httpproxy=urllib2.ProxyHandler({"http":"yincheng:111111@10.36.132.41:808"})
nohttpproxy=urllib2.ProxyHandler({}) #空代理
opener=urllib2.build_opener(nohttpproxy)
request=urllib2.Request("http://www.baidu.com/") #代理访问，URL必须完整，
response=opener.open(request)
print response.read()