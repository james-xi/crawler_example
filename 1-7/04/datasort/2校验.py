
mystr=input("输入数据")
try:
    num=eval(mystr)
    print(num)
    print("ok")
except:
    print("fail")