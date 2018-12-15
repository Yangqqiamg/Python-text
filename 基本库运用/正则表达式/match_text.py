 ###############
# 正则表达式练习 #
 ###############

'''match()

向他传入要匹配的字符串以及正则表达式就可以测试是否成功匹配
group():输出匹配到的内容
span():输出匹配的范围
'''
import re
#一、简答匹配
content = 'hhh 7895 12 workd_This is a text'
print(len(content))
#'^hhh':开头匹配hhh
#\s: 匹配空白符
#\d{4}: 匹配4个数字
#\w{5}: 匹配5个字母、数字及下划线
result = re.match('^hhh\s\d{4}\s\d\d\s\w{5}', content)
print(result)
print(result.group())
print(result.span())

content1 = 'hhh 789512 workd_This is a text'
print(len(content))
#(): 括号内表达式也是一个组
#\d+: 匹配多个数字
result = re.match('^hhh\s(\d+)\s\w{5}', content1)
print(result)
print(result.group())
print(result.group(1))#输出括号内的结果，如果有下一个括号则写group(2)
print(result.span())


content2 = 'hhh 789512 workd_This is a text'
result = re.match('^hhh.*text$', content2)
#.(点)可以匹配任意字符（除了换行符）
#*(星)代表匹配前面的字符无限次
#符号 $ 匹配一行字符串的结尾
print(result)
print(result.group())
print(result.span())


content3 = 'hhh 789512 123 workd_This is a text'
#贪婪模式，‘.*’ 会尽可能的匹配多的字符
result = re.match('^hhh.*(\d+).*text$', content3)
#.(点)可以匹配任意字符（除了换行符）
#*(星)代表匹配前面的字符无限次
#符号 $ 匹配一行字符串的结尾
print(result)
print(result.group())
print(result.group(1))
print(result.span())

#加一个'?'符号变成 非贪婪模式，‘.*’ 会尽可能的匹配少的字符
result = re.match('^hhh.*?(\d+).*text$', content3)
#.(点)可以匹配任意字符（除了换行符）
#*(星)代表匹配前面的字符无限次
#符号 $ 匹配一行字符串的结尾
print(result)
print(result.group())
print(result.group(1))
print(result.span())



#re.S :使 .(点)的匹配包括换行符的所有字符
#更多查看书本 P145
content4 = '''hhh 789512 workd_This
 is a text'''

result = re.match('^hhh.*?(\d+).*text$', content4, re.S)
#.(点)可以匹配任意字符（除了换行符）
#*(星)代表匹配前面的字符无限次
#符号 $ 匹配一行字符串的结尾
print(result)
print(result.group())
print(result.group(1))


#如果需要匹配的字符串包括定义符号，哪就需要在符号前加上'\'
content5 = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content5)
print(result)