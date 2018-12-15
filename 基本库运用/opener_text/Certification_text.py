"""验证：

用于查看一些需要输入用户名的网页的基本设置
"""

from urllib.request import HTTPPasswordMgrWithDefaultRealm
from urllib.request import HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://localhost:5000/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)# 添加用户名和密码
auth_handler = HTTPBasicAuthHandler(p)# 进行实例化，建立一个处理验证的hander
opener = build_opener(auth_handler)# 构建一个Opener

try:
    result = opener.open(url)# 使用方法open()打开链接
    html = result.read().decode('utf=8')
    print(html)
except URLError as e:
    print(e.reason)
