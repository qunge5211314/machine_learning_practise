#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-23
# Introduce: DataFrame索引和切片
# Dependence
import pandas as pd

df = pd.DataFrame(
    {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['b', 'a', 'c', 'd'])})

print("df['one']['a']:\n", df['one']['a'])
print("df.loc['a', 'one']:\n", df.loc['a', 'one'])
print("df.loc['a', :]:\n", df.loc['a', :])
print("df.loc[['a', 'c'], :]:\n", df.loc[['a', 'c'], :])