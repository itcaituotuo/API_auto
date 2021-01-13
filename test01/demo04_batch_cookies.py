# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2021/1/9 23:23

from test01.demo04_student_login import get_cookie
import os


def get_batch_cookies():
    """批量获取cookie"""
    # 获取cookie之前，先将cookies.csv文件内容清空
    # with open(r"D:\Desktop\Testman_Study\API_auto\file\cookies.csv", "w") as cookies_info:
    #     cookies_info.write("")
    # 或者将文件删除
    os.remove(r"D:\Desktop\Testman_Study\API_auto\file\cookies.csv")

    # 读取csv文件
    with open(r"D:\Desktop\Testman_Study\API_auto\file\register.csv", "r") as user_info:
        for user in user_info:
            # strip()去除前后空格，split(",")以","分隔转化为列表
            user_list = user.strip().split(",")
            # 输出列表
            print(user_list)
            # 调用获取单个cookies的方法，传入注册好的用户名和密码
            cookies = get_cookie(user_list[0], user_list[1])
            # 将cookie追加写入文件
            with open(r"D:\Desktop\Testman_Study\API_auto\file\cookies.csv", "a") as cookies_info:
                cookies_info.write(cookies + "\n")


# 调用方法
get_batch_cookies()
