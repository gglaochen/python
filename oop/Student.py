#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
通过class定义一个类
类名后括号里写从哪个类继承下来
重写__init__方法作为构造方法
所有方法中都有self表示调用该方法的对象
"""
__author__ = 'ChenHanLin'


class Student(object):
    # __slots__用于限制一个类的属性
    __slots__ = ('__name', '__score')

    # python不能定义多个构造方法
    def __init__(self, name, score):
        # 变量前加__表示私有变量外部不能直接访问
        # 但也不是完全不能访问，可以通过_Student__name进行操作（不同版本Python解释器会改成成不同变量名所以不建议这么用），
        self.__name = name
        self.__score = score
        if not score:
            self.__score = 0

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    # 需要注意的是不能通过zzt.__name
    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("成绩必须是整数")
        if score < 0 or score > 100:
            raise ValueError("成绩必须在0到100之间")
        self.__score = score

    def print_score(self):
        print('成绩为%s 名字为%s' % (self.__score, self.__name))

    # __str__相当于java的toString方法
    def __str__(self):
        return "姓名%s  分数%d" % (self.__name, self.__score)

    # 调试时不调用__str__方法二十__repr__方法，因为两种方法基本写法一样可以直接复制
    __repr__ = __str__

    # 作用和在__init__方法里赋予值一样，为了避免没赋值导致报错
    def __getattr__(self, attr):
        if attr == '__name':
            return 'chl'


lisa = Student('lisa', 59)
lisa.print_score()

zzt = Student('zzt', None)
zzt.print_score()
print(zzt._Student__name)
print('名字为', zzt.get_name())
print('toString方法', zzt)

chl = Student(None, None)
print(chl)
