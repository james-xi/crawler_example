#coding:utf-8
import selenium
import selenium.webdriver
import time
import lxml
import lxml.etree
import requests

driver = selenium.webdriver.Firefox()
driver.get("https://login.taobao.com/member/login.jhtml")
time.sleep(3)
elem=driver.find_element_by_class_name("login-switch")
elem.click()
time.sleep(3)

user=driver.find_element_by_id("TPL_username_1")
password=driver.find_element_by_id("TPL_password_1")
submit=driver.find_element_by_id("J_SubmitStatic")
user.clear()
password.clear()
time.sleep(1)
'''
18370802679
sxmxfdbz@jgl5257
'''
user.send_keys(u"感悟人生百态jl")
time.sleep(3)
password.send_keys("sxmxfdbz@jgl5257")
time.sleep(2)
submit.click()
time.sleep(25) #等待页面加载，
cookies=driver.get_cookies()#抓取全部的cookie
driver.close()

print "开始会话"
req=requests.session()#会话

for  cookie  in cookies:
    req.cookies.set(cookie['name'],cookie["value"])
req.headers.clear()#清空头
newpage=req.get("https://cart.taobao.com/cart.htm?")
print "会话完成"
print newpage.text  #页面



time.sleep(10)

