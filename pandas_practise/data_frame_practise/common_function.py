#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-23
# Introduce: pandas常用函数
# Dependence
import pandas as pd
import numpy as np

df = pd.DataFrame({'two': [1, 2, 3, 4],
                   'one': [np.nan, 5, 6, 7]},
                  index=['c', 'd', 'b', 'a'])
print("df:\n", df)

print("---------------------------")

# 默认按列求均值
print("df.mean():\n", df.mean())

print("---------------------------")

# 按行求均值
print("df.mean(axis=1):\n", df.mean(axis=1))

print("---------------------------")

# 默认按列求和
print("df.sum():\n", df.sum())

print("---------------------------")

# 按行求和
print("df.sum(axis=1):\n", df.sum(axis=1))

print("---------------------------")

# 按值排序，注意有nan的数据默认永远排在后面
print("df.sort_values(by='two', ascending=False):\n", df.sort_values(by='two', ascending=False, axis=0))

print("---------------------------")

# 按key排序
print("df.sort_index(ascending=False, axis=0):\n", df.sort_index(ascending=True, axis=0))

print("---------------------------")
