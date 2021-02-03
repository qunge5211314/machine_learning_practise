#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2020-02-02
# Introduce: K-means算法模型评估
# Dependence
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.decomposition import PCA
import ssl
from sklearn.metrics import silhouette_score

ssl._create_default_https_context = ssl._create_unverified_context


def k_means_cluster():
    # 1.获取数据
    order_products = pd.read_csv(
        "https://dakastatic.oss-cn-beijing.aliyuncs.com/hanqun/instacart/order_products__prior.csv")
    products = pd.read_csv("https://dakastatic.oss-cn-beijing.aliyuncs.com/hanqun/instacart/products.csv")
    orders = pd.read_csv("https://dakastatic.oss-cn-beijing.aliyuncs.com/hanqun/instacart/orders.csv")
    aisles = pd.read_csv("https://dakastatic.oss-cn-beijing.aliyuncs.com/hanqun/instacart/aisles.csv")
    # 2.合并表
    tab1 = pd.merge(aisles, products, on=["aisle_id", "aisle_id"])
    tab2 = pd.merge(tab1, order_products, on=["product_id", "product_id"])
    tab3 = pd.merge(tab2, orders, on=["order_id", "order_id"])
    # 3.找到user_id和aisles之间的关系
    table = pd.crosstab(tab3["user_id"], tab3["aisle"])
    print(table)
    # 4.PCA降维
    #  1)实例化一个转换器类
    transfer = PCA(n_components=0.95)
    #  2)调用fit_transform
    data_new = transfer.fit_transform(table)
    # 5.实例化预估器
    estimator = KMeans(n_clusters=3)
    # 6.训练数据
    estimator.fit(data_new)
    y_predict = estimator.predict(data_new)
    print("预测结果为:\n", y_predict)
    score = silhouette_score(data_new, y_predict)
    print(score)


if __name__ == '__main__':
    k_means_cluster()
