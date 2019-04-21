#coding:utf-8
import selenium
import selenium.webdriver
import time
path=r"C:\Users\Tsinghua-yincheng\Desktop\SZday8\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe"
driver=selenium.webdriver.PhantomJS(path)#打开无界面浏览器
driver.get("http://www.baidu.com")

elem=driver.find_element_by_id("kw")
elem.send_keys(u"尹成")
time.sleep(1)
elem.send_keys(selenium.webdriver.common.keys.Keys.RETURN)


time.sleep(3)
driver.save_screenshot("baidu.jpg")
print driver.title  #标题
print driver.page_source #网页源码
driver.close()