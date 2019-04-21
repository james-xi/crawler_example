#coding:utf-8
import urllib,urllib2,re,cookielib
#建立一个cookie管理器,用这个打开自带cookie
cookie=cookielib.CookieJar()
cookieproc=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(cookieproc)

headdata=opener.open("http://passport.csdn.net/").read().decode("utf-8")
pat1=re.compile(r"name=\"lt\" value=\"(.*?)\"")
pat2=re.compile(r"name=\"execution\" value=\"(.*?)\"")
b1=pat1.findall(headdata)
b2=pat2.findall(headdata) #挖掘两个加密信息

postData={
    "username":"yincheng01@163.com",
    "password":"yinchengak48.net",
    "lt":b1[0],
    "execution":b2[0],
    "_eventId":"submit"
}

postData=urllib.urlencode(postData) #编码

opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'),
                     ('Referer', 'http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn')
                     ]

response=opener.open("http://passport.csdn.net/",data=postData)
print response.read()

responsex=opener.open("http://my.csdn.net/my/mycsdn")
file=open("csdnff.html","w")
file.write(responsex.read())
file.close()
print  responsex.read().find("请您先登录")!=-1




