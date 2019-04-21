import  requests
import time
mycookie=dict(BDSID="zhadu")
req=requests.get("http://httpbin.org/cookies",cookies=mycookie)
time.sleep(3)
print req.cookies
print req.text