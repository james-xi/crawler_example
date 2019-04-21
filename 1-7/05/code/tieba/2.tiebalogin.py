#coding:utf-8
import urllib2
import urllib
import cookielib
import re

#主页，用户编号，登陆，三个页面
url_baidu_index="http://www.baidu.com"
reqReturn=urllib2.urlopen(url_baidu_index) #打开主页

url_baidu_token="https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&class=login"
url_baidu_login="https://passport.baidu.com/v2/api/?login"
user="18520025781"
password="abcd1234"
cookiejar=cookielib.CookieJar()#cookie管理器
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))#打开按照这个cookie管理器
urllib2.install_opener(opener) #全局生效，urllib2打开

#抓取token
tokenReturn=urllib2.urlopen(url_baidu_token)
#print tokenReturn.read() #信息提取出来了，没有登陆
matchval=re.search( u'"token" : "(?P<tokenVal>.*?)"',tokenReturn.read())
tokenVal=matchval.group("tokenVal")
print "取出token----",tokenVal

#post登陆
postData={
'username':user,
'password':password,
'u':"https://passport.baidu.com/",
'tpl':'pp',
'token':tokenVal,
'staticpage':'https://passport.baidu.com/static/passpc-account/html/v3Jump.html',
'isPhone':'false',
'charset':"utf-8",
"callback":"parent.bd__pcbs__ra48vi"
}
postData=urllib.urlencode(postData) #编码转换
loginRequest=urllib2.Request(url_baidu_login,postData) #模拟登陆
#增加请求头，模拟真实浏览器
loginRequest.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8');
loginRequest.add_header('Accept-Encoding','gzip,deflate,sdch');
loginRequest.add_header('Accept-Language','zh-CN,zh;q=0.8');
loginRequest.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36');
loginRequest.add_header('Content-Type','application/x-www-form-urlencoded');
sendPost=urllib2.urlopen(loginRequest)#发起登陆请求


#不同的账号，贴吧的主页不一样
selfindex="http://tieba.baidu.com/home/main?id=9898706163686f6e6778696178696191a4"
content=urllib2.urlopen(selfindex).read()
print content.find("pachongxiaxia")
print content




















