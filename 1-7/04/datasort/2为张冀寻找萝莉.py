# encoding:utf-8
def  checkstr(mystr):
    try:
        num=eval(mystr)
        return True
    except:
        return False


filepath=r"C:\Users\Tsinghua-yincheng\Desktop\SZday4\nasa.txt"
readfile=open(filepath,"rb")
mydatalist= readfile.readlines()
mynewlist=[]
for  line in mydatalist:
    line=line.decode("gbk","ignore")
    linelist=line.split("\t")
    if  len(linelist)>19  :  #筛选数据
        if  checkstr(linelist[3]):
            #print (linelist)
            mynewlist.append(linelist)#存储列表，每个元素都是列表
readfile.close()

mynewlist.sort(key=lambda x:eval(x[3])) #根据第三个排序，转化为整数
#mynewlist.reverse() #反转，


savefile=open("zhangji.txt","w")
for data  in  mynewlist:
    print(data)
    savefile.write(str(data)+"\r\n")
savefile.close()



