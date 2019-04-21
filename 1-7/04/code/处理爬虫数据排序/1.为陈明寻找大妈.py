# encoding:utf-8

filepath=r"C:\Users\Tsinghua-yincheng\Desktop\SZday4\nasa.txt"
readfile=open(filepath,"rb")
mydatalist= readfile.readlines()
for  line in mydatalist:
    print line.decode("gbk",errors="ignore")
readfile.close()