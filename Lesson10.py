import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#1 
#list
l = pd.Series([1, 2, 3, 4, 5])
print(l)
#array
a = np.arange(5)
npser = pd.Series(a)
print(npser)
#dictionary
d = {'Arbuz': '3kg',
              'Beton': '77kg',
              'Shtanga': '100kg',
              'Gantelya': '10kg',
              'Girya': '50kg'}
pddict = pd.Series(d)
print(pddict)

#2

ser1 = pd.Series([1, 4, 5, 2, 9, 11])
ser2 = pd.Series([5, 2, 5, 7, 8, 9])
s_union = pd.Series(np.union1d(ser1, ser2))
s_intersect = pd.Series(np.intersect1d(ser1, ser2))
print(s_union[~s_union.isin(s_intersect)])

#3

data = 'абвгдеёжз'
len_sr = 40
sr = pd.Series(np.take(list(data), np.random.randint(len(data), size=len_sr)))
print(sr.value_counts())


#5

n = 1
sr = pd.Series([1, 3, 7, 14, 17, 21, 46, 12, 67, 98])
ans = sr.diff(periods=n)
print(ans)