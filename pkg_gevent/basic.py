#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import gevent
#
#
# def foo():
#     print('Running in foo')
#     gevent.sleep(0)
#     print('Explicit context switch to foo again')
#
#
# def bar():
#     print('Explicit context to bar')
#     gevent.sleep(0)
#     print('Implicit context switch back to bar')
#
#
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])

"""
results:
    Running in foo
    Explicit context to bar
    Explicit context switch to foo again
    Implicit context switch back to bar
"""

# import time
# import gevent
# from gevent import select
#
# start = time.time()
# tic = lambda: 'at %1.1f seconds' % (time.time() - start)
#
#
# def gr1():
#     # Busy waits for a second, but we don't want to stick around...
#     print('Started Polling: %s' % tic())
#     select.select([], [], [], 2)
#     print('Ended Polling: %s' % tic())
#
#
# def gr2():
#     # Busy waits for a second, but we don't want to stick around...
#     print('Started Polling: %s' % tic())
#     select.select([], [], [], 2)
#     print('Ended Polling: %s' % tic())
#
#
# def gr3():
#     print("Hey lets do some stuff while the greenlets poll, %s" % tic())
#     gevent.sleep(1)
#     print('end gr3 %s' % tic())
#
#
# gevent.joinall([
#     gevent.spawn(gr1),
#     gevent.spawn(gr2),
#     gevent.spawn(gr3),
# ])
from gevent.hub import Waiter

"""
result:
    Started Polling: at 0.0 seconds
    Started Polling: at 0.0 seconds
    Hey lets do some stuff while the greenlets poll, at 0.0 seconds
    end gr3 at 1.0 seconds
    Ended Polling: at 2.0 seconds
    Ended Polling: at 2.0 seconds
"""

# import gevent
# import random
#
#
# def task(pid):
#     gevent.sleep(random.randint(0, 2) * 0.001)
#     print("Task %s done." % pid)
#
#
# def synchronous():
#     for i in range(1, 10):
#         task(i)
#
#
# def asynchronous():
#     threads = [gevent.spawn(task, i) for i in range(10)]
#     gevent.joinall(threads)
#
#
# print('Synchronous:')
# synchronous()
#
# print('Asynchronous:')
# asynchronous()

"""
result:
    Synchronous:
    Task 1 done.
    Task 2 done.
    Task 3 done.
    Task 4 done.
    Task 5 done.
    Task 6 done.
    Task 7 done.
    Task 8 done.
    Task 9 done.
    Asynchronous:
    Task 0 done.
    Task 7 done.
    Task 3 done.
    Task 4 done.
    Task 5 done.
    Task 8 done.
    Task 9 done.
    Task 1 done.
    Task 2 done.
    Task 6 done.
"""

# import gevent.monkey
#
# gevent.monkey.patch_socket()
# import gevent
# import requests
# import time
#
#
# def fetch(pid):
#     requests.get('http://www.baidu.com')
#     print('Process {},{}'.format(pid, time.time()))
#
#
# def synchronous():
#     for i in range(1, 10):
#         fetch(i)
#
#
# def asynchronous():
#     threads = [gevent.spawn(fetch, i) for i in range(10)]
#     gevent.joinall(threads)
#
# print('Synchronous:')
# synchronous()
#
# print('Asynchronous:')
# asynchronous()

"""
result:
    Synchronous:
    Process 1,1518078253.29675
    Process 2,1518078253.381696
    Process 3,1518078253.478975
    Process 4,1518078253.5542378
    Process 5,1518078253.641247
    Process 6,1518078253.71512
    Process 7,1518078253.797309
    Process 8,1518078253.887291
    Process 9,1518078253.963506
    Asynchronous:
    Process 0,1518078254.057664
    Process 6,1518078254.0592341
    Process 8,1518078254.06039
    Process 4,1518078254.061583
    Process 5,1518078254.062714
    Process 9,1518078254.063721
    Process 7,1518078254.065095
    Process 1,1518078254.0687912
    Process 2,1518078254.0699148
    Process 3,1518078254.071058
"""

# import time
# from multiprocessing.pool import Pool
#
#
# def echo(i):
#     time.sleep(0.001)
#     return i
#
#
# p = Pool(10)
# run1 = [a for a in p.imap_unordered(echo, range(10))]
# run2 = [a for a in p.imap_unordered(echo, range(10))]
# run3 = [a for a in p.imap_unordered(echo, range(10))]
# run4 = [a for a in p.imap_unordered(echo, range(10))]
#
# print(run1 == run2 == run3 == run4)
#
# from gevent.pool import Pool
# p=Pool(10)
# run1 = [a for a in p.imap_unordered(echo, range(10))]
# run2 = [a for a in p.imap_unordered(echo, range(10))]
# run3 = [a for a in p.imap_unordered(echo, range(10))]
# run4 = [a for a in p.imap_unordered(echo, range(10))]
#
# print(run1 == run2 == run3 == run4)
"""
result:
    False
    True
"""

# import gevent
# from gevent import Greenlet
#
#
# def foo(message, n):
#     gevent.sleep(n)
#     print(message)
#
#
# thread1 = Greenlet.spawn(foo, "Hello", 1)
# thread2 = gevent.spawn(foo, "I live!", 2)
# thread3 = gevent.spawn(lambda x: (x + 1), 2)
# threads = [thread1, thread2, thread3]
# gevent.joinall(threads)

"""
result:
    Hello
    I live!
"""

# import gevent
# from gevent import Greenlet
#
#
# class MyGreenlet(Greenlet):
#     def __init__(self, message, n):
#         Greenlet.__init__(self)
#         self.message = message
#         self.delay = n
#
#     def _run(self):
#         print(self.message)
#         gevent.sleep(self.delay)
#
#
# g = MyGreenlet("Hi there!", 3)
# g.start()
# g.join()

"""
result:
    Hi there!
"""

# import gevent
#
#
# def win():
#     return 'You win'
#
#
# def fail():
#     raise Exception('You fail at failing.')
#
#
# winner = gevent.spawn(win)
# loser = gevent.spawn(fail)
#
# print(winner.started)
# print(loser.started)
# try:
#     gevent.joinall([winner, loser])
# except Exception as e:
#     print('This will never be reached')
#
# print(winner.value)
# print(loser.value)
#
# print(winner.ready())
# print(loser.ready())
#
# print(loser.exception)

# import gevent
# import signal
#
#
# def run_forever():
#     gevent.sleep(100)
#
#
# if __name__ == '__main__':
#     gevent.signal(signal.SIGQUIT, gevent.shutdown)
#     thread = gevent.spawn(run_forever)
#     thread.join()

# import gevent
# from gevent import Timeout
#
# seconds = 10
#
# timeout = Timeout(seconds)
# timeout.start()
#
#
# def wait():
#     gevent.sleep(4)
#
#
# try:
#     gevent.spawn(wait).join()
# except Timeout:
#     print("Could not compelte!")

# import gevent
# from gevent import Timeout
#
# time_to_wait = 5
#
#
# class TooLong(Exception):
#     pass
#
#
# with Timeout(time_to_wait, TooLong):
#     gevent.sleep(10)

# import gevent
# from gevent import Timeout
#
#
# def wait():
#     gevent.sleep(2)
#
#
# timer = Timeout(1).start()
# thread1 = gevent.spawn(wait)
# try:
#     thread1.join(timeout=timer)
# except Timeout:
#     print('Thread1 time out')
#
# timer = Timeout.start_new(1)
# thread2 = gevent.spawn(wait)
# try:
#     thread2.get(timeout=timer)
# except  Timeout:
#     print('Thread2 time out')
#
# try:
#     gevent.with_timeout(1, wait)
# except Timeout:
#     print('Thread3 time out')

# import socket
#
# print(socket.socket)
# print('After monkey patch')
# from gevent import monkey
#
# monkey.patch_socket()
# print(socket.socket)
# import select
#
# print(select.select)
# monkey.patch_select()
# print("After monkey patch")
# print(select.select)


# import gevent
# from gevent.event import Event
#
# evt = Event()
#
#
# def setter():
#     print('A: Hey wait for me, I have to do something')
#     gevent.sleep(3)
#     print("Ok, I'm done")
#     evt.set()
#
#
# def waiter():
#     '''After 3 seconds the get call will unblock'''
#     print("I'll wait for you")
#     evt.wait()  # blocking
#     print("It's about time")
#
#
# def main():
#     gevent.joinall([
#         gevent.spawn(setter),
#         gevent.spawn(waiter),
#         gevent.spawn(waiter),
#         gevent.spawn(waiter),
#         gevent.spawn(waiter),
#         gevent.spawn(waiter)
#     ])
#
#
# if __name__ == '__main__':
#     main()

# import gevent
# from gevent.event import AsyncResult
#
# a = AsyncResult()
#
#
# def setter():
#     gevent.sleep(3)
#     a.set('Hello')
#
#
# def waiter():
#     print(a.get())
#
#
# gevent.joinall([
#     gevent.spawn(setter),
#     gevent.spawn(waiter),
# ])

# import gevent
# from gevent.queue import Queue
#
# tasks = Queue()
#
#
# def worker(n):
#     while not tasks.empty():
#         task = tasks.get()
#         print('Worker %s got task %s' % (n, task))
#         gevent.sleep(0)
#
#     print('Quitting time!')
#
#
# def boss():
#     for i in range(1, 25):
#         tasks.put_nowait(i)
#
#
# gevent.spawn(boss).join()
# print(tasks)
# gevent.joinall([
#     gevent.spawn(worker, 'steve'),
#     gevent.spawn(worker, 'john'),
#     gevent.spawn(worker, 'nancy'),
# ])

# import gevent
# from gevent.queue import Queue, Empty
#
# tasks = Queue(maxsize=3)
#
#
# def worker(n):
#     try:
#         while True:
#             task = tasks.get(timeout=1)
#             print('Worker %s got task %s' % (n, task))
#             gevent.sleep(0)
#     except Empty:
#         print("Quitting time")
#
#
# def boss():
#     for i in range(1, 10):
#         tasks.put(i)
#     print('Assigned all work in iteration 1')
#     for i in range(10, 20):
#         tasks.put(i)
#     print('Assigned all work in iteration 2')
#
#
# gevent.joinall([
#     gevent.spawn(boss),
#     gevent.spawn(worker, 'steve'),
#     gevent.spawn(worker, 'john'),
#     gevent.spawn(worker, 'bob'),
# ])

# import gevent
# from gevent.pool import Group
#
#
# def talk(msg):
#     for _ in range(3):
#         print(msg)
#
#
# g1 = gevent.spawn(talk, 'bar')
# g2 = gevent.spawn(talk, 'foo')
# g3 = gevent.spawn(talk, 'fizz')
#
# group = Group()
# group.add(g1)
# group.add(g2)
# group.join()
# print('group add g3')
# group.add(g3)
# group.join()

# import gevent
# from gevent import getcurrent
# from gevent.pool import Group
#
# group = Group()
#
#
# def hello_from(n):
#     print('Size of group %s' % len(group))
#     print('Hello from Greenlet %s' % id(getcurrent()))
#
#
# group.map(hello_from, range(3))
#
#
# def intensive(n):
#     gevent.sleep(3 - n)
#     return 'task', n
#
#
# print('Ordered')
#
# ogroup = Group()
# for i in ogroup.imap(intensive, range(3)):
#     print(i)
#
# print('Unordered')
#
# igroup = Group()
# for i in igroup.imap_unordered(intensive, range(3)):
#     print(i)

# from gevent import sleep
# from gevent.pool import Pool
# from gevent.coros import BoundedSemaphore
#
# sem = BoundedSemaphore(2)
#
# def worker1(n):
#     sem.acquire()
#     print('Worker %i acquired semaphore' % n)
#     sleep(0)
#     sem.release()
#     print('Worker %i released semaphore' % n)
#
# def worker2(n):
#     with sem:
#         print('Worker %i acquired semaphore' % n)
#         sleep(0)
#     print('Worker %i released semaphore' % n)
#
# pool = Pool()
# pool.map(worker1, xrange(0,2))
# pool.map(worker2, xrange(3,6))p(hello_from, range(3))

# import gevent
# from gevent.local import local
#
# stash = local()
#
#
# def f1():
#     print(gevent.get_hub(), gevent.get_hub().loop, type(gevent.getcurrent()), gevent.getcurrent())
#     print(Waiter().hub)
#     stash.x = 1
#     print(stash.x)
#
#
# def f2():
#     print(gevent.get_hub(), type(gevent.get_hub().loop), type(gevent.getcurrent()), gevent.getcurrent())
#     stash.y = 2
#     print(stash.y)
#
#     try:
#         stash.x
#     except AttributeError:
#         print("x is not local to f2")
#
#
# print(gevent.get_hub(), type(gevent.getcurrent()), gevent.getcurrent())
# g1 = gevent.spawn(f1)
# g2 = gevent.spawn(f2)
#
# gevent.joinall([g1, g2])


import gevent
import greenlet


def callback(event, args):
    print
    event, args[0], '===:>>>>', args[1]


def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')


def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')


print('main greenlet info: ', greenlet.greenlet.getcurrent())
print('hub info', gevent.get_hub())
oldtrace = greenlet.settrace(callback)

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
greenlet.settrace(oldtrace)
