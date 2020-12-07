#!/usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
from time import sleep

print('abc')


def foo1():
    print('I am foo1')


def foo2():
    print('I am foo2')


def foo3():
    print('I am foo3')


if __name__ == '__main__':
    a = Process(target=foo1)
    b = Process(target=foo2)
    c = Process(target=foo3)
    a.start()
    sleep(2)
    b.start()
    c.start()

    a.join()
    b.join()
    c.join()
