# encoding:utf-8
def  xueli(study):
    if study=="博士后":
        return 10
    elif study=="博士":
        return 9
    elif study=="硕士":
        return 8
    elif study=="本科":
        return 7
    elif study=="大专":
        return 6
    elif study=="高中":
        return 5
    elif study=="中专":
        return 4
    elif study=="初中":
        return 3
    elif study=="小学":
        return 2
    elif study=="幼儿园":
        return 1
    else:
        return 0

filepath=r"C:\Users\Tsinghua-yincheng\Desktop\SZday4\nasa.txt"
readfile=open(filepath,"rb")
mydatalist= readfile.readlines()
mynewlist=[]
for  line in mydatalist:
    line=line.decode("gbk","ignore")
    linelist=line.split("\t")
    if  len(linelist)>19  :  #筛选数据
            mynewlist.append(linelist)#存储列表，每个元素都是列表
readfile.close()

mynewlist.sort(key=lambda x:xueli(x[5])) #根据第三个排序，转化为整数
mynewlist.reverse() #反转，


savefile=open("youqiang.txt","w")
for data  in  mynewlist:
    print(data)
    savefile.write(str(data)+"\r\n")
savefile.close()



