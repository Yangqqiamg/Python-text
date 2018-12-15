'''获取并分析robots.txt文件

使用RobotFileParser()， 格式如下：
urllib.robotparser.RobotFileParser(url='')
'''
from urllib.robotparser import RobotFileParser

urly = 'http://www.jianshu.com/search?q=python&page=1&type=collections'
rp = RobotFileParser()  # 创建对象
rp.set_url('http://www.jianshu.com/robots.txt')  # 添加链接
rp.read()                                      # 读取robots.txt文件并分析
# can_fetch()两个参数，一个是User-agent，一个是要抓取的url
# 返回是否可以抓取(Ture、Flase)
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'urly'))

from urllib.request import urlopen
from urllib import request


req = request.Request(url='http://www.jianshu.com/robots.txt')
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; windows NT)')
urlx = 'http://www.jianshu.com/search?q=python&page=1&type=collections'
rq = RobotFileParser()
rq.parse(urlopen(req).read().decode('utf-8').split('\n'))
# can_fetch()两个参数，一个是User-agent，一个是要抓取的url
# 返回是否可以抓取(Ture、Flase)
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'urlx'))

''' 测试程序
rp = RobotFileParser()
rp.set_url('http://example.com/robots.txt')
rp.read()
url = 'http://example.com'
user_agent = 'GoodCrawler'
print(rp.can_fetch('*', url))#是否允许指定的用户代理访问网页
'''
