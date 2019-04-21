#coding:utf-8
import selenium.webdriver
import time

options=selenium.webdriver.ChromeOptions()
prefs={"profile.default_content_setting_values":{"images":2}}
options.add_experimental_option("prefs",prefs) #不加载图片
driver=selenium.webdriver.Chrome(chrome_options=options)
driver.get("http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%B0%B9%E6%88%90")

time.sleep(15)#不加载图片
driver.quit()