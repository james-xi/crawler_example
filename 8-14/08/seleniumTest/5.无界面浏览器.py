#coding:utf-8
import selenium
import selenium.webdriver
import time
path=r"C:\Users\Tsinghua-yincheng\Desktop\SZday8\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe"
driver=selenium.webdriver.PhantomJS(path)#打开无界面浏览器
driver.get("http://www.qq.com")
time.sleep(3)
driver.save_screenshot("qq.jpg")
print driver.title  #标题
print driver.page_source #网页源码
driver.close()