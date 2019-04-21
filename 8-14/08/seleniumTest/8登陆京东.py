#coding:utf-8
import selenium
import selenium.webdriver
import time
import lxml
import lxml.etree
driver = selenium.webdriver.Firefox()
driver.get("https://passport.jd.com/new/login.aspx")
time.sleep(3)
elem=driver.find_element_by_xpath("//*[@class=\"login-tab login-tab-r\"]/a")
elem.click()
#切换到账户登录

user=driver.find_element_by_id("loginname")
password=driver.find_element_by_id("nloginpwd")
submit=driver.find_element_by_id("loginsubmit")
user.clear()
password.clear()
time.sleep(1)
user.send_keys("yincheng5201314@163.com")
password.send_keys("yinchengak47")
time.sleep(1)
submit.click()

time.sleep(13)
driver.get("https://cart.jd.com/cart.action")
time.sleep(10)
data=driver.page_source
mytree=lxml.etree.HTML(data)
print  mytree.xpath("//*[@class=\"cell p-price\"]/strong/text()")

driver.close()