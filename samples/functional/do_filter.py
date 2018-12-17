#!/usr/bin/env python
# encoding: utf-8
"""
filter(function or None, iterable) --> filter object

filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
"""

even_num = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(even_num)
# [2, 4, 6]

odd_num = list(filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6]))
print(odd_num)
# [1, 3, 5]

r = filter(lambda x: x < 'g', 'hijack')
print(list(r))
