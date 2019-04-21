#coding:utf-8
from  selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome() #配置参数
driver.get("https://www.baidu.com")
above=driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(above).perform() #鼠标停留
#ActionChains(driver).move_to_element(above).move_to_element(elem)移动
ActionChains(driver).move_to_element(above).context_click() #鼠标，单击，双击
ActionChains(driver).move_to_element(above).double_click()
#ActionChains(driver).move_to_element(above).drag_and_drop() #拖放
time.sleep(10)
driver.close()