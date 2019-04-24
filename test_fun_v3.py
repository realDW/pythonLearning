# 函数作用域
# var1 = 123
#
#
# def test():
#     global var1
#     var1 = 456
#     print(var1)
#
#
# test()
#
# print(var1)


# 函数迭代器与生成器
# my_list = [1, 2, 3, 4]
# my_iter = iter(my_list)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# list 越界会报错
# print(next(my_iter))

# 自定义生成器
# yield 停止函数运行，下次调用继续运行
# def get_next(start, end, step):
#     x = start
#     while x < end:
#         yield x
#         x += step
#
#
# for i in get_next(10, 20, 0.5):
#     print(i)

# lambda 表达式

# lambda: True
#
# lambda x, y: x+y
#
# adict = {'a': 'aaa', 'bb': 'ccc'}
#
# for i in adict.items():
#     print(i[0])


# python 的内建函数
from functools import reduce

test_list = [1, 2, 3, 4, 5]

print(list(filter(lambda x: x > 3, test_list)))

print(list(map(lambda a: a + 1, test_list)))

# reduce 是合并操作，合并所有的item，所有出来是一个 int
print(reduce(lambda x,y: x + y, test_list, 1))

print(list(zip((1, 2, 3), (4, 5, 6))))


