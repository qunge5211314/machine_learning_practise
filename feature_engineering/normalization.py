#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-01-23
# Introduce: 特征数据预处理之标准化
# Dependence
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

data = load_iris()

features_x = data.data

if __name__ == '__main__':
    standardScaler = StandardScaler()
    result = standardScaler.fit_transform(features_x)
    print(result)