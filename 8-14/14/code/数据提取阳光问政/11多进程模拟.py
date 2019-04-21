#coding:utf-8
import multiprocessing
import time
def  go(N,name,queue):
    time.sleep(1)
    for  i  in range(N):
        queue.put(name+str(i)) #进程压入数据


if __name__=="__main__":
    queue=multiprocessing.Queue()#进程之间传递数据
    processlist = []

    for name in  ["A","B","C","E","F","G"]:
        process = multiprocessing.Process(target=go, args=(50,name,queue))
        process.start()
        processlist.append(process) #开启多个进程

    for p  in processlist:
       p.join()#等待所有进程退出
        
    while  not  queue.empty():
        data=queue.get()
        print "get",data
