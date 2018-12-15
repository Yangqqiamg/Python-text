import requests

'''文件上传：

使用POST请求，发送图片，用open 以二进制读模式打开文件
'''
file = {'file': open('favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=file)
# print(r.text)

'''Cookies:

'''
import requests
v = requests.get('https://www.baidu.com')
print(v.cookies)
#for key, value in v.cookies.items():
# print(key + "=" + value)

# 替换cookies
# 用cookies登陆
UA1 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_14)'
UA2 = 'AppleWebKit/537.36(KHTML, like Gecko)Chrome/52.0.2743.166 Safari/537.36'

headers = {
    'Cookies': 'q_c1=c16369a378c94006a0803e89903f1bf8|1540093444000|1540093444000; r_cap_id="MTJlNzJhNmMwNzVjNDdmZTkzYTM5YTkzMzU5YjZjN2I=|1540093444|ad4f081115bd656deb5fa8f0e8d6e58e2a809134"; cap_id="MTEyODg4YWZhNTYwNDUzNmFkY2NiMGIwODgzNWVjYjE=|1540093444|817bf9856250644b45cfe8a8dd5896bfb745140b"; l_cap_id="MzdjMGI4OTIwZWVhNGMwZGJjOGQxNTViYTBmOGZiMDM=|1540093444|a4b32fb933991b8db5d69c2bb09fda646cb94a18"; d_c0="ABAnEu5BZQ6PTpKYXmvLsHlyWqPatwu-9z8=|1540093446"; _zap=9e680902-7ec2-4545-91fb-2b3f420a5606; tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc; _xsrf=9q7BNCrTAkPHsZ5IQLLcvwuo2zJ0DSt7; capsion_ticket="2|1:0|10:1540345403|14:capsion_ticket|44:MjRlNjM1MmQ1NGM2NDU3MzhiMWYzYWUzZDU0MzYwN2U=|4e8cad2ba8780467b1a7a527bfe435025775801a889a76434fc6c89d8d75d62b"; z_c0="2|1:0|10:1540345446|4:z_c0|92:Mi4xSEhUaERBQUFBQUFBRUNjUzdrRmxEaVlBQUFCZ0FsVk5aaHk5WEFDTndBZ1F0VlJ6RS1MRlBUdndhblRfT1hzRDdn|bc392f582d02070f90d01695a23890346952c6e5823164ab8794a5611610f169"; tst=r; __gads=ID=ea0b91afe8cf8950:T=1540345451:S=ALNI_MZXSkjf6jMp4L4BPFrKpsymRKou2A',
    'Host': 'www.zhihu.com',
    'User-Agent': UA1+UA2,
}

b = requests.get('https://www.zhihu.com', headers=headers)
#print(b.text)


'''会话维持：

用POST和GET打开url时其实时不同会话，所以要用Session对象
'''
#一、
#设置测试网站的cookies为123456789
requests.get('http://httpbin.org/cookies/set/number/123456789')
#打开同一个网站
re = requests.get('http://httpbin.org/cookies')
#结果发现cookies不一样
#print(re.text)

#二、
#用Session(),可以模拟同一个会话不用担心cookies
s = requests.Session()
#设置测试网站的cookies为123456789
s.get('http://httpbin.org/cookies/set/number/123456789')
#打开同一个网站
r = s.get('http://httpbin.org/cookies')
#发现cookies一样
print(r.text)

'''SSL证书认证：

发送HTTP请求时会检查SSL证书，可通过参数verify来控制是否检测此证书
'''
from requests.packages import urllib3

urllib3.disable_warnings()# 设置忽略警告
#不加参数verify 会报错，表示证书错误
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

'''超时设置：

请求分两个阶段，即连接和读取，两者的时间总和就时timeout
'''
#超一秒没响应就异常
r = requests.get('https://www.taobao.com', timeout = 1)
#分别指定连接、读取和timeout时间
r = requests.get('https://www.taobao.com', timeout=(5,11))

'''身份认证

使用requests的HTTPBasicAuth类,传入一个元组
'''
from requests.auth import HTTPBasicAuth

#r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
#print(r.status_code)

#可简写：不需要导入HTTPBasicAuth类，当直接传入元组时会默认使用

# r = requests.get('http://localhost:5000', auth=('username', 'password'))
# print(r.status_code)

'''Preared Requests

不用post达到同样的结果
'''
from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'geremy',
}
UA1 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_14)'
UA2 = 'AppleWebKit/537.36(KHTML, like Gecko)Chrome/52.0.2743.166 Safari/537.36'

headers = {
    #'Cookies': 'q_c1=c16369a378c94006a0803e89903f1bf8|1540093444000|1540093444000; r_cap_id="MTJlNzJhNmMwNzVjNDdmZTkzYTM5YTkzMzU5YjZjN2I=|1540093444|ad4f081115bd656deb5fa8f0e8d6e58e2a809134"; cap_id="MTEyODg4YWZhNTYwNDUzNmFkY2NiMGIwODgzNWVjYjE=|1540093444|817bf9856250644b45cfe8a8dd5896bfb745140b"; l_cap_id="MzdjMGI4OTIwZWVhNGMwZGJjOGQxNTViYTBmOGZiMDM=|1540093444|a4b32fb933991b8db5d69c2bb09fda646cb94a18"; d_c0="ABAnEu5BZQ6PTpKYXmvLsHlyWqPatwu-9z8=|1540093446"; _zap=9e680902-7ec2-4545-91fb-2b3f420a5606; tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc; _xsrf=9q7BNCrTAkPHsZ5IQLLcvwuo2zJ0DSt7; capsion_ticket="2|1:0|10:1540345403|14:capsion_ticket|44:MjRlNjM1MmQ1NGM2NDU3MzhiMWYzYWUzZDU0MzYwN2U=|4e8cad2ba8780467b1a7a527bfe435025775801a889a76434fc6c89d8d75d62b"; z_c0="2|1:0|10:1540345446|4:z_c0|92:Mi4xSEhUaERBQUFBQUFBRUNjUzdrRmxEaVlBQUFCZ0FsVk5aaHk5WEFDTndBZ1F0VlJ6RS1MRlBUdndhblRfT1hzRDdn|bc392f582d02070f90d01695a23890346952c6e5823164ab8794a5611610f169"; tst=r; __gads=ID=ea0b91afe8cf8950:T=1540345451:S=ALNI_MZXSkjf6jMp4L4BPFrKpsymRKou2A',
    #'Host': 'www.zhihu.com',
    'User-Agent': UA1+UA2,
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)