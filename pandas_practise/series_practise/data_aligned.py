#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-23
# Introduce: Series数据对齐
# Dependence
import pandas as pd

sr1 = pd.Series([12, 23, 34], index=['c', 'a', 'd'])
sr2 = pd.Series([11, 20, 10, 5], index=['d', 'c', 'a', 'b'])
print("sr1+sr2=:\n", sr1 + sr2)
print("sr1.add(sr2, fill_value=0):\n", sr1.add(sr2, fill_value=0))
