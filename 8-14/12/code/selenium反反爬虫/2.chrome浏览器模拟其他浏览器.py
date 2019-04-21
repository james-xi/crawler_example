import selenium.webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
options=selenium.webdriver.ChromeOptions()
options.add_argument("lang=zh_CN.UTF-8")
options.add_argument("user-agent=\"Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20\"")

driver=selenium.webdriver.Chrome(chrome_options=options)
driver.get("http://www.httpbin.org/user-agent")
driver.get_screenshot_as_file("6.png")
driver.quit()