#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import hashlib


class student:
    """学生类"""

    def __init__(
            self,
            name,
            passwd,
            level,
            subject=[],
            class_grade=[],
            lecturer=[]):
        """
        用户属性
        :param name:用户名称
        :param passwd:用户密码
        :param level:用户等级，0表示管理员，1表示学生，2表示老师，管理用户默认创建为admin，密码123
        :param subject:用户选的课程
        :param  class_grade:用户所选的班级,默认为空表示未选班级
        :param  lecturer:用户所选的讲师,默认为空表示未选讲师
        """

        self.name = name
        hash = hashlib.md5()
        hash.update(bytes(passwd, encoding='utf-8'))
        self.passwd = hash.hexdigest()  # 实现密码加密
        self.level = level
        self.subject = subject
        self.class_grade = class_grade
        self.lecturer = lecturer

    def save_info(self):
        """
        保存用户信息到文件
        """
        info = {
            'name': self.name,
            'passwd': self.passwd,
            'level': self.level,
            'subject': self.subject,
            'class_grade': self.class_grade,
            'lecturer': self.lecturer
        }
        with open('../data/info.txt', 'a', encoding='utf-8') as f:
            f.write(str(info) + '\n')

    def show_total_subject(self):
        """
        显示所有的课程
        """
        with open('../data/info.txt', 'r', encoding='utf-8') as f:
            ret = f.readline()
            while ret:
                ret = ret.strip('\n')
                ret = eval(ret)
                if ret['level'] == 0:
                    print(ret['subject'])
                ret = f.readline()

    def choose_subject(self):
        """
        选择课程
        选择完后将内容写到新的文件并重命名为info.txt
        """
        # 是否写入标志位
        write_flag = False

        sj = input("请选择你想要学习的课程：").strip()
        # 判断课程是否存在，且课程是否已经在我的课程列表
        with open('../data/info.txt', 'r', encoding='utf-8') as f:
            ret = f.readline()
            while ret:
                ret = ret.strip('\n')
                ret = eval(ret)
                # 判断课程是否存在
                if ret['name'] == 'admin':
                    if sj in ret['subject']:
                        ret = f.readline()
                        continue
                    else:
                        print("该课程不存在，请联系管理员添加。")
                        write_flag = False
                        break
                # 判断用户是否已经添加了该课程
                if ret['name'] == self.name:
                    if sj in ret['subject']:
                        print("您的课程已经存在,请不要重复添加，谢谢")
                    else:
                        write_flag = True
                ret = f.readline()
        if write_flag:
            with open('../data/info.txt', 'r', encoding='utf-8') as f1:
                with open('../data/info1.txt', 'w', encoding='utf-8') as f2:  # 写入的新文件
                    ret = f1.readline()
                    while ret:
                        ret = ret.strip('\n')
                        ret = eval(ret)
                        if ret['name'] == self.name:
                            # 便于在show_subject时不读写文件
                            self.subject.append(sj)
                            ret['subject'].append(sj)
                        f2.write(str(ret) + '\n')
                        ret = f1.readline()
            os.remove('../data/info.txt')
            os.rename('../data/info1.txt', '../data/info.txt')
            print("{}课程已经添加成功".format(sj))

    def show_subject(self):
        """
        显示用户已经选择的课程
        """
        print('已经选择的课程', self.subject)

    def quit_procedure(self):
        """
        退出
        """
        exit(0)
