# encoding:utf-8



import selenium  #测试框架
import selenium.webdriver #模拟浏览器
import  re
import matplotlib
import  matplotlib.pyplot as plt #数据可视化

matplotlib.rcParams["font.sans-serif"]=["simhei"] #配置字体
matplotlib.rcParams["font.family"]="sans-serif"

def  getnumberbyname(searchname):
    url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw="+searchname+"&p=1&isadv=0"
    driver=selenium.webdriver.Firefox()#调用火狐狸浏览器
    driver.get(url)#访问链接
    pagesource=driver.page_source #抓取网页源代码
    restr = "<em>(\\d+)</em>"  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(pagesource)
    driver.close()#关闭
    return mylist[0]

#print getnumberbyname("java")
pythonlist=[u"python",u"python 运维",u"python 测试",u"python 数据",u"python web"]
num=0
for  pystr in pythonlist:
    num+=1
    print pystr , eval(getnumberbyname(pystr))
    plt.bar([num], eval(getnumberbyname(pystr)), label=pystr)

plt.legend() #绘制
#plt.show() #显示