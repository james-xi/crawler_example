#coding:utf-8
import gevent
import gevent.monkey
import selenium
import selenium.webdriver
from bs4 import BeautifulSoup
import time
gevent.monkey.patch_all()#自动切换

def  download(url,start,end,file):
    driver = selenium.webdriver.PhantomJS( r"C:\Users\Tsinghua-yincheng\Desktop\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    driver.get(url)
    gevent.sleep(10)
    #0，100  100 200  200 300
    for  i   in  range(start,end):
        js="javascript:goPage('"+str(i)+"')"
        driver.execute_script(js)
        print "js is  run",i,
        gevent.sleep(10)  #循环提取页面
        #提取页面的数据
        soup = BeautifulSoup(driver.page_source, "lxml")  # 解析数据
        table = soup.find("table", attrs={"id": "report"})
        trs = table.find("tr").find_next_siblings()
        for tr in trs:
            tds = tr.find_all("td")
            linestr="" #拼合数据
            for td in tds:
                linestr += td.text
                linestr += " # "
            linestr+="\r\n"
            print linestr
            file.write(linestr.encode("utf-8",errors="ignore"))#写入保存到文件
    driver.quit()


url="http://www.hshfy.sh.cn/shfy/gweb/ktgg_search.jsp"
file=open("save.txt","wb") #保存文件
gevent.joinall([
    gevent.spawn(download,url,0,2,file),
    gevent.spawn(download,url,2,4,file),
    gevent.spawn(download,url,4,6,file),
    gevent.spawn(download,url,6,8,file),
    gevent.spawn(download,url,8,10,file),
])
file.close()