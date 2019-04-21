#coding:utf-8
import greenlet
import time
def   go1():
    while True:
        print "我是庞子卓，雪糕我吃一口"
        gr2.switch()
        time.sleep(1)

def go2():
    while True:
        print "我是杜江南，雪糕我吃一口"
        gr1.switch()
        time.sleep(1)

if __name__=="__main__":
    gr1=greenlet.greenlet(go1)
    gr2=greenlet.greenlet(go2)
    gr1.switch()