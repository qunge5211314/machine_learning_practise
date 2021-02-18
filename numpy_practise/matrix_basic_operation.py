#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-18
# Introduce: 矩阵基础运算
# Dependence
import numpy as np

a = np.array([20, 30, 40, 50])
b = np.array([0, 1, 2, 3])
print("a:\n", a)
print("b:\n", b)

print("-------------------------------")

print("a+2:\n", a + 2)  # 与数字相加，结果为其中每一个元素与该数字相加
print("a-2:\n", a - 2)  # 与数字相减，结果为其中每一个元素与该数字相减
print("a*2:\n", a * 2)  # 与数字相乘，结果为其中每一个元素与该数字相乘
print("a/2:\n", a / 2)  # 与数字相除，结果为其中每一个元素与该数字相除

print("-------------------------------")

print("a+b:\n", a + b)  # 两个ndarray相加，结果为对应元素相加，注意，两个ndarray对象需要具有相同的维度
print("a-b:\n", a - b)  # 两个ndarray相减，结果为对应元素相减，注意，两个ndarray对象需要具有相同的维度
print("a*b:\n", a * b)  # 两个ndarray相乘，结果为对应元素相乘，注意，两个ndarray对象需要具有相同的维度
print("a/b:\n", a / b)  # 两个ndarray相除，结果为对应元素相除，注意，两个ndarray对象需要具有相同的维度

print("-------------------------------")

print("a@b:\n", a @ b)  # 两个ndarray点乘，结果为对应元素相乘后求和，注意，两个ndarray对象需要具有相同的维度
print("a.dot(b):\n", a.dot(b))  # 同a@b

print("-------------------------------")

print(a == 35)  # ndarray对象中每个元素与实数做比较，结果为新的ndarray对象，与原ndarray对象维度一致，但每个元素为布尔值

print("-------------------------------")


