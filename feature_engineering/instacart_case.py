#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-02-02
# Introduce: instacart案例
# Dependence
import pandas as pd
from sklearn.decomposition import PCA
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def instacart_case():
    # 1.获取数据
    order_products = pd.read_csv(
        "https://dakastatic.oss-cn-beijing.aliyuncs.com/hanqun/instacart/order_products__prior.csv")
    products = pd.read_csv("https://dakastatic.oss-cn-beijing.aliyuncs.com/hanqun/instacart/products.csv")
    orders = pd.read_csv("https://dakastatic.oss-cn-beijing.aliyuncs.com/hanqun/instacart/orders.csv")
    aisles = pd.read_csv("https://dakastatic.oss-cn-beijing.aliyuncs.com/hanqun/instacart/aisles.csv")
    # 2.合并表
    # order_products__prior.csv：订单与商品信息
    # 字段：order_id, product_id, add_to_cart_order, reordered

    # products.csv：商品信息
    # 字段：product_id, product_name, aisle_id, department_id

    # orders.csv：用户的订单信息
    # 字段：order_id, user_id, eval_set, order_number,….

    # aisles.csv：商品所属具体物品类别
    # 字段： aisle_id, aisle

    # 合并aisles和products
    tab1 = pd.merge(aisles, products, on=["aisle_id", "aisle_id"])
    tab2 = pd.merge(tab1, order_products, on=["product_id", "product_id"])
    tab3 = pd.merge(tab2, orders, on=["order_id", "order_id"])
    # print(tab3)
    # 3.找到user_id和aisles之间的关系
    table = pd.crosstab(tab3["user_id"], tab3["aisle"])
    print(table.shape)
    # 4.PCA降维
    # 1)实例化一个转换器类
    transfer = PCA(n_components=0.95)
    # 2)调用fit_transform
    data_new = transfer.fit_transform(table)
    print(data_new.shape)


if __name__ == '__main__':
    instacart_case()
