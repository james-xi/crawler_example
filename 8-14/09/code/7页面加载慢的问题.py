#coding:utf-8
from  selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import  WebDriverWait #等待一个元素加载完成
from  selenium.webdriver.support import  expected_conditions as EC
import time

driver=webdriver.Chrome() #配置参数
driver.get("https://www.baidu.com")
driver.implicitly_wait(10) #控制操作的时间在10秒以内，如果元素出现，就继续执行，元素没有出现最多10秒

elem=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.ID,"kw"))) #节约时间，网页出现这个元素再操作
#最多等15秒，必须等到这个元素的出现

elem.send_keys("selenium")
time.sleep(10)
driver.close()