#coding:utf-8
import urllib2
import urllib
import cookielib
import re

#主页，用户编号，登陆，三个页面
url_baidu_index="http://www.baidu.com"
reqReturn=urllib2.urlopen(url_baidu_index) #打开主页
print reqReturn.read()