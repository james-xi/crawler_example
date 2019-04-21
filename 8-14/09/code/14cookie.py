#coding:utf-8
from  selenium import webdriver
import time
from  selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome() #配置参数
driver.get("https://www.youdao.com")
#driver.find_element_by_id("kw").send_keys("python")
#driver.find_element_by_id("kw").submit()
driver.add_cookie({'name' : 'foo', 'value' : 'bar'}) #增加cookie

print driver.get_cookies() #抓取cookie
print driver.get_cookie("foo")  #抓取特定的cookie
for  line  in driver.get_cookies():
    print line



driver.quit() #关闭全部