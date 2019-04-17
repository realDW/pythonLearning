dict1 = {}
print(type(dict1))

dict2 = {'1467002001': '陈佳祥', '1467002002': '陈龙','1467002003': '代炜'}

print(dict2)

dict2['1467002030'] = '荣桑'

print(dict2)

dict2['1467002030'] = dict2['1467002001']*2

print(dict2)
