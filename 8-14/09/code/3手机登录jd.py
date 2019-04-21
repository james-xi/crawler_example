#coding:utf-8
from  selenium import webdriver
import time

#设置
mobilesetting={"deviceName":"iPhone 6 Plus"}
options=webdriver.ChromeOptions()#选项
options.add_experimental_option("mobileEmulation",mobilesetting) #模拟手机
driver=webdriver.Chrome(chrome_options=options) #配置参数
driver.set_window_size(400,800)
driver.get("https://www.jd.com")
time.sleep(1)
elem=driver.find_element_by_id("index_searchLogin")
elem.click()
time.sleep(5)
username=driver.find_element_by_id("username")
password=driver.find_element_by_id("password")
username.send_keys("yincheng5201314@163.com")
time.sleep(1)
password.send_keys("yincheng8848")
time.sleep(2)
click=driver.find_element_by_id("loginBtn")
click.click()
time.sleep(15)
driver.close()