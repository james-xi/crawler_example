import selenium
import selenium.webdriver

url="http://www.51shucheng.net/kehuan/santi/santi1/174.html"
driver=selenium.webdriver.Chrome()
driver.get(url)
data=driver.find_elements_by_xpath("/*")
for  tag  in  data:
    print tag.text
driver.close()
