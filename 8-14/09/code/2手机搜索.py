#coding:utf-8
from  selenium import webdriver
import time

#设置
mobilesetting={"deviceName":"iPhone 6 Plus"}
options=webdriver.ChromeOptions()#选项
options.add_experimental_option("mobileEmulation",mobilesetting) #模拟手机
driver=webdriver.Chrome(chrome_options=options) #配置参数
driver.set_window_size(400,800)
driver.get("https://www.baidu.com")
time.sleep(1)
elem=driver.find_element_by_id("index-kw")
elem.send_keys(u"你妹")
time.sleep(1)
click=driver.find_element_by_id("index-bn")
click.click()

time.sleep(10)

driver.close()