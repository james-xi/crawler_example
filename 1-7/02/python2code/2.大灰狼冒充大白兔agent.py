# encoding:utf-8
import  urllib2
def  download1(url):
    headers={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request=urllib2.Request(url,headers=headers)#发起请求，
    # 也可以通过调⽤Request.add_header() 添加/修改⼀个特定的 header
    request.add_header("Connection", "keep-alive") #一直活着
    response=urllib2.urlopen(request)
    data=response.read()#打开请求，抓取数据
    print response.code  # 可以查看响应状态码
    return data

def  download2(url):
    return urllib2.urlopen(url).read()  #读取全部网页

url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=java&p=1&isadv=0" #urlopen只能处理http.不可以处理https
print download1(url)
