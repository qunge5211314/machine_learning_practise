#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-18
# Introduce: 创建数组
# Dependence
import numpy as np

a = np.array([1, 2, 3, 4, 5])  # []: 列表数据类型

print("np.pi:\n", np.pi)
print("np.e:\n", np.e)

print("-------------------------------------")

print("a:\n", a)
print(type(a))

print("-------------------------------------")

b = np.array((1, 2, 3, 4, 5))  # (): 元组数据类型
print("b:\n", b)
print(type(b))

print("-------------------------------------")

try:
    b = np.array(1, 2, 3, 4, 5)  # 报错
    print("b:\n", b)
except Exception as e:
    print(e)

print("-------------------------------------")

c = np.arange(5)  # 通过范围创建，可与range()函数相对比
print("c:\n", c)
print(type(c))

print("-------------------------------------")
# 创建多维数组
d = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])  # 创建3*3矩阵
print("d:\n", d)
print(type(d))
print(d[2, 2])

print("-------------------------------------")

e = np.arange(15)
f = np.arange(15).reshape(3, 5)
g = e.reshape(3, 5)
h = np.arange(3, 15, 0.2).reshape(6, 10)  # arange步长可以为小数
print("e:\n", e)
print("f:\n", f)
print("g:\n", g)
print("h:\n", h)

print("-------------------------------------")

print("f的维度是:", f.shape)  # ndarray.shape 维度大小
print("f的维度的数量是:", f.ndim)  # ndarray.ndim 维度的数量
print("f的元素数据类型是:", f.dtype.name)  # ndarray.dtype.name 元素的数据类型
print("f中每个元素的字节数(bytes)是:", f.itemsize)  # ndarray.itemsize 每个元素的字节数(bytes)

print("-------------------------------------")

i = np.zeros((3, 5))  # 3*5的0矩阵
print("i:\n", i)

j = np.zeros((2, 3, 4))  # 2*3*4的0
print("j:\n", j)

print("-------------------------------------")

k = np.ones((3, 4))  # 3*4的所有元素均为1的矩阵
print("k:\n", k)

print("-------------------------------------")

l = np.linspace(0, 2 * np.pi, 6)  # (x1, x2, N): 创建N个均匀间隔的数字，包括x1, x2
print("l:\n", l)

print("-------------------------------------")

m = np.random.default_rng()  # 实例化随机数字生成器，rng: random number generator
n = m.random((3, 4))
print("m:\n", m)
print("n:\n", n)

print("-------------------------------------")
