#encoding:utf-8
import chardet
s="helloa"
print s
print chardet.detect(s)  #ascii,



s1="hellob"
print s1
print type(s1.encode("utf-8"))  #返回，str类型
print type(s1.decode("utf-8"))  #返回，unicode类型
print chardet.detect(s1)
print chardet.detect(s1.encode("utf-8")) #按照uft-8编码
#print chardet.detect(s1.decode("utf-8")) #按照uft-8解码
s2= "s中国"
print "----",s2
print "-----",type(s2) #str
print "-----",chardet.detect(s2) #utf-8
#print type(s2.encode("utf-8"))  #不能编码
print type(s2.decode("utf-8"))  #返回，unicode类型

s3= u"s中国"
print "----",s3
print "-----",type(s3) #unicode
print type(s3.decode("utf-8"))  #返回，unicode类型
print type(s3.encode("utf-8"))  #返回，unicode类型
print "-----",chardet.detect(s3) #utf-8









