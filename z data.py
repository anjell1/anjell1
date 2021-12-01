import pandas as pd

a = pd.read_csv('C:/Users/HHP/Desktop/ss.csv')
print(a)

z = a.iloc[::2]
print(z)

import csv

# open the file in the write mode
#f = open('C:/Users/HHP/Desktop/qq.csv', 'w')
z.to_csv('C:/Users/HHP/Desktop/fati.csv')