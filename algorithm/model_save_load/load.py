#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-01-25
# Introduce: 模型加载
# Dependence
import joblib
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def boston_housing_price_predict():
    # (1)获取数据
    raw_all_data = load_boston()
    # (2)划分数据集
    x_train, x_test, y_train, y_test = train_test_split(raw_all_data.data, raw_all_data.target)
    # (3)标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)
    # (4)加载模型
    estimator = joblib.load("./heihei.m")
    # (5)得出模型
    print("权重系数为:\n", estimator.coef_)
    print("偏置值为:\n", estimator.intercept_)
    # (6)评估模型
    y_predict = estimator.predict(x_test)
    print("预测的房价:\n", y_predict)
    error = mean_squared_error(y_test, y_predict)
    print("梯度下降-均方误差为:\n", error)


if __name__ == '__main__':
    boston_housing_price_predict()
