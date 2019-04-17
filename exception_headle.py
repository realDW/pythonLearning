# python 的异常处理机制

# try:
#     year = int(input('请输入年份：'))
# except ValueError as e:
#     print("请输入正确的格式")
# finally:
#     print("最后调用的 finally")

# 捕获多个异常
# try:
#     print('hello')
# except (KeyError, ValueError, NameError):
#     print('hi')
# finally:
#     print('hello')


# 打印错误信息
# try:
#     a = 1 / 0
# except ZeroDivisionError as e:
#     print('被除数不能为 0，异常信息：%s' % e)
# finally:
#     print('最后finally')

# finally 资源关闭
# try:
#     a = open('hell2o.py', 'r+')
# except FileNotFoundError as fe:
#     print('exception : %s' % fe)
# finally:
#     a.close()

# 自定义异常信息
try:
    raise NameError('daiwei Error!')
except NameError as n:
    print(n)