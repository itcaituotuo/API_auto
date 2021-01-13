# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2021/1/9 23:26

import requests


def get_cookie(username, password):
    """通过考试系统学生登录获取单个cookie"""

    url_login = "http://182.92.178.83:8088/api/user/login"
    payload = {"userName": username, "password": password, "remember": False}
    result = requests.post(url_login, json=payload)
    # result_json = result.json()
    # print(result_json)

    # 获取RequestsCookieJar
    result_cookie = result.cookies
    # print(result_cookie, type(result_cookie))  # RequestsCookieJar
    # 将RequestsCookieJar转化为字典格式
    result_cookie_dic = requests.utils.dict_from_cookiejar(result_cookie)
    # print(result_cookie_dic)  # {'SESSION': 'YzFkM2IzN2QtZWY1OC00Nzc4LTgyOWYtNjg5OGRiZDZlM2E4'}

    # 获取SESSION
    final_cookie = "SESSION=" + result_cookie_dic["SESSION"]  # SESSION=Mzc2...
    return final_cookie
