#coding:utf-8
import selenium
import selenium.webdriver
import time
import os
print os.getcwd()
options=selenium.webdriver.ChromeOptions()
prefs={"profile.default_content_setting.popups":0,  #下载不提示
       "download.default_directory":r"C:\Users\Tsinghua-yincheng\Desktop\SZday10"} #下载的路径，新版本的chrome
options.add_experimental_option("prefs",prefs)
driver=selenium.webdriver.Chrome()
driver.get("https://pypi.python.org/pypi/selenium")
driver.find_element_by_partial_link_text("tar.gz").click()
