from urllib.parse import urlparse
"""方法urlparse():
 模板： urllib.parse.urlparse(urlstring, scheme='', allow_fragments=Ture)
urlparse()有三个参数：
1、 urlstring 必填，即待解析的url
2、scheme 默认的协议，如果url未指定，则返回scheme指定的协议，如果url有协议则看url的
3、allow_fragments 即是否忽略frament。

对URL进行解析:
下方例子：
1、type 解析类型
2、scheme 代表协议
3、netloc 域名
4、path 访问路径
5、params 代表参数
6、query 查询条件
7、fragment 锚点，用于直接定位页面内部的下拉位置
"""
result = urlparse('http://www.baidu.com/index.html;user?id=5#commemt')
print(type(result), '\n',result)

#output <class 'urllib.parse.ParseResult'>
#       ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html',
#                    params='user', query='id=5', fragment='commemt'

result2 = urlparse('http://www.bandu.com/index.html#comment', scheme='https',
                     allow_fragments=False)
#结果证明urlparse()生成的是一个元组
print(result2.scheme, result2[0], result2.netloc, result2[2], sep='\n')

print('\n')
"""urlunparse()方法：

用于构建URL，需要6个参数齐全
"""
from urllib.parse import urlunparse
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=7', 'comment']
print(urlunparse(data))

print('\n')

'''urlsplit()

与urlparse()类似，,也是元组，不同于把param归入了path
'''
from urllib.parse import urlsplit

result3 = urlsplit('http://www.baidu.com/index.html;user?id=5#commemt')
print(result3)
print(result3[0], result3.scheme, sep='\n')

print('\n')

'''urlunsplit():

与urlunparse()类似，只是是5个参数
'''
from urllib.parse import urlunsplit

data1 = ['http',  'www.baidu.com', 'index.html', 'a=7', 'comment']
print(urlunsplit(data1))

print('\n')
'''urljoin():

需要两个参数，一个基本链接，和一个新链接，用基本链接里的东西（scheme, netloc, path）
补全新链接，但不会替代新链接已有部分
'''
from urllib.parse import urljoin

print(urljoin('https://www.baidu.com', 'FQQ.html'))
print(urljoin('http://www.baidu.com/abuut.html', 'FQQ.html'))
print(urljoin('http://www.baidu.com/abuut.html', 'https://www.cidv.com/FQQ.html'))

'''urlencode():

用于构造GET请求参数时非常有用
'''
from urllib.parse import urlencode
params = {
    'name': 'germey',
    'age': 22,
}

bace_url = 'http://www.baidu.com?'
url = bace_url + urlencode(params)
print(url)

'''parse_qs():

把一串GET请求参数转化为字典
   parse_qsl():

把一串GET请求参数转化为元组
'''
from urllib.parse import parse_qs, parse_qsl

query = 'name=query&age=22'
print(parse_qs(query))

print(parse_qsl(query))

'''quote():

可以把中文参数转化为URL编码，防止产生产生乱码
   unquote():
把URL编码转化为中文参数
'''
from urllib.parse import quote, unquote

keyword = '美女'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

print(unquote(url))

