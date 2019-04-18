# 定义一个函数
def hello(world):
    for i in range(0, 10):
        print('hello %s - %d' %(world, i))


# 定义一个有返回值的函数
def my_sum(n, m):
    return n + m


# 调用函数
hello('daiwei')
result = my_sum(1, 2)
print(result)