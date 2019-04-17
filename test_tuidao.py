res_list = [];
for i in range(1, 10):
    if i % 2 == 0:
        res_list.append(i*i)
print(res_list)

res_list1 = [i*i for i in range(1, 10) if i % 2 == 0]

print(res_list1)
