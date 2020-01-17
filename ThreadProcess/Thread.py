#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
线程
_thread是低级模块
threading是高级模块
由于python解释器有GIL锁，多线程在Python中只能交替执行(历史遗留问题)，多核系统执行python也只能用到一核，但多进程可以实现多核任务
"""
__author__ = 'ChenHanLin'

import threading
import time


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('main thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('main thread %s ended.' % threading.current_thread().name)

'''
锁
多进程中，同一个变量各有一份拷贝在每个进程中，互不影响
多线程中，同一个变量都由所有线程共享
'''
balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance - n
    balance = balance + n


for i in range(100000):
    # 先要获取锁:
    lock.acquire()
    try:
        # 放心地改吧:
        change_it(i)
    finally:
        # 改完了一定要释放锁:
        lock.release()
"""
ThredLocal 在python中的用法为threading.local()
"""

local_school = threading.local()
global_school = 1


def func():
    global local_school
    global global_school
    for j in range(100):
        local_school = j
        print('%s>>>%s>>>local>>>>%s' % (threading.current_thread().name, j, local_school))
        global_school = j
        print('%s>>>%s>>>global>>>>%s' % (threading.current_thread().name, j, local_school))


for i in range(3):
    t = threading.Thread(target=func, name='thread' + str(i))
    t.start()

time.sleep(5)
