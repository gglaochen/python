#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
序列化，同java serialization
"""
__author__ = 'ChenHanLin'

import pickle

# 序列化
d = dict(name='a', age=20, score=88)
seria = pickle.dumps(d)
print(seria)
# 反序列化
print(pickle.loads(seria))
