#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-24
# Introduce: DataFrame对象数据对齐
# Dependence
import pandas as pd

# DataFrame对象在运算时，同样会进行数据对齐，其行索引和列索引分别对齐
df1 = pd.DataFrame({'two': [1, 2, 3, 4],
                    'one': [4, 5, 6, 7]},
                   index=['c', 'd', 'b', 'a'])

df2 = pd.DataFrame({'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
                    'two': pd.Series([1, 2, 3, 4], index=['b', 'a', 'c', 'd'])})
print("-------------------------------")

print("df1:\n", df1)

print("-------------------------------")

print("df2:\n", df2)

print("-------------------------------")

print("df1+df2:\n", df1 + df2)

print("-------------------------------")
