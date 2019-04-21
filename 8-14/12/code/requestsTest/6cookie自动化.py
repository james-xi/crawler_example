
#coding:utf-8
import requests
session=requests.session()
req=session.get("http://v57.demo.dedecms.com/dede/login.php?",allow_redirects=True)
datas={ "gotopage":"/dede/index.php",
         "dopost":"login",
        "adminstyle":"newdedecms",
        "userid":"admin",
        "pwd":"admin",
        "sm1":""}
res=session.post("http://v57.demo.dedecms.com/dede/login.php?",data=datas)
print res.text
print "-----------------------------------------------------------"
res=session.get("http://v57.demo.dedecms.com/member/")
print res.text
