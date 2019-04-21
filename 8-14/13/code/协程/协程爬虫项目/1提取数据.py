#coding:utf-8
import requests
import selenium
import selenium.webdriver
import time
driver=selenium.webdriver.PhantomJS(r"C:\Users\Tsinghua-yincheng\Desktop\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get("http://www.hshfy.sh.cn/shfy/gweb/ktgg_search.jsp")
time.sleep(10)
driver.execute_script("javascript:goPage('2041')")
print "js is  run"
time.sleep(10)
print driver.page_source
driver.quit()









'''
def get_html_post(url,data):
    response=requests.post(url,data=data)
    return response.text


postdata={
    "yzm":"UXEa",
    "ft":"",
    "ktrqks":"2017-10-16",
    "ktrqjs":"2017-11-16",
    "spc":"",
    "yg":"",
    "bg":"",
    "ah":"",
    "pagesnum":"1943"
}
print get_html_post("http://www.hshfy.sh.cn/shfy/gweb/ktgg_search.jsp",postdata)
'''


'''
def get_html_get(url): #get不能取得信息
    response=requests.get(url)
    return response.text
'''
#print get_html_get("http://www.hshfy.sh.cn/shfy/gweb/ktgg_search.jsp")
