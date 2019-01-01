from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from pyquery import PyQuery
browser = webdriver.Chrome()    #初始化，并赋值给对象
# try:
#     browser.get('https://music.163.com/')   #访问url
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)      #输出源代码
# finally:
#     browser.close()

browser.get('https://music.163.com/#/search')   #访问url

# 使用css选择器 获取 class值为service-bd 的代码里的所有 li 节点
# 参考链接：http://www.w3school.com.cn/cssref/css_selectors.asp
# ############################################################

# input = browser.find_elements_by_css_selector('.service-bd li')
# input = browser.find_elements_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div/ul/li')
# print(input)
# print(browser.page_source) /html/body/div[4]/div[1]/div[1]/div[1]/div
time.sleep(1)
browser.switch_to.frame('g_iframe')
input = browser.find_element_by_xpath('//*[@id="m-search-input"]')

input.send_keys('安静 ')       #输入文字
time.sleep(1)
input.send_keys(Keys.ENTER)
time.sleep(1)
# next = browser.find_element_by_css_selector('.srchsongst')
# browser.switch_to.frame('g_iframe')
text = browser.page_source
# print(text)
res = PyQuery(text)
first = res('.srchsongst .item .td .hd ')
# next = first('a:first-child')
sec = first.children()
song_id = sec.attr('data-res-id')

browser.close()