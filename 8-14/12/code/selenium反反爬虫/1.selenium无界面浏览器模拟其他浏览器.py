#coding:utf-8
import selenium.webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap=dict(DesiredCapabilities.PHANTOMJS)#处理无界面浏览器
#dcap["phantomjs.page.settings.userAgent"]=("Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36")
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)
driver=selenium.webdriver.PhantomJS(executable_path=r"C:\Users\Tsinghua-yincheng\Desktop\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe",desired_capabilities=dcap)
driver.get("http://www.httpbin.org/user-agent")
driver.get_screenshot_as_file("4.png")
driver.quit()