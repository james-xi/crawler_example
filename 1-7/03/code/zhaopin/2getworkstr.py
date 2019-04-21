# encoding:utf-8
import  urllib2
import re
def  download1():
    url="http://jobs.zhaopin.com/344582482250000.htm?ssidkey=y&ss=201&ff=03&sg=64a3086a365945f8bbb56752adbbddd7&so=10"
    headers={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request=urllib2.Request(url,headers=headers)#发起请求，
    # 也可以通过调⽤Request.add_header() 添加/修改⼀个特定的 header
    request.add_header("Connection", "keep-alive") #一直活着
    response=urllib2.urlopen(request)
    data=response.read()#打开请求，抓取数据
    print response.code  # 可以查看响应状态码
    return data

data= download1()
restr = "<!-- SWSStringCutStart -->([\s\S]*?)<!-- SWSStringCutEnd -->"  # 正则表达式，（）只要括号内的数据
regex = re.compile(restr, re.IGNORECASE)
mylist = regex.findall(data)
print mylist
print mylist[0].decode("utf-8").strip().replace("<p>","").replace("</p>","")

