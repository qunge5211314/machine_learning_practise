#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-23
# Introduce: Series对象整数索引
# Dependence
import pandas as pd
import numpy as np

a = pd.Series(np.arange(20))
print("a:\n", a)
b = a[9:].copy()
print("b:\n", b)
print("b[9]:\n", b[9])
print("b.loc[9]:\n", b.loc[9])
print("b.iloc[9]:\n", b.iloc[9])
