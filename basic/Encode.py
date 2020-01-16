#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
编码与反编码
"""
__author__ = 'ChenHanLin'

print('abc'.encode('ascii'))

print(b'abc'.decode('utf-8'))

print('中文'.encode('utf-8'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
