#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-23
# Introduce: 创建DataFrame
# Dependence
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

a = pd.DataFrame({'one': [1, 2, 3], 'two': [4, 5, 6]})
print("a:\n", a)

print("-----------------------")

b = pd.DataFrame({'one': [1, 2, 3], 'two': [4, 5, 6]}, index=['a', 'b', 'c'])
print("b:\n", b)

print("-----------------------")

c = pd.DataFrame(
    {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['b', 'a', 'c', 'd'])})
print("c:\n", c)
c.to_csv("./test.csv")

print("-----------------------")

d = pd.read_csv("https://dakastatic.oss-cn-beijing.aliyuncs.com/hanqun/instacart/products.csv")
print("d:\n", d)
