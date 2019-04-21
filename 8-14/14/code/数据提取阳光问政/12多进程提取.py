# coding:utf-8
import multiprocessing
import time
import requests
import lxml
import re
import lxml.etree
import os

def  download(url,queue):
    print os.getpid(),"start"
    pagetxt = requests.get(url).content  # text返回unicode ,content  str
    # print pagetxt.decode("GB2312",errors="ignore") #必须解码
    myxml = lxml.etree.HTML(pagetxt.decode("GB2312", errors="ignore"))  # 编码
    # 浏览器xpath  mytable=myxml.xpath("//*[@id=\"morelist\"]/div/table[2]/tbody/tr/td/table")
    mytable = myxml.xpath("//*[@cellpadding=\"0\"]//*[@cellpadding=\"1\"]")
    idlist = []
    typelist = []
    titlelist = []
    aboutlist = []
    statuslist = []
    namelist = []
    datelist = []
    otherlist = []
    for line in mytable:
        idlist = line.xpath("//td[1]/text()")
        typelist = line.xpath("//td[2]/a[1]/text()")
        titlelist = line.xpath("//td[2]/a[2]/text()")
        aboutlist = line.xpath("//td[2]/a[3]/text()")
        statuslist = line.xpath("//td[3]/span/text()")
        namelist = line.xpath("//td[4]/text()")
        datelist = line.xpath("//td[5]/text()")
        print len(typelist)

        for i in range(len(typelist)):
            #print idlist[i + 1], typelist[i], titlelist[i], aboutlist[i], statuslist[i], namelist[i + 1], datelist[
            #   i + 1]
            mygetstr = ""
            mygetstr +=idlist[i + 1]
            mygetstr += " # "
            mygetstr += typelist[i]
            mygetstr += " # "
            mygetstr +=titlelist[i]
            mygetstr += " # "
            mygetstr += aboutlist[i]
            mygetstr += " # "
            mygetstr += statuslist[i]
            mygetstr += " # "
            mygetstr += namelist[i+1]
            mygetstr += " # "
            mygetstr += datelist[i+1]
            mygetstr+="\r\n"  #换行

            otherlist.append(mygetstr)
    for line in otherlist:
        pass
        queue.put(line)
        #print  line
    #queue.put(os.getpid())
    print os.getpid(), "end"
    return 1





if __name__ == "__main__":
    queue = multiprocessing.Queue(10000)  # 进程之间传递数据
    processlist = []

    for url in  ["http://wz.sun0769.com/index.php/question/questionType?type=4&page=81240",
                 "http://wz.sun0769.com/index.php/question/questionType?type=4&page=81270",
                 "http://wz.sun0769.com/index.php/question/questionType?type=4&page=81330",
                 "http://wz.sun0769.com/index.php/question/questionType?type=4&page=81300"]:
        process = multiprocessing.Process(target=download, args=(url, queue))
        process.start()
        processlist.append(process)  # 开启多个进程

    for p in processlist:
        p.join()  # 等待所有进程退出

    while not queue.empty():
        data = queue.Queue.get_nowait()
        print "get", data
