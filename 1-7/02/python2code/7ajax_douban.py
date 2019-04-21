# encoding:utf-8
import urllib2
import urllib

url="https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action"
formdata={"limit":"20","start":"0"} #
data=urllib.urlencode(formdata) #编码
request=urllib2.Request(url,data)#post,发起请求，传递data
print urllib2.urlopen(request).read()