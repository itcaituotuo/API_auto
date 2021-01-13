# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2021/1/7 21:48

import requests

url_toutiao = "https://www.ixigua.com/tlb/comment/article/v5/tab_comments/?tab_index=0&count=10&group_id=6914830518563373581&item_id=6914830518563373581&aid=1768"
# 方式一：
# result_toutiao = requests.get(url_toutiao)

# 方式二：
result_toutiao = requests.get(url=url_toutiao)

# 方式三：
# result_toutiao = requests.get(
#     "https://www.ixigua.com/tlb/comment/article/v5/tab_comments/?tab_index=0&count=1&group_id=6914830518563373581&item_id=6914830518563373581&aid=1768")

# print(result_toutiao.json())
# print(type(result_toutiao.json()))  # <class 'dict'>
result = result_toutiao.json()
print(result)
expect_result = "华晨金杯汽车花朵朵"
actual_result = result["data"][0]["comment"]["user_name"]
print(actual_result)
if expect_result == actual_result:
    print("pass!")
else:
    print("failed!")
