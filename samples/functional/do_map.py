#!/usr/bin/env python
# encoding: utf-8
"""
map(func, *iterables) --> map object

map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
"""


def square(x):
    return x * x


iter = map(square, [1, 2, 3, 4])
print(list(iter))
# [1, 4, 9, 16]

iter = map(lambda x: x * x, [1, 2, 3, 4])  # 使用 lambda
print(list(iter))
# [1, 4, 9, 16]

iter = map(str, [1, 2, 3, 4])
print(list(iter))
# ['1', '2', '3', '4']

iter = map(int, ['1', '2', '3', '4'])
print(list(iter))
# [1, 2, 3, 4]
