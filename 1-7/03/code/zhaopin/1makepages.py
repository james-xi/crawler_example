# encoding:utf-8
import selenium  #测试框架
import selenium.webdriver #模拟浏览器
import  re

def  getnumberbyname(searchname):
    url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw="+searchname+"&p=1&isadv=0"
    driver=selenium.webdriver.Firefox()#调用火狐狸浏览器
    driver.get(url)#访问链接
    pagesource=driver.page_source #抓取网页源代码
    restr = "<em>(\\d+)</em>"  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(pagesource)
    driver.close()#关闭
    return mylist[0]

num=eval(getnumberbyname("python")) #1731
if  num%60==0:
    pages=num//60
else:
    pages=num//60+1

mylist=[  "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=64a3086a365945f8bbb56752adbbddd7&p="+str(i)   for  i  in range(1,pages+1)]
for line in mylist:
    print line









