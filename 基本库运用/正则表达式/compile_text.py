'''compile()

用于把正则表达式变成一个对象，可以多次调用
'''

import re

con1 = '2016-12-15 12:00'
con2 = '2017-12-15 05:20'
con3 = '2016-15-05 12:08'
mas = re.compile('\d{4}-\d{2}-\d{2}')
result1 = re.sub(mas, '', con1)
result2 = re.sub(mas, '', con2)
result3 = re.sub(mas, '', con3)
print(result1, result2, result3)