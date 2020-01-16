#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
函数相关用法
"""
__author__ = 'ChenHanLin'


def a(x):
    if x <= 1:
        return 1
    else:
        return x + a(x - 1)


print('回调函数', a(3))

'''
map(function,[1,2,3...])
将function作用于第二个list参数的每一个元素上

reduce(function,[1,2,3...])
fucntion需要有两个参数，reduce函数将该function作用于列表的上一个元素和下一个元素
'''
from functools import reduce


def f(x):
    return x * x


a = list(map(str, [1, 2, 3, 4]))
print('将列表转为字符类型', a)

b = list(map(f, [1, 2, 3, 4]))
print('将数字列表求平方', b)


def add(x, y):
    return x + y


c = reduce(add, [1, 2, 3])
print('将数字列表相加', c)

'''
将字符转化为数字型工具方法
'''

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(fn, map(char2num, s))


print('map+reduce将字符转数字', str2int('123123'))

'''
lambda表达式
lambda <参数>:方法体
可以简化一些一行能处理的简单方法
'''


def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(lambda x: DIGITS[x], s))


print('使用lambda进行简化', str2int2('123123'))

'''
filter(function,[1,2,3...])
filter把传入的function作用于每个列表，如果返回为True则保留，反则反之
'''
print('使用filter列表进行过滤', list(filter(lambda x: x % 2 == 1, [1, 2, 3])))

'''
sorted([0,1,2...],key = function,reverse = True)
排序 按照function对元素进行计算后升序排序，如果要降序，设置reverse = True
也可以设置cmp = function，大于则返回1，小于则返回-1，等于则返回0
'''
print('sorted starting...')
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
print(sorted([1, 2, 3, 4, 5, 6], key=lambda x: x % 4))


def foo():
    print("yield starting...")
    while True:
        print("*" * 10)
        res = yield 5
        print("res:", res)


g = foo()
print(next(g))
print("*" * 20)
print(next(g))
print(next(g))

'''
求范围内所有素数
从3开始每次+2
'''


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


'''
元素不被传入参数n整除
'''


def doFilter(n):
    return lambda x: x % n > 0


'''
第一次：2
之后：拿从3开始 每次拿 过滤掉后续(3+2)列表中能整除当前数的元素 并且 执行+2
'''


def getIt():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(doFilter(n), it)


'''
获取素数
'''
print("开始列素数")
for n in getIt():
    if n < 100:
        print(n)
    else:
        break

'''
functools.partial 帮助我们给函数赋予默认值
'''
import functools


def plus(a, b):
    return a + b


plus2 = functools.partial(plus, b=2)

print(plus(1, 2))

print(plus2(a=3))

print(plus2(3))
