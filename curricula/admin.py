#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from student import student
from teacher import teacher


class admin(student):
    def add_subject(self):
        """
        创建课程
        """
        #  是否写入文件标准位
        write_flag = False
        sj = input("请选择你想要创建的课程：").strip()
        # 判断课程是否已经存在，不存在则可以进行添加
        with open('../data/info.txt', 'r', encoding='utf-8') as f:
            ret = f.readline()
            while ret:
                ret = ret.strip('\n')
                ret = eval(ret)
                if ret['level'] == 0:
                    if sj in ret['subject']:
                        print("课程已经存在，请不要重复添加")
                        break
                    else:
                        write_flag = True
                ret = f.readline()
        # write_flag 为True 是即是可以写入
        if write_flag:
            with open('../data/info.txt', 'r', encoding='utf-8') as f1:  # 从源文件读
                with open('../data/info1.txt', 'w', encoding='utf-8') as f2:  # 写入的新文件
                    ret = f1.readline()
                    while ret:
                        ret = ret.strip('\n')
                        ret = eval(ret)
                        if ret['level'] == 0:
                            self.subject.append(sj)  # 便于在show_subject时不读写文件
                            ret['subject'].append(sj)
                        f2.write(str(ret) + '\n')
                        ret = f1.readline()
            os.remove('../data/info.txt')
            os.rename('../data/info1.txt', '../data/info.txt')
            print("创建课程 {}成功".format(sj))

    def add_account(self):
        """
        创建学生用户
        """
        student_name = input("请输入学生的用户名:").strip()
        student_passwd = input("请输入学生的密码:").strip()
        new_account = student(student_name, student_passwd, 1)
        new_account.save_info()
        # 创建学生用户写入日志
        with open('../log/add_user_log.txt', mode='a', encoding='utf-8') as f3:
            f3.write(
                "{}学生用户{}创建成功\n".format(
                    time.strftime("%Y-%m-%d %X"),
                    student_name))
        print("学生账户创建成功")

    def show_all_student(self):
        '''
        显示所有学生账户
        '''
        with open('../data/info.txt', 'r', encoding='utf-8') as f:
            ret = f.readline()
            while ret:
                ret = ret.strip('\n')
                ret = eval(ret)
                if ret['level'] == 1:
                    print('--------------{}-------------'.format(ret['name']))
                ret = f.readline()

    def show_all_stu_sub(self):
        '''
        显示所有账户的账户和所选课程
        '''
        with open('../data/info.txt', 'r') as f:
            ret = f.readline()
            while ret:
                ret = ret.strip('\n')
                ret = eval(ret)
                if ret['level'] == 1:
                    print(
                        '-------账户名：{}--------选择的课程{}'.format(ret['name'], ret['subject']))
                ret = f.readline()

    def create_lecturer(self):
        """
        创建讲师
        :return:
        """
        lecturer_name = input("请输入讲师的用户名:").strip()
        lecturer_passwd = input("请输入讲师的密码:").strip()
        new_lecturer = teacher(lecturer_name, lecturer_passwd, 2)
        new_lecturer.save_info()
        # 创建好了后在讲师的lecturer字段添加该讲师的名称
        with open("../data/info.txt", mode='r', encoding='utf-8') as f1:
            with open('../data/info1.txt', mode='w', encoding='utf-8') as f2:
                ret = f1.readline()
                while ret:
                    ret = ret.strip('\n')
                    ret = eval(ret)
                    if ret['name'] == 'admin':
                        ret['lecturer'].append(lecturer_name)
                    f2.write(str(ret) + '\n')
                    ret = f1.readline()
        os.remove('../data/info.txt')
        os.rename('../data/info1.txt', '../data/info.txt')
        with open('../log/add_user_log.txt', mode='a', encoding='utf-8') as f3:
            f3.write(
                "{}讲师用户{}创建成功\n".format(
                    time.strftime("%Y-%m-%d %X"),
                    lecturer_name))
        print("讲师账户创建成功")

    def lecturer_class(self):
        """
        讲师指定班级
        首先要判断讲师是否存在，班级是否存在，不存在的话，添加和更改文件
        :return:
        """
        write_flag = False
        lecturer = input("请输入要指定的教师:").strip()
        grade = input("请输入要指定的班级:").strip()
        # 实现检验班级和老师都存在且讲师的班级未添加，为下面的添加班级做准备
        with open("../data/info.txt", mode='r', encoding='utf-8') as f:
            ret = f.readline()
            while ret:
                ret = ret.strip('\n')
                ret = eval(ret)
                # 判断是否有该老师和班级
                if (ret['name'] == 'admin') and (
                        grade in ret['class_grade']) and (lecturer in ret['lecturer']):
                    # 判断班级和老师是否存在,
                    write_flag = True
                # 判断用户自己是否已有该班级
                if (ret['name'] == lecturer) and (ret['level'] == 2):
                    if grade in ret['class_grade']:
                        write_flag = False
                        break
                ret = f.readline()
        # 当班级和老师都存在且讲师的班级未添加，就可以进行添加了
        if write_flag:
            with open("../data/info.txt", mode='r', encoding='utf-8') as f1:
                with open('../data/info1.txt', mode='w', encoding='utf-8') as f2:
                    ret = f1.readline()
                    while ret:
                        ret = ret.strip('\n')
                        ret = eval(ret)
                        if ret['name'] == lecturer:
                            ret['class_grade'].append(grade)
                        f2.write(str(ret) + '\n')
                        ret = f1.readline()
            os.remove('../data/info.txt')
            os.rename('../data/info1.txt', '../data/info.txt')
            print("{}老师指定班级为{}".format(lecturer, grade))
        else:
            # 由于有三种错误情况，分开较为繁琐，这边统一用一个提示
            print("班级或老师不存在,或是该班级已经在该老师的列表中")

    def create_class(self):
        """
        创建班级
        :return:
        """
        write_flag = False
        class_name = input("请输入班级的名称:").strip()
        with open("../data/info.txt", mode='r', encoding='utf-8') as f:
            ret = f.readline()
            while ret:
                ret = ret.strip('\n')
                ret = eval(ret)
                if ret['name'] == 'admin' and class_name in ret['class_grade']:
                    print("班级已经存在，请勿重复添加！！！")
                    break
                else:
                    write_flag = True
                ret = f.readline()
        if write_flag:
            with open("../data/info.txt", mode='r', encoding='utf-8') as f1:
                with open('../data/info1.txt', mode='w', encoding='utf-8') as f2:
                    ret = f1.readline()
                    while ret:
                        ret = ret.strip('\n')
                        ret = eval(ret)
                        if ret['name'] == 'admin':
                            ret['class_grade'].append(class_name)
                        f2.write(str(ret) + '\n')
                        ret = f1.readline()
            os.remove('../data/info.txt')
            os.rename('../data/info1.txt', '../data/info.txt')
            print("班级创建成功")

    def student_class(self):
        """
        学生指定班级
        :return:
        """
        write_flag = False
        status_flag = False
        user_student = input("请输入要指定的学生:").strip()
        grade = input("请输入要指定的班级:").strip()
        # 实现检验班级和学生都存在且班级未添加，为下面的指定班级做准备
        with open("../data/info.txt", mode='r', encoding='utf-8') as f:
            ret = f.readline()
            while ret:
                ret = ret.strip('\n')
                ret = eval(ret)
                if (ret['name'] == 'admin') and (grade in ret['class_grade']):
                    # 判断班级是否存在,
                    write_flag = True
                    status_flag = True # 用于判断班级存在
                if ret['name'] == user_student and ret['level'] == 1:
                    if grade in ret['class_grade']:
                        write_flag = False
                        break
                    else:
                        if status_flag:
                            write_flag = True
                            break
                else:
                    write_flag = False
                ret = f.readline()
        # 当班级和学生都存在且班级未添加，就可以进行添加了
        if write_flag:
            with open("../data/info.txt", mode='r', encoding='utf-8') as f1:
                with open('../data/info1.txt', mode='w', encoding='utf-8') as f2:
                    ret = f1.readline()
                    while ret:
                        ret = ret.strip('\n')
                        ret = eval(ret)
                        if ret['name'] == user_student:
                            ret['class_grade'].append(grade)
                        f2.write(str(ret) + '\n')
                        ret = f1.readline()
            os.remove('../data/info.txt')
            os.rename('../data/info1.txt', '../data/info.txt')
            print("学生{}指定班级{}".format(user_student, grade))
        else:
            print("该班级已经存在用户中或是用户不存在 或是该班级不存在 。添加有误！")
