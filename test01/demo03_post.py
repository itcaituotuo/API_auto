# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2021/1/9 22:51

import requests

url_v_login = "http://182.92.178.83:8081/login"
# 定义参数，字典格式
payload = {'username': 'sang', 'password': '123'}
# Content-Type: application/json --> json
# Content-Type: application/x-www-form-urlencoded --> data
result = requests.post(url_v_login, data=payload)
# 将返回结果转为json格式
result_json = result.json()
print(result_json)  # {'status': 'success', 'msg': '登录成功'}
# 获取RequestsCookieJar
result_cookie = result.cookies
print(result_cookie, type(result_cookie))  # RequestsCookieJar
# 将RequestsCookieJar转化为字典格式
result_cookie_dic = requests.utils.dict_from_cookiejar(result_cookie)
print(result_cookie_dic)  # {'JSESSIONID': 'D042C5FE4CFF337806D545B0001E7197'}
# 获取SESSION
final_cookie = "JSESSIONID=" + result_cookie_dic["JSESSIONID"]  # SJSESSIONID=D042C5FE4CFF337806D545B0001E7197
print(final_cookie)
