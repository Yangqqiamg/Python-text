"""错误总集：
    (1)URLError: 是error异常模块的基类，由request产生的异常都可以通过这个类来捕获
    (2)HTTPError： 是URLError 的子类，专门用于处理HTTP请求错误，比如认证失败等等。
                他有3个属性：
                code: 返回状态码，如404等
                reason： 用于返回错误的原因
                headers: 返回请求头


"""
# 一
from urllib import request, error
print('\none:')
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')  # 打开链接
except error.URLError as e:
    print(e.reason)  # 如果错误则打印错误信息

# 二
from urllib import request, error
print('\ntwo:')
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')

# 三
# 优先捕获子类错误，再去捕获父类错误，进行优化
from urllib import request, error
print('\nthree:')
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')

# 四
# reason返回的不一定是字符串，也可能是对象
import socket
import urllib.request
import urllib.error

print('\nfour:')
try:
    response = urllib.request.urlopen(
        'https://cuiqingcai.com/index.htm', timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))  # 打印错误类型
    # 判断如果类型是timeout，则做下一步处理
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")
