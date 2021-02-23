#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-23
# Introduce: Series对象缺失值处理
# Dependence
import pandas as pd

sr1 = pd.Series([12, 23, 34, 21], index=['c', 'a', 'd', 'e'])
sr2 = pd.Series([11, 20, 10, 20], index=['d', 'c', 'a', 'b'])

sr3 = sr1 + sr2
print("sr3:\n", sr3)
# 返回布尔数组，缺失值对应为True
print("sr3.isnull():\n", sr3.isnull())
# 返回布尔数组，缺失值对应为False
print("sr3.notnull():\n", sr3.notnull())
# 过滤缺失数据
print("sr3[sr3.notnull()]:\n", sr3[sr3.notnull()])
print("sr3.dropna():\n", sr3.dropna())  # 过滤掉值为nan的行
print("sr3.fillna(0):\n", sr3.fillna(0))  # 填充缺失数据

# 可以填充平均值
print("sr3.mean():\n", sr3.mean())
print("sr3.fillna(sr3.mean()):\n", sr3.fillna(sr3.mean()))  # 填充缺失数据
