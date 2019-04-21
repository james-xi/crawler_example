#coding:utf-8
import requests
import selenium
import selenium.webdriver
import time
from bs4 import BeautifulSoup
driver=selenium.webdriver.PhantomJS(r"C:\Users\Tsinghua-yincheng\Desktop\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get("http://www.hshfy.sh.cn/shfy/gweb/ktgg_search.jsp")
time.sleep(10)
driver.execute_script("javascript:goPage('2041')")
print "js is  run"
time.sleep(10)
#print driver.page_source
soup=BeautifulSoup(driver.page_source,"lxml")#解析数据
table=soup.find("table",attrs={"id":"report"})
trs=table.find("tr").find_next_siblings()
for  tr in  trs:
    tds=tr.find_all("td")
    for  td  in tds:
        print td.text

driver.quit()