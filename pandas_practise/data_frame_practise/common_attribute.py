#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-23
# Introduce: DataFrame对象常用属性
# Dependence
import pandas as pd

df = pd.DataFrame(
    {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['b', 'a', 'c', 'd'])})
print("df:\n", df)
print("df.index:\n", df.index)
print("df.values:\n", df.values)
print("df.columns:\n", df.columns)
print("df.T:\n", df.T)
print("df.describe():\n", df.describe())
