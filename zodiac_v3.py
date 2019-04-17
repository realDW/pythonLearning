# 星座落在的范围

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

zodiac_date = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

cz_num = {chinese_zodiac[i]: 0 for i in range(len(chinese_zodiac))}
zn_num = {zodiac_name[i]: 0 for i in range(len(zodiac_name))}

# for i in range(len(chinese_zodiac)):
#     cz_num[chinese_zodiac[i]] = 0

# for i in range(len(zodiac_name)):
#     zn_num[zodiac_name[i]] = 0

print(cz_num)
print(zn_num)

while True:
    year = int(input("请输入年："))
    month = int(input("请输入月份："))
    day = int(input("请输入日期："))
    n = 0
    while (month, day) > zodiac_date[n]:
        if month >= 12 and day > 23:
            break;
        n += 1

    # 添加对应生肖和星座到对应的dict
    cz_num[chinese_zodiac[year % 12]] += 1
    zn_num[zodiac_name[n]] += 1

    for each_key in cz_num:
        print("属相 %s 有 --> %d 个" %(each_key, cz_num[each_key]))

    for each_key in zn_num:
        print("星座 %s 有 --> %d 个" %(each_key, zn_num[each_key]))


