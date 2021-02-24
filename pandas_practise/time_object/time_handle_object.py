#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-24
# Introduce: 时间处理对象
# Dependence
import datetime
from dateutil import parser
import pandas as pd

# 传统时间解析方式：
print("python内置datetime模块时间字符串解析方式:\n", datetime.datetime.strptime("2021-02-24", "%Y-%m-%d"))

print("------------------------------")

# pandas内置时间解析方式
print("pandas内置时间解析方式:\n", parser.parse("02/24/2021"))
print("pandas内置时间解析方式:\n", parser.parse("2021-FEB-24"))

print("------------------------------")

# pandas可批量转换时间对象
print("pandas批量转换时间对象:\n", pd.to_datetime(["02/24/2021", "2021-FEB-24"]))

print("------------------------------")
