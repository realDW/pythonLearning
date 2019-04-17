# 写文件操作

file1 = open('/Users/daiwei/hello.txt', 'w')

words = ['hello，this words wrote by python!', '\nhello again~']

# file1.writelines('hello，this words wrote by python!')

file1.writelines(words)

file1.close()

