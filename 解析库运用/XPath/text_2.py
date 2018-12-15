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

#####################################################################
#按序选择 #
##########
html = etree.HTML(text)
#获取第一个li节点的信息
result = html.xpath('//li[1]/a/text()')
print(result)
#获取最后一个li节点的信息
result = html.xpath('//li[last()]/a/text()')
print(result)
#获取位置小于3的li节点的信息
result = html.xpath('//li[position()<3]/a/text()')
print(result)
#获取倒数第3个li节点的信息
result = html.xpath('//li[last()-2]/a/text()')
print(result)
#获取所有li节点的信息
result = html.xpath('//li/a/text()')
print(result)

print('\n')

#################################################################
#节点轴选择 #
############

text1 = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text1)
#调用sncestor轴 可以获取所有祖先节点，‘*’ 表示匹配所有节点
result = html.xpath('//li[1]/ancestor::*')
print(result)
#匹配有‘body’的祖先节点
result = html.xpath('//li[1]/ancestor::body')
print(result)
#调用arrribute轴 获取所有属性值
result = html.xpath('//li[1]/attribute::*')
print(result)
#调用child轴 获取所有直接子节点，这里获取所有href值为link1.html的a节点
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
#调用descendant轴 获取所有子孙节点， 这里限制获取span
result = html.xpath('//li[1]/descendant::span')
print(result)
#调用following轴 获取当前节点后的所有节点， 这里加了索引【2】，所以只获取了第二个
result = html.xpath('//li[1]/following::*[2]')
print(result)
#调用following-sibling轴 获取之后的所有同级节点
result = html.xpath('//li[1]/following-sibling::*')
print(result)
print('\n')


##############################################################
#