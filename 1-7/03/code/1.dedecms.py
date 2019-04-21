#coding:utf-8
import  urllib2
import  urllib
import cookielib
url1="http://v57.demo.dedecms.com/dede/login.php?gotopage=%2Fdede%2Findex.php"
url2="http://v57.demo.dedecms.com/dede/index.php"

jar=cookielib.LWPCookieJar()#创建一个cookie管理器
cookieprocessor=urllib2.HTTPCookieProcessor(jar) #http.cookie管理工具
opener=urllib2.build_opener(cookieprocessor,urllib2.HTTPHandler) #创建一个打开工具
urllib2.install_opener(opener)#安装一个打开器
response=urllib2.urlopen(url1) #打开第一个链接，必须登陆

PostData={  "dopost":"login",
            "adminstyle": "newdedecms",
            "userid": "admin",
            "pwd": "admin",
            "sm1": "",
            }
PostData=urllib.urlencode(PostData) #编码--dopost=login&adminstyle=newdedecms&userid=admin&pwd=admin&sm1=
headers={'Referer':'http://v57.demo.dedecms.com/dede/login.php?gotopage=%2Fdede%2Findex.php',
          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'}
#开启一个请求头

request=urllib2.Request(url1,PostData,headers)#post传递消息
responsenew=urllib2.urlopen(request)
print responsenew.read()

print "-------------------------------------------------------------"
print "-------------------------------------------------------------"
responsenew2=urllib2.urlopen(url2)
print responsenew2.read()



