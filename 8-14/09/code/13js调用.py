#coding:utf-8
from  selenium import webdriver
import time
from  selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome() #配置参数
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("kw").submit()

time.sleep(5)
js="window.scrollTo(200,550);" #调用js
driver.execute_script(js)
time.sleep(5)




driver.quit() #关闭全部