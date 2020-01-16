#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
json
"""
__author__ = 'ChenHanLin'

import json

d = dict(name='Bob', age=20, score=88)
# 序列化
jsonResult = json.dumps(d)
print(jsonResult)
# 反序列化
print(json.loads(jsonResult))

print('对象序列化')


# 对象的序列化/反序列化——>还是需要一个中间状态(字典)
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)
objJson = json.dumps(s, default=lambda obj: obj.__dict__)
print(objJson)
print(json.loads(objJson, object_hook=lambda d: Student(d['name'], d['age'], d['score'])))
