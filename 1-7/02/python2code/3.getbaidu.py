#coding:utf-8
import  urllib2
import  urllib

'''
word={"wd":"尹成"}
print urllib.urlencode(word)  #统一规范，编码解码
print urllib.unquote( urllib.urlencode(word))

'''

url="http://www.baidu.com/s"
word={"wd":"尹成"}
word=urllib.urlencode(word) #编码成字符串
newurl=url+"?"+word #拼接网址
request=urllib2.Request(newurl)#发起请求
print urllib2.urlopen(request).read() #打开页面读取信息
