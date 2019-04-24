# # python 闭包
# def f_sum(a):
#     def add(b):
#         return a + b
#     return add
#
#
# def test_fun():
#     var = 'hello'
#     return var
#
#
# print(test_fun());
#
# print(type(f_sum(2)))
#
# print(f_sum(2)(3))
#
# # 闭包实现的计数器
#
#
# def counter(start=0):
#     # 注意闭包无法直接访问外部函数的局部变量
#     # 可以通过容器来解决
#     cnt = [start]
#
#     def add_cnt():
#         cnt[0] += 1
#         return cnt[0]
#     return add_cnt
#
#
# cnt_fun = counter(3)
#
# print(cnt_fun())
# print(cnt_fun())
# print(cnt_fun())

# 闭包常见使用

#
# def a_line(a, b):
#
#     def cal(x):
#         return a*b*x
#     return cal
#
#
# a_line_cal = a_line(1, 4)
#
# print(a_line_cal(4))
# print(a_line_cal(5))

# 函数装饰器
import time


def time_wrapper(func):
    def wrapper(s):
        start = time.time()
        func(s)
        end = time.time()
        print('函数运行用时 %s' % (end - start))
    return wrapper


def wrapper_plus(argv):
    def wrapper(fun):
        def inner(s):
            print('start %s %s' % (argv, fun.__name__))
            fun(s)
            print('end %s %s' % (argv, fun.__name__))
        return inner
    return wrapper


@wrapper_plus("hello")
def sleep_fun(s):
    time.sleep(s)


sleep_fun(4)