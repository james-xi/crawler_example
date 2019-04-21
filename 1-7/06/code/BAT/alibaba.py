# encoding:utf-8
import  urllib2
import urllib
import lxml
import lxml.etree
import re
import selenium  #测试框架
import selenium.webdriver #模拟浏览器
import time
def  makeurllist(url):
    driver = selenium.webdriver.Firefox()  # 调用火狐狸浏览器
    driver.get(url)  # 访问链接
    time.sleep(5)
    pagesource = driver.page_source  # 抓取网页源代码
    #print pagesource
    mytree = lxml.etree.HTML(pagesource )
    numbers= eval(mytree.xpath("//*[@class=\"pagination\"]/ul//li[last()-1]/@data-index")[0])
    urllist=[]
    for i in range(1,numbers+1):
        urllist.append("https://job.alibaba.com/zhaopin/positionList.htm?keyWord=cHl0aG9u#page/"+str(i))
    driver.close()
    return urllist

def  gettitilefromurl(url):
    driver = selenium.webdriver.Firefox()  # 调用火狐狸浏览器
    driver.get(url)  # 访问链接
    time.sleep(5)
    pagesource = driver.page_source  # 抓取网页源代码
    # print pagesource
    mytree = lxml.etree.HTML(pagesource)
    mylist= mytree.xpath("//*[@id=\"J-list-box\"]//tr//td//span//a//text() ")
    for  line in mylist:
        print line.strip()

    mylist = mytree.xpath("//*[@id=\"J-list-box\"]//tr/td/span/a/@href ")
    for line in mylist:
        print line.strip()

    driver.close()


print gettitilefromurl("https://job.alibaba.com/zhaopin/positionList.htm?keyWord=cHl0aG9u&_input_charset=UTF-8")
#print  makeurllist("https://job.alibaba.com/zhaopin/positionList.htm?keyWord=cHl0aG9u&_input_charset=UTF-8#page/1")