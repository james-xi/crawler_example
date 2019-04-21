#coding:utf-8
import selenium
import selenium.webdriver
import time

driver = selenium.webdriver.Chrome()
driver.get("https://qzone.qq.com/")
time.sleep(3)
driver.switch_to_frame("login_frame")
elem=driver.find_element_by_id("switcher_plogin")
elem.click()
time.sleep(3)
user=driver.find_element_by_id("u")
password=driver.find_element_by_id("p")
loginbtn=driver.find_element_by_id("login_button")
user.send_keys("475318423")
password.send_keys("yincheng")
loginbtn.click()
time.sleep(6)
print driver.title #标题
#print driver.page_source->lxml,re,bs4

#print  driver.find_element_by_class_name("title-text ui-mr5").text
#print  driver.find_element_by_xpath("//span[@class=\"title-text ui-mr5\"]").text
print  driver.find_element_by_id("QZ_Space_Desc").text
#print  driver.find_element_by_xpath("//span[@class=\"user-name textoverflow\"]").text
print  driver.find_element_by_id("QM_OwnerInfo_Icon").get_attribute("src") #标签之间的东西


time.sleep(13)
driver.close()