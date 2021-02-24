#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-24
# Introduce: DataFrame对象缺失值处理
# Dependence
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
                    'two': pd.Series([1, 2, 3, 4], index=['b', 'a', 'c', 'd'])})
print("-----------------------")

print("df1:\n", df1)

print("-----------------------")

print("df1.fillna(0):\n", df1.fillna(0))

print("-----------------------")

print("df1.dropna():\n", df1.dropna())

print("-----------------------")

df1.loc["d", "two"] = np.nan
df1.loc["c", "two"] = np.nan
print("df1:\n", df1)

print("-----------------------")

print("df1.dropna(how='all'):\n", df1.dropna(how='all'))

print("-----------------------")

df2 = pd.DataFrame({'two': [1, 2, 3, 4],
                    'one': [np.nan, 5, 6, 7]},
                   index=['c', 'd', 'b', 'a'])
print("df2:\n", df2)

print("-----------------------")

print("df2.dropna(axis=1):\n", df2.dropna(axis=1))

print("-----------------------")
