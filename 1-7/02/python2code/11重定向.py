# encoding:utf-8
import urllib2
"""
#判断有没有重定向
response=urllib2.urlopen("http://www.baidu.cn")
print  response.geturl()=="http://www.baidu.cn"
"""



class  RedirectHander(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers): #302重定向
        res= urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)#重定向以后的URL
        res.status=code  #返回的编码
        res.newurl=res.geturl() #当前的URL
        print res.newurl,res.status #重定向地址 ,302
        return res

opener=urllib2.build_opener(RedirectHander)
opener.open("http://www.baidu.cn/")







