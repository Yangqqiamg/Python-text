
html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello!</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
##########################################
#find_all():查询所有符合条件的元素
##########################################
#返回了列表
#name ： 查询所有节点名为 "XX"的节点
print(soup.find_all(name="ul"))
print(type(soup.find_all(name="ul")))
print('')
#嵌套使用,用for循环，在找到所有 ul节点后，从中找 li节点
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name="li"))
    #再循环答应每个 li节点的文本
    for li in ul.find_all(name="li"):
        print(li.string)

print('')

#atttrs=XX :传入属性查询， 参数类型为字典，传入属性和值
#
#查找属性为 id 和值为 list-1的元素
print(soup.find_all(attrs={'id': 'list-1'}))
#同上使用
print(soup.find_all(attrs={'name': 'elements'}))

#常用属性比如id和class等可以不用attrs从、来传递，可以直接使用
print(soup.find_all(id='list-1'))
#class 是一个关键字，需要加"_"
print(soup.find_all(class_="element"))

print('')

#text参数可以用于匹配文本，传入的形式可以是字符串也可以是正则表达式对象
import re
html1 = '''
<div class="panel">
    <div calss="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link,too</a>
    </div>
</div>
'''
soup1 = BeautifulSoup(html1, 'lxml')
#正则表达式对象
print(soup1.find_all(text=re.compile('link')))

###############################
#其他方法：
#
#       find():返回第一个符合元素
#       find_parent():返回父节点
#       find_parents():返回祖先节点
#       find_next_siblings():返回节点后所有兄弟节点
#       find_next sibling():返回节点后第一个兄弟节点
#       find_previous_siblings():返回节点前所有兄弟节点
#       find_previous_sibling():返回节点前第一个兄弟节点
#       find_all_next():返回节点后所有符合节点
#       find_next():返回节点后第一个符合节点
#       find_all_previous():返回节点前所有符合的节点
#       find_previous():返回节点前第一个符合的节点