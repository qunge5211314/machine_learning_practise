#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-01-22
# Introduce: 字典特征提取示例
# Dependence
from sklearn.feature_extraction import DictVectorizer

data = [{"city": "北京", "temperature": 5},
        {"city": "上海", "temperature": 13},
        {"city": "广州", "temperature": 24},
        {"city": "深圳", "temperature": 26}]


if __name__ == '__main__':
    # 第一步 实例化转换器
    dictVectorizer = DictVectorizer(sparse=False)
    # 第二步 调用转换器的fit_transform方法
    new_data = dictVectorizer.fit_transform(data)
    # 输出值包含哑变量
    print(new_data)
    print(dictVectorizer.get_feature_names())
    # 转换器inverse_transform方法输入array数组或者sparse矩阵，返回：转换之前数据格式
    print(dictVectorizer.inverse_transform(new_data))
