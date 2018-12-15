import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
# 替换cookies
# 用cookies登陆
UA1 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_14)'
UA2 = 'AppleWebKit/537.36(KHTML, like Gecko)Chrome/52.0.2743.166 Safari/537.36'

headers = {
    'Cookies': 'q_c1=c16369a378c94006a0803e89903f1bf8|1540093444000|1540093444000; r_cap_id="MTJlNzJhNmMwNzVjNDdmZTkzYTM5YTkzMzU5YjZjN2I=|1540093444|ad4f081115bd656deb5fa8f0e8d6e58e2a809134"; cap_id="MTEyODg4YWZhNTYwNDUzNmFkY2NiMGIwODgzNWVjYjE=|1540093444|817bf9856250644b45cfe8a8dd5896bfb745140b"; l_cap_id="MzdjMGI4OTIwZWVhNGMwZGJjOGQxNTViYTBmOGZiMDM=|1540093444|a4b32fb933991b8db5d69c2bb09fda646cb94a18"; d_c0="ABAnEu5BZQ6PTpKYXmvLsHlyWqPatwu-9z8=|1540093446"; _zap=9e680902-7ec2-4545-91fb-2b3f420a5606; tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc; _xsrf=9q7BNCrTAkPHsZ5IQLLcvwuo2zJ0DSt7; capsion_ticket="2|1:0|10:1540345403|14:capsion_ticket|44:MjRlNjM1MmQ1NGM2NDU3MzhiMWYzYWUzZDU0MzYwN2U=|4e8cad2ba8780467b1a7a527bfe435025775801a889a76434fc6c89d8d75d62b"; z_c0="2|1:0|10:1540345446|4:z_c0|92:Mi4xSEhUaERBQUFBQUFBRUNjUzdrRmxEaVlBQUFCZ0FsVk5aaHk5WEFDTndBZ1F0VlJ6RS1MRlBUdndhblRfT1hzRDdn|bc392f582d02070f90d01695a23890346952c6e5823164ab8794a5611610f169"; tst=r; __gads=ID=ea0b91afe8cf8950:T=1540345451:S=ALNI_MZXSkjf6jMp4L4BPFrKpsymRKou2A',
    'Host': 'www.zhihu.com',
    'User-Agent': UA1+UA2,
}

#如果你想取文本，可以通过r.text。
#如果想取图片，文件，则可以通过r.content。
html = requests.get(url, headers=headers).text
doc = pq(html)
# 进行pyquery解析（里面放的是css选择器参数）对class里有两个参数来进行解析
items = doc('.explore-tab .explore-feed').items()
for item in items:
    question = item.find("h2").text()
    author = item.find('.author-link-line').text()
    # 提取里面的回复的内容，这里注意一下，在内容的上面有一个textarea被 hidden了
    answer = pq(item.find('.content').html()).text()
    #str转bytes叫encode，bytes转str叫decode
    with open('text.txt','a', encoding='utf-8') as file:
        #分别写入 jion()里的对象，并以换行符分开
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '='*50 + '\n')