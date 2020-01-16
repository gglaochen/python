#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
异常处理
BaseException是所有异常的父类，相当于Java的Exception
"""
__author__ = 'ChenHanLin'

import logging
import traceback

# 设置日志级别
logging.basicConfig(level=logging.INFO)

try:
    devide = 10 / 0
except ZeroDivisionError as e:
    print('发送异常:', e)
    # 将异常调用栈记录日志，用日志而不用print一个好处是可以动态设置日志级别，另外日志还可以保存在文件中
    logging.error(traceback.print_exc())
finally:
    print('over')
