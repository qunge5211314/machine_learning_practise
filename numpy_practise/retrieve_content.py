#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-19
# Introduce: 检索内容
# Dependence
import numpy as np

# 向量
a = np.array([20, 30, 40, 50])

print("-------------------------------")

print("a[2]:\n", a[2])  # 0，1，2通过位置检索到内容
print("a[0:2]:\n", a[0:2])  # 切片
print("a[2::]:\n", a[1::2])
print("a[0:6]:\n", a[0:6])  # 溢出情况下返回完整向量

print("-------------------------------")

print("a的维度为:\n", a.shape)

print("-------------------------------")

# 矩阵
b = np.arange(16).reshape(4, 4)
print("b:\n", b)

print("-------------------------------")

print("b[2]:\n", b[2])  # 一行数据
print("b[0:3]:\n", b[0:3])  # 切片，连续几行数据
print("b[0:3][1]:\n", b[0:3][1])  # 切片后取索引为1的一行数据
print("b[0:3][1][2]:\n", b[0:3][1][2])  # 切片后取索引为1的一行数据中的索引为2的元素

print("-------------------------------")

# 遍历每一行
i = 0
for row in b:
    i += 1
    print("第{}行:".format(i), row)

print("-------------------------------")

# 遍历每一个元素
i = 0
for element in b.flat:
    i += 1
    print("第{}个元素:".format(i), element)

print("-------------------------------")
