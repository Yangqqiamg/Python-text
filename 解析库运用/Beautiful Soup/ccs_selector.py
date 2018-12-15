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
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
#选择class为panel 和panel-heading 中的元素
print(soup.select('.panel .panel-heading'))
#选择ul节点下所有li节点
print(soup.select('ul li'))
#选择id为list-2div 下包含class为element的元素
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

##########################
#嵌套选择
#选择所有ul节点
#从所选的ul节点中选li节点
print('')
for ul in soup.select('ul'):
    print(ul.select('li'))

##########################
#获取属性
#打印 ul 节点的属性值
#用直接传入法和使用attrs来获取
print('')
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

###########################
#获取文本
#使用string和get_text方法
#获取 li节点的文本
print('')
for li in soup.select('li'):
    print('Get Text: ', li.get_text())
    print('String: ', li.string)