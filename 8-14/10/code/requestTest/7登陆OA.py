#coding:utf-8
import requests
session=requests.Session()#会话
#emp_no=admin&password=admin
params={"emp_no":"admin","password":"admin1"}
mysession=session.post("http://demo.smeoa.com/index.php?m=&c=public&a=check_login",params)
print mysession.cookies.get_dict()
mysession=session.get("http://demo.smeoa.com")
print mysession.text