# 记录生肖，根据年份来判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# cur_zodiac = chinese_zodiac[0:5]

# 根据输入的年份判断当年生肖
# year = int(input("请输入年份："))
#
# if year == 2018:
#     print("去年的运势还是不错的哦！")
#
# print(chinese_zodiac[year % 12])

# 1、实现 for 循环打印 1- 20

# for i in range(1, 21):
#     print(i)

# 2、实现2000-2020的区间生肖打印
# for year in range(2000, 2021):
#     print('%s 年是中国 %s年' %(year, chinese_zodiac[year % 12]))

import time

num = 1

while True:
    num = num + 1
    if num == 10:
        continue
    print(num)
    time.sleep(1)



