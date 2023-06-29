a = str(input('Введите строку: '))
list = []
for bykva in a:
    list.append(bykva)
count = len(list)
list1 = []
list2 = []
ccount = count // 2
for i in range(count):
    if i < ccount:
        list1.append(list[i])
    else:
        list2.append(list[i])
list2.reverse()
count_True = 0
for i in range(len(list1)):
    if list1[i] == list2[i]:
        count_True += 1
if count_True == len(list1):
    print(True)
else:
    print(False)