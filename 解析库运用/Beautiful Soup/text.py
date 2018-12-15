html1 = '''
<html><head><title>The Dormouse's story</title></head>
<body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters: and their name were
        <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>:
        and they lived at the bottom of a well.</p>
    <p class="story">...</p>
</body>
'''
#格式如下
from bs4 import BeautifulSoup
#导入文件html1， 并自动更正格式
soup = BeautifulSoup(html1, 'html')
#########################################
#使用string属性获取文本的值 #
###########################

#把字符串以标准的缩进格式输出
print(soup.prettify())
#输出title节点文本内容
print(soup.title.string)
#打印整个title节点
print(soup.title)
#打印titile节点类型
print(type(soup.title))
#打印整个head节点
print(soup.head)
#打印第一个p节点(多个同门节点时，打印第一个)
print(soup.p)
print('\n')
########################################
#使用name属性获取节点名称 #
#########################

print(soup.title.name)
print('\n')
########################################
#使用attrs属性获取节点所有属性 #
##############################

print(soup.p.attrs)
print(soup.p.attrs['name'])

#获取单个属性值

print(soup.p['class'])
print(soup.p['name'])
print('\n')

##########################################
# 嵌套选择 #
# #########

#打印head节点里的title节点
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)
print('\n')

###########################################
# 关联选择
# 当不能一步就确定到想要的节点时，先选一个基准节点，然后再选他的子、父节点
# 用contends属性
# ##########################

html2 = '''
<html><head><title>The Dormouse's story</title></head>
<body>
    <p class="story">Once upon a time there were three little sisters: and their name were
        <a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>:
        and they lived at the bottom of a well.</p>
    <p class="story">...</p>
</body>
'''
soup = BeautifulSoup(html2, 'html')
#返回的是列表格式，每个值都是p节点的直接子节点
print(soup.p.contents)

#使用children节点，获取子节点，获取的是生成器类型，需要用for循环输出
print(soup.p.children)
#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
#同时列出数据和数据下标。
for i, child in enumerate(soup.p.children):
    print(i, child)

#使用descendants属性，获取子孙节点，获取的是生成器类型，需要用for循环输出
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)

#使用parent属性，获取父节点
print('\n')
print(soup.a.parent)
print('\n')

#获取所有祖先节点要用parents属性,获取的是生成器类型
print(type(soup.a.parents))
print(soup.a.parents)
print(list(enumerate(soup.a.parents)))
print('\n')

#获取兄弟节点
#使用属性：
#           next_sibling      :获取下一个兄弟元素
#           previous_sibling ：获取上一个兄弟元素
#           next_siblings    ：获取下边所有兄弟元素
#           previous_siblings：获取前边所有兄弟元素
print(soup.a.next_sibling)
print(soup.a.previous_sibling)
print(list(enumerate(soup.a.next_siblings)))
print(list(enumerate(soup.a.previous_siblings)))

#提取信息
#获取 a节点的下一个兄弟节点的值的文本
print(soup.a.next_sibling.string)
#获取 a节点的所有祖先节点中的第0个的‘class属性的值
print(list(soup.a.parents)[0].attrs['class'])