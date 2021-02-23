#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-23
# Introduce: series简介
# Dependence
import pandas as pd
import numpy as np

# Series支持array的特性
a = pd.Series([2, 3, 4, 5])

print("a:\n", a)

print("-----------------------------------------")

b = pd.Series([2, 3, 4, 5], index=['a', 'b', 'c', 'd'])
print("b:\n", b)
print("b[1]:\n", b[0])

print("-----------------------------------------")

c = pd.Series(np.arange(-5, 5))
print("c:\n", c)
print("c+c:\n", c + c)
print("c[0:2]:\n", c[0:2])
print("np.abs(c):\n", np.abs(c))

print("-----------------------------------------")

# Series支持字典的特性
d = pd.Series({'a': 1, 'b': 2})
print("d:\n", d)
print("d['b']:\n", d['b'])
print("d.index:\n", d.index)
print("d.index[0]:\n", d.index[0])
print("d.values:\n", d.values)

print("-----------------------------------------")

e = pd.Series(np.arange(4, 5, 0.2), index=['a', 'b', 'c', 'd', 'e'])
print("e:\n", e)
print("e[['a','c']]:\n", e[['a', 'c']])
print("e[['a':'c']]:\n", e['a':'c'])


