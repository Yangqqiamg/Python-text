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
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)


#########################################
#使用attr()方法来获取属性值
#选择class属性为 item-0和 active的节点内的 a节点
a =  doc('.item-0.active a')
#获取a节点内 href的值
print(a.attr('href'))
print(a.attr.href)
print('')
#多个节点属性时，需要使用items()遍历获取
a = doc('a')
for a1 in a.items():
    print(a1.attr('href'))
    print(a1.attr.href)
print('\n1')
########################################
#获取文本，使用text()
a = doc('.item-0.active a')
print(a.text())
#获取html文本使用html()
li = doc('.item-0.active')
print(li.html())

#遍历多个节点
li = doc('li')
print(li.text())
for item in li.items():
    print(item.html())
print('')
#########################################
#节点操作
#addClass(): 添加属性
#removeClass(): 删除属性
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

print('')
#attr():添加属性，第一个参数为属性名，第二个为值
#text():修改文本
#html():修改HTML文本
#总结：attr()方法只穿一个参数时，就是获取这个属性值，传两个时，就是添加属性
#     text()和 html()不传参数时就是获取文本和HTML文本，传入参数就时进行赋值
li.attr('name', 'link')
print(li)
li.text("change text")
print(li)
li.html('<span>change text</span>')
print(li)

##############################
#remove():移除节点、
#例子：
#     doc.find('p').remove()
#     寻找选中 p节点，然后调用remove()将其移除
#

################################
#伪类选择器

doc = pq(html)
li = doc(li:first-chirld)   #第一个 li节点
li = doc(li:last-chirld)    #最后一个 li节点
li = doc(li:nth-chirld(2))  #第二个
li = doc(li:gt(2))          #第三个之后的所有
li = doc(li:nth-chirld(2n)) #偶数的
li = doc(li:contains(second))#包含second的