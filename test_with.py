# 自定义 with 语句块
class WithTest:

    def __enter__(self):
        print('entry')
        return self  # 如果不返回会报错

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('no Exception')
        else:
            print('has error!')
        print('exit!')

    def print_test(self):
        print('this is a test method')


with WithTest() as wt:
    wt.print_test()