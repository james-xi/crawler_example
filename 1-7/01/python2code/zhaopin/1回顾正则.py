# encoding:utf-8
import  re

mystr="""<span class=\"search_yx_tj\">
        共<em>5830</em>个职位满足条件
    </span>"""
restr="<em>(\\d+)</em>" #正则表达式，（）只要括号内的数据
regex=re.compile(restr,re.IGNORECASE)
mylist=regex.findall(mystr)
print mylist
print mylist[0]
