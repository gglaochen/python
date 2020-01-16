#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件读写
"""
__author__ = 'ChenHanLin'

# 以只读、utf-8方式打开文件
try:
    f = open('D:/doc/myDoc/docker根据sh执行文件生成tar包', 'r', encoding='utf-8')
    print(f.read())
finally:
    if f:
        f.close()

# 可以发现代码不够简洁，所以python提供了以下方式，不必调用close()方法
# w是覆盖写，a是追加写
with open('D:/doc/myDoc/docker根据sh执行文件生成tar包', 'w', encoding='utf-8') as f:
    f.write('Hello, world!')

with open('D:/doc/myDoc/docker根据sh执行文件生成tar包', 'r', encoding='utf-8') as f:
    # 循环每次读一行，避免一次读太多内存占满
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉
