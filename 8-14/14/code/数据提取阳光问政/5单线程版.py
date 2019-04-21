#coding:utf-8
import gevent
import gevent.monkey
import requests
import lxml
import re
import lxml.etree
gevent.monkey.patch_all()#自动切换

def  download(url,file):
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
    for line in mytable:
        idlist = line.xpath("//td[1]/text()")
        typelist = line.xpath("//td[2]/a[1]/text()")
        titlelist = line.xpath("//td[2]/a[2]/text()")
        aboutlist = line.xpath("//td[2]/a[3]/text()")
        statuslist = line.xpath("//td[3]/span/text()")
        namelist = line.xpath("//td[4]/text()")
        datelist = line.xpath("//td[5]/text()")
        mygetstr=""
        for i in range(len(typelist)):
            print idlist[i + 1], typelist[i], titlelist[i], aboutlist[i], statuslist[i], namelist[i + 1], datelist[
                i + 1]
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
        file.write(mygetstr.encode("utf-8",errors="ignore"))

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


numbers=geturlnumbers("http://wz.sun0769.com/index.php/question/questionType?type=4&page=81240")
urllist= makeurllist(numbers)
file=open("onethead.txt","wb")
for  url  in urllist:
    try:
        download(url, file)
    except:
        pass
file.close()
