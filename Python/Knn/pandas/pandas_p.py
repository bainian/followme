from numpy import *
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt

s = Series([1, 3, 5, nan, 6, 8, 'abc'])
print(s)
s = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s.index.name)

data = {'state': ['a', 'c', 'b'], 'year': [200, 300, 400], 'pop': [2, 4, 5], 'day': [8, 7, 56]}
df = DataFrame(data)
print(df.index)
