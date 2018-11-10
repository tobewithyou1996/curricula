#!/usr/bin/env python
# -*- coding: utf-8 -*-
from student import student


class teacher(student):
    """
    老师类
    """

    def show_class(self):
        """
        显示老师所教的班级
        :return:
        """
        print("-------------{}老师所教的班级有---------".format(self.name))
        for i in self.class_grade:
            print("-------------{}---------".format(i))

    def show_student(self):
        """
        显示老师所教的学生
        :return:
        """
        print("-------------{}老师教的学生有---------".format(self.name))
        with open("../data/info.txt", mode='r', encoding='utf-8') as f:
            ret = f.readline()
            while ret:
                ret = ret.strip('\n')
                ret = eval(ret)
                # 判断是用户，且用户班级列表不为空
                if ret['level'] == 1 and len(ret['class_grade']) > 0:
                    # 学生班级列表是讲师班级列表的子集就意味着学生是该讲师的学生
                    if set(self.class_grade) >= set(ret['class_grade']):
                        print("-------------{}---------".format(ret['name']))
                ret = f.readline()
