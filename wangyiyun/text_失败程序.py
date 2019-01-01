import requests
from urllib.parse import urlencode
import os
from pyquery import PyQuery as pq
import re
from bs4 import BeautifulSoup

search_url = "https://music.163.com/#/search/m/?s="
download_url = "http://music.163.com/song/media/outer/url?id="

def get_html():
    UA1 = 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
    UA2 = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36'
    headers = {
        #'Host':'https://music.163.com',                            #指定请求资源的主机IP和端口号
        #'Referer': 'https://www.toutiao.com/search/?keyword=街拍',   #标识这个请求时从哪个网页发过来的
        'User-Agent': UA1+UA2,                          # 进行伪装，防止被禁止抓取
        #'X-Requestd-With': 'XMLHttpRequest',            #可以用来判断客户端的请求是Ajax请求还是其他请求
    }
    url =search_url + "稻香"
    #print(url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            #print(response.text)
            return response.text
    except:
        print('error!')

base_html = get_html()
print(type(base_html))
soup = BeautifulSoup(base_html, 'lxml')
print(type(soup))
# print(soup.prettify())
print(soup.body)
#pattern = re.compile('<div class="srchsongst">(*?)</div>', re.S)
# text = '<div class="srchsongst">'
# rq = base_html.get(text)
