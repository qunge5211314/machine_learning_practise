#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-01-25
# Introduce: 正规方程求解线性回归系数
# Dependence
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

raw_all_data = load_boston()

if __name__ == '__main__':
    print(raw_all_data)