#coding:utf-8
import requests
import requests.auth
#登陆路由器，
auth=requests.auth.HTTPBasicAuth("reryan","password12321321321")
req=requests.post(url="http://pythonscraping.com/pages/auth/login.php",auth=auth)
print req.text