#coding:utf-8
import gevent
import time
'''
def showwait(name,n):
    for  i  in range(n):
        print name ,"等待了",i+1,"秒"
        time.sleep(1)

showwait("庞子卓",10)
showwait("韩海飞",10)
showwait("李海宝",10)
'''
def showwait(name,n):
    for  i  in range(n):
        print name ,"等待了",i+1,"秒"
        gevent.sleep(1)  #不需要等待就顺序执行，需要等待，自动切换
        #time.sleep(1)


g1=gevent.spawn(showwait,"庞子卓",10)
g2=gevent.spawn(showwait,"韩海飞",10)
g3=gevent.spawn(showwait,"李海宝",10)
g1.join()
g2.join()
g3.join()
