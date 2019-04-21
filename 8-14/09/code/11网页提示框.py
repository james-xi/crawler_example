#coding:utf-8
from  selenium import webdriver
import time
from  selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome() #配置参数
driver.get("https://www.baidu.com")
time.sleep(3)
above=driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(above).perform() #鼠标停留
time.sleep(1)

driver.find_element_by_link_text(u"搜索设置").click()
time.sleep(2)

driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(3)

driver.switch_to.alert.accept()

driver.close() #关闭当前

time.sleep(5)
driver.quit() #关闭全部