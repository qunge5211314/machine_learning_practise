#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-24
# Introduce: 文件读取
# Dependence
import pandas as pd

# read_csv、read_table函数主要参数
# sep 指定分隔符，可以用正则表达式
# header=None 指定文件无列名
# name 指定列名
# index_col 指定某列作为索引
# skip_row 指定跳过某些行
# na_values 指定某些字符串表示缺失值
# parse_dates 指定某列是否被解析为日期，类型为布尔或列表

df0 = pd.read_csv("./601318.csv")
print("df0:\n", df0)

print("--------------------------------")

df1 = pd.read_csv("./601318.csv", index_col=0)
print("df1:\n", df1)

print("--------------------------------")

# 这两个等价
df2 = pd.read_csv("./601318.csv", index_col="date", parse_dates=True)
# df2 = pd.read_csv("./601318.csv", index_col="date", parse_dates=["date"])
print("df2:\n", df2)

print("--------------------------------")

df3 = pd.read_csv("./601318.csv", header=None, index_col=1, parse_dates=True, skiprows=[0])
print(df3)
