#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
协程
优势 1.协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显
2.不需要多线程的锁机制
所以python经常使用多进程+协程
"""
__author__ = 'ChenHanLin'


# generator
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)

# asyncio提供了完善的异步IO支持

import asyncio
import threading


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # 异步操作需要通过yield from完成
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
# 多个coroutine封装成一组Task然后并发执行
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# python 3.5后提供了新的语法async、await
async def hello2():
    print('Hello world! (%s)' % threading.currentThread())
    # 异步操作需要通过yield from完成
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
# 多个coroutine封装成一组Task然后并发执行
tasks = [hello2(), hello2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
