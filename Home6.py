#5

import random
import math
a, b = input('Введите натуральные числа, обозначающие количество строчек и столбцов через пробел\n').split()
while(not(a.isdigit() and b.isdigit())):
    a, b = input('Вы ввели не число!!!!!! \tПовторите попытку\n').split()
a, b = int(a), int(b)
k = []
summax = -999999
summaxnum = 1
summin = math.inf
summinnum = 1
for i in range(a):
    l = []
    sum = 0
    for j in range(b):
        l.append(random.randint(-9,9))
        sum += l[j]
    print(l)
    k.append(l)
    if summax < sum: 
        summax = sum
        summaxnum = i
    if summin > sum: 
        summin = sum
        summinnum = i
print(f'Наибольшая сумма слагаемых находится в строчке {summaxnum + 1}. Сумма равна {summax}\nНаименьшая сумма слагаемых находится в строчке {summinnum + 1}. Сумма равна {summin}')
#6

def checknum(lst, num):
    i = 0
    while i != len(lst):
        if lst[i] == num:
            num = random.randint(-999, 999)
            i = 0
        i += 1
    lst.append(num)
    return lst, num

x, y = input('Введите натуральные числа, обозначающие количество строчек и столбцов через пробел\n').split()
while(not(x.isdigit() and y.isdigit())):
    x, y = input('Вы ввели не число!!!!!! \tПовторите попытку\n').split()
x, y = int(x), int(y)
k = []
lst = []
check = []
for i in range(x):
    l = []
    min = math.inf
    munnum = 0
    for j in range(y):
        check, helpnum = checknum(check, random.randint(-999, 999))
        l.append(helpnum)
        if min > l[j]:
            min = l[j]
            minnum = j
    print(l)
    if min % 2 == 1:
        l[minnum] = 1
    else:
        l[minnum] = 0
    k.append(l)
for i in range(len(k)):
    print(k[i])
