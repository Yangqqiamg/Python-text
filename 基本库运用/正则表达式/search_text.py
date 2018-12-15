'''search()

扫描整个字符串，返回第一个匹配合适的选项
'''

import re
content = 'Extra stings Hello 12345 7 World_This is a text'
result = re.search('Hello.*?(\d+).*is',content)
print(result)
print(result.group())

