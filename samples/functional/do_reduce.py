#!/usr/bin/env python
# encoding: utf-8
"""
reduce(function, sequence[, initial]) -> value

解释：先将 sequence 的前两个 item 传给 function，即 function(item1, item2)，函数的返回值和 sequence 的下一个 item 再传给 function，即 function(function(item1, item2), item3)，如此迭代，直到 sequence 没有元素，如果有 initial，则作为初始值调用。

效果等同：
reduece(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""

from functools import reduce

num = reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 相当于 ((1 * 2) * 3) * 4
print(num)
# 24

num = reduce(lambda x, y: x * y, [1, 2, 3, 4], 5)  # ((((5 * 1) * 2) * 3)) * 4
print(num)
# 120

num = reduce(lambda x, y: x / y, [2, 3, 4], 72)  # (((72 / 2) / 3)) / 4
print(num)
# 3

num = reduce(lambda x, y: x + y, [1, 2, 3, 4], 5)  # ((((5 + 1) + 2) + 3)) + 4
print(num)
# 15

num = reduce(lambda x, y: x - y, [8, 5, 1], 20)  # ((20 - 8) - 5) - 1
print(num)
# 6

f = lambda a, b: a if (a > b) else b  # 两两比较，取最大值
num = reduce(f, [5, 8, 1, 10])
print(num)
# 10
