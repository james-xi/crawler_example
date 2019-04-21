import requests
proxies={"http":"http://10.36.132.56:808",
         "https": "http://10.36.132.56:808"}
#{"http":"yincheng:111111@10.36.132.41:808"})
print requests.get("https://www.baidu.com",proxies=proxies).text
