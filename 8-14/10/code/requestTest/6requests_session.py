#coding:utf-8
import requests
session=requests.Session()#会话
params={"username":"username","password":"passworda"}
mysession=session.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
print mysession.cookies.get_dict()
mysession=session.get("http://pythonscraping.com/pages/cookies/profile.php")
print mysession.text

