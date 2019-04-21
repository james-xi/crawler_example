#coding:utf-8
import  selenium
import selenium.webdriver
import selenium.webdriver.common.keys
import time

driver= selenium.webdriver.Firefox()
driver.get("https://job.alibaba.com/zhaopin/positionList.htm?keyWord=cHl0aG9u&_input_charset=UTF-8")
time.sleep(5)
print driver.page_source
elem=driver.find_element_by_xpath("//*[@class=\"pagination\"]//ul//li[last()]//a")
print elem
elem.click()
time.sleep(25)


driver.close()