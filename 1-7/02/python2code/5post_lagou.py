# encoding:utf-8
import urllib2
data="first=true&p=1&kd=python"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
request=urllib2.Request("https://www.lagou.com/jobs/positionAjax.json",headers=headers)
request.add_data(data)#post操作
print urllib2.urlopen(request).read()