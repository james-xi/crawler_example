#coding:utf-8
from  selenium import webdriver
import time

#设置
mobilesetting={"deviceName":"iPhone 6 Plus"}
options=webdriver.ChromeOptions()#选项
options.add_experimental_option("mobileEmulation",mobilesetting) #模拟手机
driver=webdriver.Chrome(chrome_options=options) #配置参数
driver.set_window_size(400,800)
driver.get("https://login.m.taobao.com/login.htm")

username=driver.find_element_by_id("username")
password=driver.find_element_by_id("password")
username.send_keys("18520025781")
time.sleep(1)
password.send_keys("Zxcvbnm,1234")
time.sleep(2)
click=driver.find_element_by_id("btn-submit")
click.click()
time.sleep(35) #如果特定验证码比较麻烦，手动搞定，
driver.close()