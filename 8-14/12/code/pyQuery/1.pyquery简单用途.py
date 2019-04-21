#coding:utf-8
import pyquery
html="""
<html>
    <title>这是标题</title>
<body>
    <p id="hi">Hello</p>
    <ul>
        <li>list1</li>
        <li>list2</li>
    </ul>
</body>
</html>
"""
pyq=pyquery.PyQuery(html) #根据字符串初始化
print pyq('title')
print pyq("title").text()
print pyq("#hi")  #id=hi
print pyq("#hi").text()

lilist=pyq("li")
for  line in lilist:
    print pyq(line).text() #处理子元素
