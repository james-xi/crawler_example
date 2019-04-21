#coding:utf-8
import  requests
import chardet


'''
             编码         类型       encode之后类型      decode之后类型
"a"          #ascii,     str            str               unicode
"中国"       #utf-8      str          不可编码             unicode
u"中国"      #utf-8     unicode        不可以编码          不可以解码
'''

def  geturl(url):
    pagetxt=requests.get(url).content #text返回unicode ,content  str
    print type(pagetxt) #str
    print chardet.detect(pagetxt) #gb2312
    return pagetxt.decode("GB2312",errors="ignore") #得到网页


print geturl("http://wz.sun0769.com/index.php/question/questionType?type=4&page=300")