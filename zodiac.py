# 星座落在的范围

# zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
#                u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
#
# zodiac_date = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
#                (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
#
# (month, date) = (1, 10);
#
# zodiac_day = len(list(filter(lambda x : x > (month, date), zodiac_date)))
#
# print(zodiac_name[zodiac_day % 12])

a_list = ['abc', 'xyz']
print(a_list)

a_list.append("X")

print(a_list)

a_list.remove('abc')

print(a_list)


print('X' not in a_list)