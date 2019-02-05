# -*- coding: utf-8 -*-
# class test(object):
#     def __init__(self):
#         self._x = None
#
#     def getx(self):
#         print("get x")
#         return self._x
#
#     def setx(self, value):
#         print("set x")
#         self._x = value
#
#     def delx(self):
#         print("del x")
#         del self._x
#
#     x = property(getx, setx, delx, "I'm the 'x' property.")

#
# class test(object):
#     def __init__(self):
#         self.__x = None
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         self.__x = value
#
#     @x.deleter
#     def x(self):
#         del self.__x
#
#     def my_func(self):
#         pass
#
#
# print test.__dict__
# print test().__dict__
# test().x = 1


# class Singleton(type):
#     def __init__(cls, name, bases, dic):
#         super(Singleton, cls).__init__(name, bases, dic)
#         cls.instance = None
#         print 1, name, bases, dic
#
#     def __call__(cls, *args, **kwargs):
#         print 2
#         if cls.instance is None:
#             cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls.instance
#
#
# class MySingleton(object):
#     __metaclass__ = Singleton
#
#
# MySingleton()


def consumer():
    r = '200 OK'
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER]Consuming %s...' % n)


def produce(c):
    c.next()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER]Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER]Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
