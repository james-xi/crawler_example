# encoding:utf-8
import  urllib2
import urllib
def  download1(addr,mytype):
    url="http://sou.zhaopin.com/jobs/searchresult.ashx?"
    headers={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}


    word = {"jl":addr,"kw":mytype}
    word = urllib.urlencode(word)  # 编码成字符串
    url =url+word
    request=urllib2.Request(url,headers=headers)#发起请求，
    # 也可以通过调⽤Request.add_header() 添加/修改⼀个特定的 header
    request.add_header("Connection", "keep-alive") #一直活着
    response=urllib2.urlopen(request)
    data=response.read()#打开请求，抓取数据
    print response.code  # 可以查看响应状态码
    return data



addr="深圳" #urlopen只能处理http.不可以处理https
mytype="python"
print download1(addr,mytype)