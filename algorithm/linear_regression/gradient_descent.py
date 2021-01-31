#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-01-25
# Introduce: 梯度下降法
# Dependence
# 波士顿房价预测
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
import joblib


def boston_housing_price_predict():
    # (1)获取数据
    raw_all_data = load_boston()
    # (2)划分数据集
    x_train, x_test, y_train, y_test = train_test_split(raw_all_data.data, raw_all_data.target)
    # (3)标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)
    # (4)预估器
    estimator = SGDRegressor(learning_rate="invscaling", eta0=0.03, alpha=0.01)
    estimator.fit(x_train, y_train)
    # joblib.dump(estimator, "../model_save_load/heihei.m")
    # (5)得出模型
    print("权重系数为:\n", estimator.coef_)
    print("偏置值为:\n", estimator.intercept_)
    # (6)评估模型
    y_test_predict = estimator.predict(x_test)
    print("预测的房价:\n", y_test_predict)
    test_error = mean_squared_error(y_test, y_test_predict)
    print("梯度下降-测试集均方误差为:\n", test_error)
    y_train_predict = estimator.predict(x_train)
    train_error = mean_squared_error(y_train, y_train_predict)
    print("梯度下降-训练集均方误差为:\n", train_error)


if __name__ == '__main__':
    boston_housing_price_predict()