import  urllib.request
def  download(url):
    response=urllib.request.urlopen(url,timeout=10) #
    print(type(response))#class 'http.client.HTTPResponse
    print(response.info())
print(download("http://www.baidu.com"))