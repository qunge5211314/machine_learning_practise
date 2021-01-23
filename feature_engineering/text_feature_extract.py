#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-01-22
# Introduce: 文本特征值提取
# Dependence
from sklearn.feature_extraction.text import CountVectorizer
import jieba

english_data = ["Life is short, I like python, python is very good!",
                "Life is too long, I dislike python, python is very bad!"]

chinese_data = ["我爱北京天安门",
                "天安门 上 太阳 升"]


# 中文分词方法
def chinese_cut_word(text):
    return " ".join(list(jieba.cut(text)))


if __name__ == '__main__':
    # 第一步 创建转换器实例
    countVectorizer = CountVectorizer(stop_words=["is", "too"])
    # 第二步 调用转换器的fit_transform方法
    # 英文分词
    new_data1 = countVectorizer.fit_transform(english_data)
    print(new_data1.toarray())
    print(countVectorizer.get_feature_names())
    # 第二步 调用转换器的fit_transform方法
    # 中文分词
    new_data2 = countVectorizer.fit_transform(chinese_data)
    print(new_data2.toarray())
    print(countVectorizer.get_feature_names())
    # 利用jieba自动分词
    new_list = []
    for chinese_text in chinese_data:
        new_list.append(chinese_cut_word(chinese_text))
    print(new_list)
    new_data3 = countVectorizer.fit_transform(new_list)
    print(new_data3.toarray())
    print(countVectorizer.get_feature_names())
