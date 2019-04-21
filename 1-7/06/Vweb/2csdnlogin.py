#coding:utf-8
import  selenium
import selenium.webdriver
import selenium.webdriver.common.keys
import time

driver= selenium.webdriver.Firefox()
driver.get("https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn")
elem=driver.find_element_by_id("username")
elem.send_keys("18520025781")
time.sleep(3)
elem=driver.find_element_by_id("password")
elem.send_keys("abcd1234")
time.sleep(5)
elem.send_keys(selenium.webdriver.common.keys.Keys.RETURN)
time.sleep(15)
print driver.page_source
driver.close()