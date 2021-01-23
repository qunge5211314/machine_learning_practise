#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-01-23
# Introduce: 数据预处理之归一化
# Dependence
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_iris

data = load_iris()

features_x = data.data

if __name__ == '__main__':
    minMaxScaler = MinMaxScaler(feature_range=(-1, 1))
    result = minMaxScaler.fit_transform(features_x)
    print(result)
