'''findall()

匹配符合的所哟内容,返回列表
'''


import re
content = '''Extra stings Hello 123457 World_This is a text
            Extra stings Hello 1238637 World_This is a text'''
results = re.findall('Hello.*?(\d+).*is',content)
print(results)
for result in results:
    print(result)
