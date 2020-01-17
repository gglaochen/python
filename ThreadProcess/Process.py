#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
进程
"""
__author__ = 'ChenHanLin'

import os
from multiprocessing import Process

print('进程id (%s) 启用...' % os.getpid())


# 仅适用于 Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# 子进程要执行的代码
def run_proc(name):
    print('子进程运行中: %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('父进程 %s.' % os.getpid())
    # args定义传给资金池的参数，必须是tuple类型
    # target是要执行子进程的逻辑(参数是args)
    p = Process(target=run_proc, args=('test',))
    print('子进程将启动.')
    p.start()
    # 等待子进程结束后继续运行
    p.join()
    print('子进程结束.')

"""
进程池
"""
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('第 %s 个进程: %s...' % (name, os.getpid()))
    # 获取当前时间
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('进程 %s 运行了 %0.2f 秒.' % (name, (end - start)))


if __name__ == '__main__':
    print('进程池  父进程id （%s）.' % os.getpid())
    # 创建进程池大小为4(不设置默认是CPU核数)，前四个进程是立即异步执行的，而第五个进程要等之前某个进程执行完成后才执行
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('等待所有子进程结束...')
    # 调用close()后不能继续添加新进程
    p.close()
    p.join()
    print('所有子进程执行完毕.')

"""
启用外部进程
"""
import subprocess

print('$ 请求外部进程 www.python.org')
# nslookup用于查询域名解析是否正常
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
# 如果子进程还需要输入
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)
"""
进程间通信
"""
from multiprocessing import Queue


# 写数据进程执行的代码:
def write(q):
    print('要写入Queue的进程id: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('写入 %s 到队列中...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('要读Queue的进程id: %s' % os.getpid())
    # 轮询读取
    while True:
        value = q.get()
        print('从队列中拿到 %s' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
