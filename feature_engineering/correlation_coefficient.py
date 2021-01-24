#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date:
# Introduce:
# Dependence
from sklearn.datasets import load_iris
from scipy.stats import pearsonr

data = load_iris(as_frame=True)
data = data.frame

feature_x1 = data.get("sepal length (cm)")
feature_x2 = data.get("sepal width (cm)")

if __name__ == '__main__':
    print(feature_x1)
    print(feature_x2)
    p_value = pearsonr(feature_x1, feature_x2)
    print(p_value)