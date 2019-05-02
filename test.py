# 日常应用比较广泛的模块是：
# 1、文字处理 re
# 2、日期类型 time 和 datetime
# 3、数字和数字类型的 math、random
# 4、文件和目录访问的 pathlib、os.path
# 5、数据压缩的和归档的 tarfile
# 6、通用操作系统 os、logging、argparse
# 7、多线程 threading、queue
# 8、Integer 数据处理 base64、json、urllib
# 9、结构化标记处理工具 html、xml
# 10、开发工具 unitest
# 11、调试工具 timeit
# 12、软件包发布 venv
# 13、运行服务 __main__

import re

p = re.compile('ca*t')
print(p.match('caaaabt'))
