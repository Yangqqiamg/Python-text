'''抓取猫眼：

获取猫眼TOP100电影排行
'''

import json
import requests
from requests.exceptions import RequestException
import re
import time

#获取一页的源代码
def get_one_page(url):
    #尝试执行获取
    try:
        UA1 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_14)'
        UA2 = 'AppleWebKit/537.36(KHTML, like Gecko)Chrome/52.0.2743.166 Safari/537.36'
        headers = {
            'User-Agent': UA1+UA2,  # 进行伪装，防止被知乎禁止抓取
        }
        response = requests.get(url, headers=headers)
        if response.status_code ==200:
            return response.text
        return None
    #如果失败就不返回东西
    except RequestException:
        return None


############
#抓取信息函数
###########
def parse_one_page(html):
    #下列正则表达式的括号分别抓取排名、图片、名字、主演、上映时间、评分
    patten = re.compile(
        '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)'
        +'</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)'
        +'</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(patten, html)
    #生成字典
    for item in items:
        #迭代，生成多个字典,不会储存，当下次调用时才会显示
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5].strip() + item[6].strip()
        }
    #print()


'''########
写入文件函数
'''########
def write_to_file(content, name):
    #参数‘a’: 如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到
    #已有内容之后。如果该文件不存在，创建新文件进行写入。
    with open(name + '.txt', 'a', encoding='utf-8') as f:
        #将一个Python数据类型列表进行json格式的编码
        #（可以这么理解，json.dumps()函数是将字典转化为字符串）
        #print(tpye(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False)+'\n')




def main(offset):
    #前100榜单
    url = 'http://maoyan.com/board/4?offset=' + str(offset)

    html = get_one_page(url)
    #print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item,'123')

#判断是否在本文件执行函数
if __name__ == '__main__':
    for i in range(10): # i为0~9
        main(offset=i*10)
        time.sleep(1)

#main()