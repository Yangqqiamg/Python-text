html = '''
<div>
    <ul>
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="ltem-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''

#####################################################
#基本初始化，以字符串形式传递
###############################
from pyquery import PyQuery as pq
#初始化
doc = pq(html)
#格式：打印 li节点
print(doc('li'))

############################
#传入URL获取
print('')
do = pq(url='https://cuiqingcai.com')
#打印了上述URL第一个 title节点的内容
print(do('title'))

############################
#传入文件并解析

print('')
#导入本地html文件
doc = pq(filename='text.html')
#打印 ul节点
print(doc('ul'))
