#coding:utf-8
import selenium
import selenium.webdriver
import time
import lxml
import lxml.etree
import requests

driver = selenium.webdriver.Firefox()
driver.get("https://kyfw.12306.cn/otn/login/init")

user=driver.find_element_by_id("username")
password=driver.find_element_by_id("password")

user.clear()
password.clear()
time.sleep(1)

user.send_keys("13694853330")
time.sleep(3)
password.send_keys("abc379464250")
time.sleep(2)


time.sleep(25) #等待页面加载，
cookies=driver.get_cookies()#抓取全部的cookie
driver.close()


print "开始会话"
req=requests.session()#会话

for  cookie  in cookies:
    req.cookies.set(cookie['name'],cookie["value"])
req.headers.clear()#清空头
newpage=req.get("https://kyfw.12306.cn/otn/modifyUser/initQueryUserInfo",verify=False)
print "会话完成"
print newpage.text  #页面
time.sleep(10)

