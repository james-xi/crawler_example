#coding:utf-8
import urllib
import urllib2
import  re

#抓取贴吧页面数量信息
def  gettiebalistnumbers(name):
    url="http://tieba.baidu.com/f?"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    word = { "kw": name} #贴吧的名字
    word = urllib.urlencode(word)  # 编码成字符串
    url = url + word #拼接URL
    request = urllib2.Request(url, headers=headers)  # 发起请求，
    # 也可以通过调⽤Request.add_header() 添加/修改⼀个特定的 header
    request.add_header("Connection", "keep-alive")  # 一直活着
    response = urllib2.urlopen(request)
    data = response.read()  # 打开请求，抓取数据


    restr="<span class=\"card_infoNum\">([\s\S]*?)</span>" # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall( data) #寻找页面所有符合条件
    tienumbers= mylist[0].replace(",","")  #替换,
    tienumbers=eval(tienumbers) #转化为数字

    restr = "<span class=\"card_menNum\">([\s\S]*?)</span>"  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(data)  # 寻找页面所有符合条件
    Pepolenumbers = mylist[0].replace(",", "")  # 替换,
    Pepolenumbers = eval(Pepolenumbers)  # 转化为数字
    return Pepolenumbers,tienumbers

def  gettiebalist(name):
    numberstuple=gettiebalistnumbers(name)
    tienumbers=numberstuple[1] #帖子的数量
    tiebalist = [] #列表
    if tienumbers%50==0: #生成页面列表
        for  i  in range(tienumbers//50):
            tiebalist.append("http://tieba.baidu.com/f?kw="+name+"&pn="+str(i*50))
    else:
        for  i  in range(tienumbers//50+1):
            tiebalist.append("http://tieba.baidu.com/f?kw="+name+"&pn="+str(i*50))
    return tiebalist

def  geturllistfrompage(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url, headers=headers)  # 发起请求，
    response = urllib2.urlopen(request)
    data = response.read()  # 打开请求，抓取数据

    restr = "<ul id=\"thread_list\" class=\"threadlist_bright j_threadlist_bright\">([\s\S]*?)<div class=\"thread_list_bottom clearfix\">"  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(data)
    #print mylist[0]#抓取整个表格
    tablestr=mylist[0]

    restr = "href=\"/p/(\d+)\""  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    urltitlelist = regex.findall(tablestr)
    #print urltitlelist
    urllist = []
    for title  in urltitlelist:
        urllist.append("http://tieba.baidu.com/p/"+title)
    return urllist

def  getpagedata(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url, headers=headers)  # 发起请求，
    response = urllib2.urlopen(request)
    data = response.read()  # 打开请求，抓取数据
    return data

def getemaillistfrompage(pagedata):
    restr = r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})"  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    emaillist = regex.findall(pagedata)
    return emaillist

def getQQlistfrompage(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url, headers=headers)  # 发起请求，
    response = urllib2.urlopen(request)
    QQlist = []
    while True:
        line=response.readline()
        if not line:
            break
        if line.find("QQ")!=-1 or  line.find("Qq")!=-1  or   line.find("qq")!=-1:
            restr = "[1-9]\\d{4,10}"  # 正则表达式，（）只要括号内的数据
            regex = re.compile(restr, re.IGNORECASE)
            templist = regex.findall(line)
            QQlist.extend(templist )

    return QQlist


#print gettiebalistnumbers("python")

'''
mylist=gettiebalist("python3")
for line  in mylist:
    print line


print  geturllistfrompage("http://tieba.baidu.com/f?kw=python3&pn=12250")
'''

#print getemaillistfrompage(getpagedata("http://tieba.baidu.com/p/3950107421"))

print  getQQlistfrompage("http://tieba.baidu.com/p/3950107421")
