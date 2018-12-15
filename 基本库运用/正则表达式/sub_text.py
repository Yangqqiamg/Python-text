'''sub():

用于替换文本
sub(old, new, 文本)
'''

import re
content = 'df84df6df4d6f87fd68'
result = re.sub('\d+', '1', content)
#result = re.sub('\d+', '', content) # 替换空字符就为删除
print(result)