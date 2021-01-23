#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-01-22
# Introduce: 机器学习scikit-learn框架基础部分
# Dependence
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


# 加载scikit-learn内置数据集
def load_dataset():
    # load和fetch返回的数据类型sklearn.datasets.Bunch(继承字典的类)
    return load_iris()


def dataset_info(dataset):
    # 数据集整体信息
    print(dataset)
    # data 特征数据数组矩阵。numpy.ndarray
    print(dataset.data)
    print(type(dataset.data))
    # target 结果数据数组向量。 numpy.ndarray
    print(dataset.target)
    print(type(dataset.target))
    # DESCR 数据描述。 str
    print(dataset.DESCR)
    print(type(dataset.DESCR))
    # feature_names: 特征名数组。 list
    print(dataset.feature_names)
    print(type(dataset.feature_names))
    # target_names: 结果集名数组。 numpy.ndarray
    print(dataset.target_names)
    print(type(dataset.target_names))


# 数据集划分
# input_param: *arrays list/np.array 矩阵
#              test_size float 测试集占比 建议占比20%～30%
#              random_state 随机数种子，不同的种子会造成不同的随机采样结果。相同的种子随机采样结果相同
# return: 训练集特征值x_train, 测试集特征值x_test, 训练集目标值y_train, 测试集目标值y_test
def split_data(dataset):
    return train_test_split(dataset.data, dataset.target, test_size=0.2)


if __name__ == '__main__':
    dataset = load_dataset()
    dataset_info(dataset)
    x_train, x_test, y_train, y_test = split_data(dataset)
    print(x_train)
    print(x_train.shape)
    print(x_test)
    print(x_test.shape)
    print(y_train)
    print(y_train.shape)
    print(y_test)
    print(y_test.shape)