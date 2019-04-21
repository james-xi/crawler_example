#coding:utf-8
import requests
try:
    url="http://www.google.com/"
    response=requests.get(url,timeout=5)
    print response.status_code
    print response.text
except  requests.exceptions.ConnectionError as e:
    print e
print "over"