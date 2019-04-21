#coding:utf-8
import selenium
import selenium.webdriver
import time

def  loginoa(username,password):
    driver=selenium.webdriver.Chrome()
    driver.get("http://demo.smeoa.com")
    time.sleep(3)

    #。抓取账户密码的文本框，输入账户密码，
    user_text=driver.find_element_by_id("emp_no")
    password_text=driver.find_element_by_id("password")
    time.sleep(1)
    user_text.send_keys(username)
    password_text.send_keys(password)
    time.sleep(3)
    #找到按钮，模拟登陆
    login=driver.find_element_by_id("login_btn")
    login.click()
    time.sleep(3)
    islogin=  driver.page_source.find(u"退出")!=-1
    time.sleep(3)
    driver.close()
    return  islogin

print loginoa("admin","admin")
