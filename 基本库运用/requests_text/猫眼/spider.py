import json
import requests
from requests.exceptions import RequestException
import re
import time
import lxml



def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    #下列正则表达式的括号分别抓取排名、图片、名字、主演、上映时间、评分
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?month-wish.*?stonefont">(.*?)</span>.*?</p>'
                         + '.*?total-wish.*?stonefont">(.*?)</span>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'month-wish': item[5],
            'total-wish': item[6]
        }


def write_to_file(content):
    with open('result2.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    #最受期待榜
    url = 'http://maoyan.com/board/6?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

#main(0)

if __name__ == '__main__':
    for i in range(5):
        main(offset=i * 10)
        time.sleep(1)


