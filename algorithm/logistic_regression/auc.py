#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-01-26
# Introduce: AUC指标评价分类算法
# Dependence
from sklearn.metrics import roc_auc_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def model_auc_estimate():
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

    # 6.导入模型
    estimator = joblib.load("./预测癌症模型.m")
    # 7.预测
    y_predict = estimator.predict(x_test)
    # 由于y_test不满足roc_auc_score方法中对y_true的要求，故需要将y_test进行转换
    # 7.转换
    y_true = np.where(y_test > 3, 1, 0)
    # 8.计算AUC指标
    auc = roc_auc_score(y_true, y_predict)
    print(auc)


if __name__ == '__main__':
    model_auc_estimate()
