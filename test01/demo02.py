# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2021/1/7 22:25

import requests

# # V部落查询栏目
# url_v_category = "http://182.92.178.83:8081/admin/category/all"
# # 设置请求头
# v_headers = {
#     "cookie": "studentUserName=ctt01; Hm_lvt_cd8218cd51f800ed2b73e5751cb3f4f9=1609742724,1609762306,1609841170,1609860946; adminUserName=admin; JSESSIONID=9D1FF19F333C5E25DBA60769E9F5248E"}
# result = requests.get(url_v_category, headers=v_headers)
# print(result.json())

# 文章列表
url_v_article = "http://182.92.178.83:8081/article/all"
v_headers = {
    "Cookie": "studentUserName=ctt01; Hm_lvt_cd8218cd51f800ed2b73e5751cb3f4f9=1609742724,1609762306,1609841170,1609860946; adminUserName=admin; JSESSIONID=9D1FF19F333C5E25DBA60769E9F5248E"}
article_params = {"state": 1,  # -1：全部文章 1：已发表 0：回收站 2：草稿箱
                  "page": 1,  # 显示第1页
                  "count": 6,  # 每页显示6条
                  "keywords": ""  # 包含的关键字
                  }
keywords = ["大橘猫", "跑男", "牙"]
for keyword in keywords:
    article_params["keywords"] = keyword
    # headers和params是不定长的，根据定义的字典传参
    # timeout超时，单位为秒
    # 通过设置超时时间，告诉requests在经过多久后停止等待响应
    result = requests.get(url_v_article, headers=v_headers, params=article_params, timeout=30)
    print(result.json())  # 响应结果以json的形式打印输出
    # print(result.url)  # 打印url地址
    # print(result.text)  # 以文本格式打印服务器响应的内容
    # print(result.status_code)  # 响应状态码
    # print(result.encoding)  # 编码格式
    # print(result.cookies)  # cookie
