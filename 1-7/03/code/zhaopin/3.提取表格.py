#coding:utf-8
import  urllib2
import re
def  download1():
    url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=64a3086a365945f8bbb56752adbbddd7&p=1"
    headers={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request=urllib2.Request(url,headers=headers)#发起请求，
    # 也可以通过调⽤Request.add_header() 添加/修改⼀个特定的 header
    request.add_header("Connection", "keep-alive") #一直活着
    response=urllib2.urlopen(request)
    data=response.read()#打开请求，抓取数据
    print response.code  # 可以查看响应状态码
    return data

data= download1() #整个页面
restr = "<div class=\"newlist_list_content\" id=\"newlist_list_content_table\">([\s\S]*?)<p class=\"newlist_list_top clearfix\">"  # 正则表达式，（）只要括号内的数据
regex = re.compile(restr, re.IGNORECASE)
mylist = regex.findall(data)
#print mylist[0]#抓取整个表格
print "------------------------------------------------------------------"

restr = "<table([\s\S]*?)</table>"  # 正则表达式，（）只要括号内的数据
regex = re.compile(restr, re.IGNORECASE)
mylist = regex.findall(mylist[0])
for line  in mylist:
    #print line
    restr = "<td class=\"zwyx\">([\s\S]*?)</td>"  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    getvaluelist = regex.findall(line)  #价格

    restr = "<td class=\"gzdd\">([\s\S]*?)</td>"  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    getaddrlist = regex.findall(line)  # 价格

    restr = " <td class=\"gsmc\">([\s\S]*?)</td>"  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    getcomlist = regex.findall(line)  # 价格
    if len(getcomlist)>0:
        restr = " target=\"_blank\">([\s\S]*?)</a>"  # 正则表达式，（）只要括号内的数据
        regex = re.compile(restr, re.IGNORECASE)
        getlastcomlist = regex.findall(getcomlist[0])  # 价格

    restr = "<td class=\"zwmc\"([\s\S]*?)</td>"  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    getnamelist = regex.findall(line)  # 价格
    if len( getnamelist) > 0:
        restr = " target=\"_blank\">([\s\S]*?)</a>"  # 正则表达式，（）只要括号内的数据
        regex = re.compile(restr, re.IGNORECASE)
        getlastnamelist = regex.findall( getnamelist[0])  # 价格

        restr = "href=\"([\s\S]*?)\""  # 正则表达式，（）只要括号内的数据
        regex = re.compile(restr, re.IGNORECASE)
        getlasturllist = regex.findall(getnamelist[0])  # 价格


    if  len(getaddrlist)>0  and  len(getvaluelist)>0   and  len(  getlastcomlist)>0  and  len( getlastnamelist)>0:
        print getlasturllist[0]
        #print getvaluelist[0],getaddrlist[0],getlastcomlist[0],getlastnamelist[0],getlasturllist[0]
        #print "------------------------------------------------------------------"

