# coding:utf-8
import requests
import chardet
import lxml
import lxml.etree
import re

def geturlnumbers(url):
    pagetxt = requests.get(url).content  # text返回unicode ,content  str
    #print pagetxt.decode("GB2312",errors="ignore") #必须解码
    myxml=lxml.etree.HTML(pagetxt.decode("GB2312",errors="ignore")) #编码
    mylist= myxml.xpath("//*[@class=\"pagination\"]/text()") #抓取数量
    text= mylist[len(mylist) - 1].strip()  #正则表达式提取
    pat=re.compile("\d+",re.IGNORECASE)
    datalist=pat.findall(text)
    return eval(datalist[0])  #81389

def  makeurllist(numbers):
    urllist=[]
    if  numbers%30==0:
        for i  in range(numbers//30):
            urllist.append("http://wz.sun0769.com/index.php/question/questionType?type=4&page="+str(i*30))
    else:
        for i  in range(numbers//30+1):
            urllist.append("http://wz.sun0769.com/index.php/question/questionType?type=4&page=" + str(i * 30))
    return urllist

mylist=makeurllist(81389)
print len(mylist) #2713  10   9*300   13
for line in   mylist:
    print line


#print  geturlnumbers("http://wz.sun0769.com/index.php/question/questionType?type=4&page=300")
