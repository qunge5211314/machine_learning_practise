#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date:
# Introduce:
# Dependence
# 波士顿房价预测
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import PolynomialFeatures
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
    # (4)多次幂处理特征
    polynomialFeatures = PolynomialFeatures(degree=3)
    x_train_poly = polynomialFeatures.fit_transform(x_train)
    x_test_poly = polynomialFeatures.fit_transform(x_test)
    print(x_train_poly)
    print(x_test_poly)
    # (5)预估器
    estimator = SGDRegressor(learning_rate="invscaling", eta0=0.03, alpha=0.01)
    estimator.fit(x_train_poly, y_train)
    joblib.dump(estimator, "../model_save_load/heihei.m")
    # (6)得出模型
    print("权重系数为:\n", estimator.coef_)
    print("偏置值为:\n", estimator.intercept_)
    # (7)评估模型
    y_predict = estimator.predict(x_test_poly)
    print("预测的房价:\n", y_predict)
    error = mean_squared_error(y_test, y_predict)
    print("梯度下降-均方误差为:\n", error)


if __name__ == '__main__':
    boston_housing_price_predict()