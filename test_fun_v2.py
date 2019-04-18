# 函数调用 关键字参数  关键字 end
print('aaa', end='\n\n')

print('aaa')


# 多个参数函数
def func(a, b, c):
    print('a = %s' % a)
    print('b = %s' % b)
    print('c = %s' % c)


func(1, 2, 3)

print('=============')

# 使用关键字参数 参数顺序可变
func(a=1, c=3, b=4)


# 可变长参数
def args_long(arg1, *args):
    return 1 + len(args)


print('=============')

print(args_long('abc', 'c', 'c', '4'))
