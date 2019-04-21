#coding:utf-8
import selenium
import selenium.webdriver
import time
import lxml
import lxml.etree
import requests
import urllib2

'''


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
print "------------------------"
driver.close()

'''


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
    u"cookie":u"uuid_tt_dd=-1734079490838081701_20171010; bdshare_firstime=1507966544895; UserName=yincheng0571; UserInfo=LZTCl6p9mr%2BUgX1cEEgqwIand1mBReKkuogvIYHivh6MdgAq8c4Y4%2Fmx1uhFT%2FmWFuTu%2BCna36D%2BZ7ssW7xuzAjlIwc7Vgjd7Y7zTDJqy%2FakzOPFEGR52GRrp8sf0i9NK7p2hdvM39vRq5Y7NLJObQ%3D%3D; UserNick=%E8%8B%B1%E9%9B%84%E6%97%A0%E6%95%8C2017; AU=821; UD=%E5%A4%A9%E4%B8%8B%E8%90%A5%E9%94%80%E5%A4%A9%E4%B8%8B%E8%90%A5%E9%94%80%E5%A4%A9%E4%B8%8B%E8%90%A5%E9%94%80%E5%A4%A9%E4%B8%8B%E8%90%A5%E9%94%80%E5%A4%A9%E4%B8%8B%E8%90%A5%E9%94%80%E5%A4%A9%E4%B8%8B%E8%90%A5%E9%94%80%E5%A4%A9%E4%B8%8B%E8%90%A5%E9%94%80%E5%A4%A9%E4%B8%8B%E8%90%A5%E9%94%80; UN=yincheng0571; UE=\"yincheng01@163.com\"; BT=1508039179648; access-token=8260e0b7-a35c-419d-b4af-1f02d51c677d; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1507965242,1507969974,1508038063,1508039035; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1508039041; dc_tos=oxuidd; dc_session_id=1508039034960_0.6956040327941211" }
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














