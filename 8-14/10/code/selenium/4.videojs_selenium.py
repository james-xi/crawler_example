#coding:utf-8
import selenium
import selenium.webdriver
import time
url="http://videojs.com/"
driver=selenium.webdriver.Chrome()
driver.get(url)
time.sleep(3)
vedio=driver.find_element_by_class_name("vjs-big-play-button")
vedio.click()

#print driver.execute_script("")
time.sleep(10)
driver.close()
