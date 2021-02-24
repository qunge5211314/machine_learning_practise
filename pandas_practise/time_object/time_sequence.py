#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-24
# Introduce: 时间序列
# Dependence
import pandas as pd
import numpy as np

sr = pd.Series(np.arange(100), index=pd.date_range('2021-01-01', periods=100, freq='B'))
print("sr:\n", sr)

print("------------------------------")

print("获取三月份数据:\n", sr['2021-03'])

print("------------------------------")

print("获取指定日期数据:\n", sr['2021-03-25'])

print("------------------------------")

print("获取某一时段数据:\n", sr['2021-01': '2021-4-1'])

print("------------------------------")

print("sr.resample('M').sum()", sr.resample('M').sum())
print("sr.resample('M').mean()", sr.resample('M').mean())
print("sr.resample('M').std()", sr.resample('M').std())

print("------------------------------")

print(sr.truncate(before='2021-02-01'))