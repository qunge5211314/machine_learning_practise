#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-01-25
# Introduce: 训练模型存储
# Dependence
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
    estimator = SGDRegressor(learning_rate="invscaling", eta0=0.01, alpha=0.3)
    estimator.fit(x_train, y_train)
    # (5)得出模型
    print("权重系数为:\n", estimator.coef_)
    print("偏置值为:\n", estimator.intercept_)
    # (6)评估模型
    y_predict = estimator.predict(x_test)
    print("预测的房价:\n", y_predict)
    error = mean_squared_error(y_test, y_predict)
    print("梯度下降-均方误差为:\n", error)
    # (7)保存模型
    joblib.dump(estimator, "./heihei.m")


if __name__ == '__main__':
    boston_housing_price_predict()
