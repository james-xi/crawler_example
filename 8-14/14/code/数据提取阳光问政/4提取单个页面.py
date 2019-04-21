# coding:utf-8
import requests
import chardet
import lxml
import lxml.etree
import re

def getdatafromurl(url):
    pagetxt = requests.get(url).content  # text返回unicode ,content  str
    #print pagetxt.decode("GB2312",errors="ignore") #必须解码
    myxml=lxml.etree.HTML(pagetxt.decode("GB2312",errors="ignore")) #编码
    #浏览器xpath  mytable=myxml.xpath("//*[@id=\"morelist\"]/div/table[2]/tbody/tr/td/table")
    mytable = myxml.xpath("//*[@cellpadding=\"0\"]//*[@cellpadding=\"1\"]")
    print mytable,len(mytable)
    idlist = []
    typelist = []
    titlelist = []
    aboutlist = []
    statuslist = []
    namelist =[]
    datelist = []
    for  line  in mytable:
        idlist = line.xpath("//td[1]/text()")
        typelist = line.xpath("//td[2]/a[1]/text()")
        titlelist = line.xpath("//td[2]/a[2]/text()")
        aboutlist = line.xpath("//td[2]/a[3]/text()")
        statuslist =  line.xpath("//td[3]/span/text()")
        namelist =  line.xpath("//td[4]/text()")
        datelist =  line.xpath("//td[5]/text()")
        print len(idlist),len(typelist),len(titlelist),len(aboutlist),len(statuslist),len(namelist),len(datelist)
        print idlist
        print namelist
        print datelist
        for  i  in range(len(typelist)):
            print idlist[i+1], typelist[i],titlelist[i],aboutlist[i] ,statuslist[i], namelist[i+1],datelist [i+1]


getdatafromurl("http://wz.sun0769.com/index.php/question/questionType?type=4&page=81240")
