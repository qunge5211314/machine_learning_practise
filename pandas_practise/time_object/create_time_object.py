#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-24
# Introduce: 时间对象生成
# Dependence
import pandas as pd

print("获取从起始日到截止日的时间序列:\n", pd.date_range('2021-01-01', '2021-02-24'))

print("-----------------------------------------------------")

print("获取从起始日到期限为30个频率的时间序列:\n", pd.date_range('2021-01-01', periods=30))

print("-----------------------------------------------------")

# freq时间频率，默认为'D'，可选H(our),W(eek),B(usiness),S(emi-)M(month),(min)T(es),S(econds),A(year),....
print("获取从起始日到期限为30小时的时间序列::\n", pd.date_range('2021-01-01', periods=30, freq="H"))

print("-----------------------------------------------------")

print("获取从起始日到期限为30周的时间序列:\n", pd.date_range('2021-01-01', periods=30, freq="W-MON"))

print("-----------------------------------------------------")

print("获取从起始日到期限为30个工作日的时间序列:\n", pd.date_range('2021-01-01', periods=30, freq="B"))

print("-----------------------------------------------------")

# 以获取从起始日到期限为30个周一到周五的时间序列为例
df = pd.date_range('2021-01-01', periods=30, freq="B")
print("df:\n", df)
print("df[0]:\n", df[0])
print("df[0].to_pydatetime():\n", df[0].to_pydatetime())

print("-----------------------------------------------------")
