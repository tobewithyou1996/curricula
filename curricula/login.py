#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time
import student
import admin
import teacher


def login():
    """
    登陆模块
    :return:
    """
    login_status = 0
    user_name = input("请输入用户名：").strip()
    user_pwd = input("请输入密码：").strip()
    hash = hashlib.md5()
    hash.update(bytes(user_pwd, encoding='utf-8'))
    with open(r'../data/info.txt', 'r', encoding='utf-8') as f:
        ret = f.readline()
        while ret:
            ret = ret.strip('\n')
            ret = eval(ret)
            if user_name == ret['name']:
                if str(hash.hexdigest()) == ret['passwd']:
                    print("登陆成功")
                    # 登录写入日志
                    with open('../log/login.txt', mode='a', encoding='utf-8') as f1:
                        f1.write(
                            "{} 用户{}登录成功了\n".format(
                                time.strftime("%Y-%m-%d %X"),
                                user_name))
                    if ret['level'] == 1:
                        user1 = student.student(
                            ret['name'],
                            ret['passwd'],
                            ret['level'],
                            ret['subject'],
                            ret['class_grade'],
                            ret['lecturer'])
                        login_status = 1
                        return user1, login_status
                    elif ret['level'] == 2:
                        user1 = teacher.teacher(
                            ret['name'],
                            ret['passwd'],
                            ret['level'],
                            ret['subject'],
                            ret['class_grade'],
                            ret['lecturer'])
                        login_status = 1
                        return user1, login_status

                    else:
                        user1 = admin.admin(
                            ret['name'],
                            ret['passwd'],
                            ret['level'],
                            ret['subject'],
                            ret['class_grade'],
                            ret['lecturer'])
                        login_status = 1
                        return user1, login_status
            ret = f.readline()
    if login_status == 0:
        print('用户不存在或者密码错误')
        return [], 0
