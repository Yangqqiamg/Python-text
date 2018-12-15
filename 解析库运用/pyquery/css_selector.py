html = '''
<div class="wrap">
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="ltem-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''
'''
选择器              例子                  例子描述                    CSS
.class             .intro        选择 class="intro" 的所有元素。       1
#id             #firstname       选择 id="firstname" 的所有元素。      1
*                   *                   选择所有元素。                 2
element             p               选择所有 <p> 元素。                1
element,element     div,p       选择所有 <div> 元素和所有 <p> 元素。    1
element element     div p       选择 <div> 元素内部的所有 <p> 元素。    1
element>element     div>p    选择父元素为 <div> 元素的所有 <p> 元素。    2
element+element     div+p    选择紧接在 <div> 元素之后的所有 <p> 元素。  2
[attribute]         [target]    选择带有 target 属性所有元素。          2
'''

from pyquery import PyQuery as pq
new = pq(html)
#选取 id值为container的节点，然后内部选class为list的节点，然后选内部所有 li节点
print(new('#container .list li'))
print(type(new('#container .list li')))

###########################
#查找子节点

print('\n1,')
#获取new 中class为list的节点的内容
items = new('.list')
print(type(items))
print(items)
#find()获取的是节点的所有子孙节点
lis = items.find('li')
print(type(lis))
print(lis)
#children()是查找所有子节点
print(items.children())
#查找子节点中class为active的节点
print(items.children('.active'))

#################################
#使用parent()获取某个节点的父节点
container = items.parent()
print(type(container))
print(container)
print('1')

################################
#使用parents()获取祖先节点,且class为wrap值的
parents = items.parents('.wrap')
print(type(parents))
print(parents)
print('2')

################################
#使用siblings()获取兄弟节点
#先选择class为list的节点，然后内部选class为item-0和active的节点
li = new('.list .item-0.active')
print(li.siblings())
print('3')

################################
#遍历，多个节点使用items()来遍历，使用for循环
doc = pq(html)
lis = doc('li').items()
print(lis)
for li in lis:
    #print(type(li))
    print(li)