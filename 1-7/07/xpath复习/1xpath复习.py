#coding:utf-8
import  urllib2
import urllib
import lxml
import lxml.etree

def geturllistfrompage(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url, headers=headers)  # 发起请求，
    response = urllib2.urlopen(request)
    data=response.read()
    mytree = lxml.etree.HTML(data)
    #print (mytree.xpath("//*[@class=\"BDE_Image\"]/@src"))
    urllist=[]
    numbers=eval (mytree.xpath("//*[@class=\"l_reply_num\"]//span[last()]/text()")[0])
    for  i in range (1,numbers+1):
        urllist.append(url+"?pn="+str(i))
    return  urllist

def getjpglistfrompage(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url, headers=headers)  # 发起请求，
    response = urllib2.urlopen(request)
    data=response.read()
    mytree = lxml.etree.HTML(data)
    jpglist= (mytree.xpath("//*[@class=\"BDE_Image\"]/@src"))
    jpgnumbers=0
    for  jpgurl  in  jpglist:
        urllib.urlretrieve(jpgurl,"jpg/"+str(jpgnumbers)+".jpg")
        jpgnumbers+=1


#print   getjpglistfrompage("http://tieba.baidu.com/p/5367239393")

getjpglistfrompage("http://tieba.baidu.com/p/5367239393?pn=1")