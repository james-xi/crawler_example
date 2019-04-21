#coding:utf-8
import selenium
import selenium.webdriver
import time
import lxml
import lxml.etree
import requests
import urllib2




driver = selenium.webdriver.Chrome()
driver.get("https://passport.csdn.net/account/login?")
time.sleep(3)


user=driver.find_element_by_id("username")
password=driver.find_element_by_id("password")
submit=driver.find_element_by_class_name("logging")
user.clear()
password.clear()
time.sleep(1)
user.send_keys("yincheng01@163.com")
password.send_keys("yinchengak47.net")
time.sleep(1)
submit.click()
time.sleep(10) #等待页面加载，
cookies=driver.get_cookies()#抓取全部的cookie
print cookies
cookiestr=""
for  cookie  in cookies:#每一条cookie信息
    print cookie
    cookiestr+=(str(cookie["name"])+"="+str(cookie["value"])+";")
print "------------------------"
driver.close()




print "开始会话"
headers={
"Host": "my.csdn.net",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"DNT": "1",
"Referer": "http://www.csdn.net/",
#"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.8",
    u"cookie":cookiestr}
request=urllib2.Request("http://my.csdn.net/",headers=headers)
response=urllib2.urlopen(request)
newpagetext=response.read()
file=open("csdn.txt","wb")
file.write(newpagetext)
file.close()
print newpagetext
print "会话完成"

time.sleep(10)





time.sleep(10)
#driver.close()
