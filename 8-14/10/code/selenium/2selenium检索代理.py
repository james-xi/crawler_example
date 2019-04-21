import selenium
import selenium.webdriver

url="http://www.kuaidaili.com/free/inha/4/"
driver=selenium.webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
elems=driver.find_elements_by_xpath("//tbody/tr")
print type(elems),elems
for elem in elems:
    print elem.find_elements_by_xpath("./td")[0].text
    print elem.find_elements_by_xpath("./td")[1].text

driver.close()