# 记录生肖，根据年份来判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# cur_zodiac = chinese_zodiac[0:5]

# 根据输入的年份判断当年生肖

year = 2018

print(chinese_zodiac[2018 % 12])

print('狗' in chinese_zodiac)

print(chinese_zodiac + 'hello')

print('hello' * 2) 