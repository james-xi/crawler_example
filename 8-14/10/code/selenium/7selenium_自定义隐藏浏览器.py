#coding:utf-8
import  pyvirtualdisplay
import selenium.webdriver
display=pyvirtualdisplay.Display()
display.start()

#定制浏览器，
chrome_options=selenium.webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--incongnito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--start-maxminzed")
driver=selenium.webdriver.Chrome(chrome_options=chrome_options)
driver.delete_all_cookies()
driver.set_window_size(800,800)
driver.set_window_position(0,0)
print "OK"



driver.get("http://www.baidu.com")
print driver.page_source
driver.close()