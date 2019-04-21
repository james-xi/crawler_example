#coding:utf-8
import gevent
import gevent.monkey
import urllib2
gevent.monkey.patch_all()#自动切换

def  download(url):
    print "start",url
    data=urllib2.urlopen(url).read()
    print "length",len(data),url

gevent.joinall([
    gevent.spawn(download,"http://www.baidu.com"),
gevent.spawn(download,"http://www.163.com"),
gevent.spawn(download,"http://www.qq.com"),
gevent.spawn(download,"http://www.sina.com"),
])