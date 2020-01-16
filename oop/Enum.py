#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
导包后
通过class <EnumName>(Enum)定义枚举类
枚举字段关联name和value
name 用于获取某个枚举
value 可以是任意类型
"""
__author__ = 'ChenHanLin'

from enum import Enum, unique


class WeekdayEnum(object):
    __slots__ = ('__code', '__msg', '__desc')

    def __init__(self, code, msg, desc):
        self.__code = code
        self.__msg = msg
        self.__desc = desc

    def getCode(self):
        return self.__code

    def getMsg(self):
        return self.__msg

    def getDesc(self):
        return self.__desc


@unique
class WeekdayEnum(Enum):
    Sun = WeekdayEnum('sunDay', 7, '周日')
    Mon = WeekdayEnum('MonDay', 1, '周一')
    Tue = WeekdayEnum('TuesDay', 2, '周二')
    Wed = WeekdayEnum('WednesDay', 3, '周三')
    Thu = WeekdayEnum('ThursDay', 4, '周四')
    Fri = WeekdayEnum('FriDay', 5, '周五')
    Sat = WeekdayEnum('SaturDay', 6, '周六')


print(WeekdayEnum.Sun.value.getDesc())
