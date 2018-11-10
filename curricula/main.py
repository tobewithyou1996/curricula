#!/usr/bin/env python
# -*- coding: utf-8 -*-

from login import login

while True:
    ret, login_status = login()
    if login_status == 1:
        if ret.level == 0:
            print("你是管理员，你已经成功登陆了")
            while True:
                num = input('''
        1、创建课程
        2、创建学生学生账号
        3、查看所有课程
        4、查看所有学生
        5、查看所有学生的选课情况
        6、创建讲师
        7、为讲师指定班级
        8、创建班级
        9、为学生指定班级
        10、退出程序
        请输入你的选择：''')
                if num.strip() == '1':
                    ret.add_subject()
                elif num.strip() == '2':
                    ret.add_account()
                elif num.strip() == '3':
                    ret.show_total_subject()
                elif num.strip() == '4':
                    ret.show_all_student()
                elif num.strip() == '5':
                    ret.show_all_stu_sub()
                elif num.strip() == '6':
                    ret.create_lecturer()
                elif num.strip() == '7':
                    ret.lecturer_class()
                elif num.strip() == '8':
                    ret.create_class()
                elif num.strip() == '9':
                    ret.student_class()
                else:
                    ret.quit_procedure()
        elif ret.level == 2:
            print("你是讲师，你已经成功登陆了")
            while True:
                num = input('''
        1、查看所有课程
        2、查看所教班级
        3、查看班级中的学生
        4、退出程序
        请输入你的选择: ''')
                if num.strip() == '1':
                    ret.show_total_subject()
                elif num.strip() == '2':
                    ret.show_class()
                elif num.strip() == '3':
                    ret.show_student()
                else:
                    ret.quit_procedure()

        else:
            print("你是学生，你已经成功登陆了")
            while True:
                num = input('''
        1、查看所有课程
        2、选择课程
        3、查看所选课程
        4、退出程序
        请输入你的选择：''')
                if num.strip() == '1':
                    ret.show_total_subject()
                elif num.strip() == '2':
                    ret.choose_subject()
                elif num.strip() == '3':
                    ret.show_subject()
                else:
                    ret.quit_procedure()
