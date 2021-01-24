#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-01-24
# Introduce: 主成分分析练习
# Dependence
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

data = load_iris()

features_x = data.data

if __name__ == '__main__':
    pca = PCA(n_components=2)
    result = pca.fit_transform(features_x)
    print(features_x)
    print(features_x.shape)
    print(result)
    print(result.shape)
