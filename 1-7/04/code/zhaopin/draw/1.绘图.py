#coding:utf-8
import matplotlib
import  matplotlib.pyplot as plt #数据可视化

matplotlib.rcParams["font.sans-serif"]=["simhei"] #配置字体
matplotlib.rcParams["font.family"]="sans-serif"

plt.bar([1],[123],label=u"广东",color="g")
plt.bar([2],[113],label=u"江苏",color="y")
plt.bar([3],[133],label=u"山东")
plt.bar([4],[133],label=u"河南")
plt.bar([5],[133],label=u"浙江")
matplotlib.use("Agg")
plt.legend() #绘制
plt.savefig("1.jpg")
#plt.show() #显示
