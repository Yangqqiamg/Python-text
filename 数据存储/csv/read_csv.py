import csv

with open('dis.csv', 'r',encoding='utf-8') as text:
    str = csv.reader(text)
    for roe in str:
        print(roe)

#使用pandas
import pandas as pd
df = pd.read_csv('dis.csv')
print(df)