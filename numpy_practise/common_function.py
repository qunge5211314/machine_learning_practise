#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-19
# Introduce: 通用函数
# Dependence
import numpy as np

a = np.arange(9).reshape(3, 3)
print(a)
rg = np.random.default_rng(1)

print("-------------------------------")

print("10*np.sin(a):\n", 10 * np.sin(a))  # 对ndarray对象中每个元素求sin值
print("np.exp(a):\n", np.exp(a))  # 对ndarray对象中每个元素求以自然对数为底的指数函数
print("np.sqrt(a):\n", np.sqrt(a))  # 对ndarray对象中每个元素开根号
print("a.ravel():\n", a.ravel())  # 将ndarray对象转换成一维并返回，但不会改变ndarray对象

print("-------------------------------")

b = np.floor(10 * rg.random((3, 4)))  # 对ndarray对象中每个元素地板取整
print(b)
print("b.reshape(6,2):\n", b.reshape(6, 2))  # 按需求调整维度，但没有改变原ndarray对象，返回调整后的ndarray对象

print("b.T:\n", b.T)  # 矩阵的转置，不会改变原矩阵
print("b.resize(6,2):\n", b.resize(6, 2))  # 按需求调整维度，改变了原ndarray对象，返回None
print("b:\n", b)

print("-------------------------------")

c = np.arange(12).reshape(3, 4)
d = np.array([[0, 1],
              [1, 2]])
e = np.array([[2, 1],
              [3, 3]])
print("c:\n", c)
print("c[d]:\n", c[d])
print("c[d,e]:\n", c[d, e])

print("-------------------------------")
print("-------------------------------")
print("-------------------------------")
print("-------------------------------")
