# encoding:utf-8
import selenium  #测试框架
import selenium.webdriver #模拟浏览器
import  re
import urllib2
import urllib

def  geturllistsz(searchname):
    url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw="+searchname+"&p=1&isadv=0"
    driver=selenium.webdriver.Firefox()#调用火狐狸浏览器
    driver.get(url)#访问链接
    pagesource=driver.page_source #抓取网页源代码
    restr = "<em>(\\d+)</em>"  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(pagesource)
    driver.close()#关闭
    num=eval(mylist[0]) #1731
    if  num%60==0:
        pages=num//60
    else:
        pages=num//60+1

    mylist=[  "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=64a3086a365945f8bbb56752adbbddd7&p="+str(i)   for  i  in range(1,pages+1)]
    for line in mylist:
        print line
    return mylist


def  downloadgeturllist(url):
    #url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=64a3086a365945f8bbb56752adbbddd7&p=1"
    headers={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request=urllib2.Request(url,headers=headers)#发起请求，
    # 也可以通过调⽤Request.add_header() 添加/修改⼀个特定的 header
    request.add_header("Connection", "keep-alive") #一直活着
    response=urllib2.urlopen(request)
    data=response.read()#打开请求，抓取数据
    restr = "<div class=\"newlist_list_content\" id=\"newlist_list_content_table\">([\s\S]*?)<p class=\"newlist_list_top clearfix\">"  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(data)
    #print mylist[0]#抓取整个表格
    returnurllist=[] #存储url,最终返回

    restr = "<table([\s\S]*?)</table>"  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(mylist[0]) #循环每一行
    for line  in mylist:
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
        if   len( getnamelist)>0:
            print getlasturllist[0]
            returnurllist.append(getlasturllist[0]) #加入列表
            #print getvaluelist[0],getaddrlist[0],getlastcomlist[0],getlastnamelist[0],getlasturllist[0]
            #print "------------------------------------------------------------------"
    return  returnurllist

def  getworkinfo(url):
    #url="http://jobs.zhaopin.com/344582482250000.htm?ssidkey=y&ss=201&ff=03&sg=64a3086a365945f8bbb56752adbbddd7&so=10"
    headers={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request=urllib2.Request(url,headers=headers)#发起请求，
    # 也可以通过调⽤Request.add_header() 添加/修改⼀个特定的 header
    request.add_header("Connection", "keep-alive") #一直活着
    response=urllib2.urlopen(request)
    data=response.read()#打开请求，抓取数据

    restr = "<!-- SWSStringCutStart -->([\s\S]*?)<!-- SWSStringCutEnd -->"  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(data)
    #print mylist
    if  len(mylist)>0:
        laststr= mylist[0].decode("utf-8").strip().replace("<p>","").replace("</p>","")
        return  laststr
    else:
        return ""


savefilepath="workinfo.txt"
savefile=open(savefilepath,"wb")
urllist=geturllistsz("python")  #抓取urllist
for  url  in urllist:
    templist=downloadgeturllist(url)
    for  tempurl  in  templist:
        workstr=getworkinfo(tempurl)
        print workstr
        savefile.write((workstr+"\r\n").encode("utf-8"))
savefile.close()