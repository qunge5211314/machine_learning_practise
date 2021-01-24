#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-01-24
# Introduce: 低方差特征过滤
# Dependence
from sklearn.feature_selection import VarianceThreshold
from sklearn.datasets import load_iris

data = load_iris()

features_x = data.data


if __name__ == '__main__':
    varianceThreshold = VarianceThreshold(threshold=1.0)
    transform = varianceThreshold.fit_transform(features_x)
    print("raw_data:\n",features_x)
    print("shape:\n",features_x.shape)
    print("transform_data:\n",transform)
    print("shape:\n",transform.shape)