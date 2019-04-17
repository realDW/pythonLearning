file = open('/Users/daiwei/hello.txt', 'rb')

# print(file.read())

# 按行读取

# for line in file.readlines():
#     print(line)
#     print('======')

print('当前指针位置在 %s' %(file.tell()))

print(file.read(10))

print('当前指针位置在 %s' %(file.tell()))

print(file.read(10))

print('当前指针位置在 %s' %(file.tell()))

# seek方法 第二个参数 0 从头开始偏移， 1 从当前位置开始偏移（需要使用 rb 模式打开）
# ，2 从文件尾部开始偏移（同 rb 模式）
file.seek(-1, 2)

print(file.read(10))

print('当前指针位置在 %s' %(file.tell()))

file.close()
