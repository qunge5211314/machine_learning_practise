#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-01-25
# Introduce: 逻辑回归算法案例
# Dependence
import pandas as pd
import numpy as np
import ssl
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context


def breast_cancer_predict():
    # 1. 获取数据
    data_path = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
    column_names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                    'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                    'Normal Nucleoli', 'Mitoses', 'Class']

    raw_all_data = pd.read_csv(data_path, names=column_names)
    # 2. 缺失值处理
    # (1) 替换 ？-> np.NAN
    # (2) 删除缺失样本
    replaced_data = raw_all_data.replace(to_replace="?", value=np.nan)
    replaced_data.dropna(inplace=True)

    # 3.筛选特征值和目标值
    x = replaced_data.iloc[:, 1: -1]
    y = replaced_data["Class"]

    # 4.划分数据集
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    # 5.特征工程--标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    # 6.创建模型
    estimator = LogisticRegression()
    estimator.fit(x_train, y_train)

    # 7.逻辑回归的模型参数：回归系数和偏置
    print("模型参数-回归系数:\n", estimator.coef_)
    print("模型参数-偏置:\n", estimator.intercept_)

    # 8.模型评估
    # 方法1。直接比对真实值和预估值
    y_predict = estimator.predict(x_test)
    print()


if __name__ == '__main__':
    breast_cancer_predict()
