from lxml import etree
text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''
#调用HTML类进行初始化文本，构成一个XPath解析对象，etree模块会自动修正HTML文本
html = etree.HTML(text)
#tostring()可输出HTML文本，但是是bytes型，要转换
result = etree.tostring(html)
#将utf-8编码转换成unicode编码(str类型),并打印
#print(result.decode('utf-8'))

#############################################################################
#读取文件进行解析

from lxml import etree

html = etree.parse('./text.html', etree.HTMLParser())
#获取整个文本
#result1 = etree.tostring(html)
#获取指定文本
#'*'为匹配所有节点
result2 = html.xpath('//*')
#print(result1.decode('utf-8'))
print(result2)
print('\n2、')

#2、匹配li节点
result3 = html.xpath('//li')
print(result3)
#列表第0个对象
print(result3[0])
print('\n3、')

#3、匹配子节点、子孙节点
#匹配li下的子节点a
result4 = html.xpath('//li/a')
print(result4)
#匹配ul下的子孙节点a
result5 = html.xpath('//ul//a')
print(result5)
print('\n4、')

#4、获取父节点及属性
#先确定子节点，然后限制子节点属性, 用'..'定位父节点，最后获取class属性
result6 = html.xpath('//a[@href="link4.html"]/../@class')
print(result6)
result7 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result7)
print('\n5、')

#5、属性匹配
result8 = html.xpath('//li[@class="item-0"]')
print(result8)
print('\n6、')

#6、文本获取 使用text()
#获取时记得要正确使用规则，到正确的位置获取文件
#一步步获取子字节
result9 = html.xpath('//li[@class="item-0"]/a/text()')
print(result9)
#获取子孙字节
result10 = html.xpath('//li[@class="item-0"]//text()')
print(result10)
print('\n7、')

#7、属性获取 使用符号‘@’
#获取所有li下所有a节点的href属性
result11 = html.xpath('//li/a/@href')
print(result11)
print('\n8、')

#8、属性多值匹配 使用contains()
#
text1 = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
#调用HTML类进行初始化文本，构成一个XPath解析对象，etree模块会自动修正HTML文本
html = etree.HTML(text1)
#通过contains()方法，第一个参数传入属性名称，第二个传入传入值，只要包含，就可以匹配
result12 = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result12)
print('\n9、')

#9、多属性匹配 使用contains() 和 ‘and’
text2 = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text2)
result13 = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result13)