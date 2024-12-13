import math
#1
def helpdig(a):
    b = a.replace('-','')
    print(a,b)
    if a.isdigit():
        a = int(a)
    elif (b.isdigit()):
        a = int(a)
    return a

def isdig():
    x, y = input('Введите координаты одной из трех точек через пробел (x,y)\n').split()  
    x = helpdig(x)   
    y = helpdig(y)
    while(not(type(x) == int and type(y) == int)):
        x, y = input('Вы ввели не числа! Повторите попытку\n').split()  
        x = helpdig(x)   
        y = helpdig(y)
    return x, y 

def angle(x,y):
    tg = y/x
    ang = math.atan(tg)
    return ang
    

x1, x2 = isdig()
y1, y2 = isdig()
z1, z2 = isdig()
print(f'X({x1}, {x2}), Y({y1}, {y2}), Z({z1}, {z2})')
if (angle(x1,x2) < angle(y1, y2)) and (angle(y1, y2) < angle(z1, z2)):
    print(f'Наименьший угол с осью абсцисс составляет точка с координатами ({x1},{x2})\nУгол равен: {angle(x1, x2)} рад.-')
elif (angle(z1, z2) < angle (x1, x2)) and (angle(z1, z2) < angle(y1, y2)):
    print(f'Наименьший угол с осью абсцисс составляет точка с координатами ({z1},{z2})\nУгол равен: {angle(z1, z2)} рад.')
else:
    print(f'Наименьший угол с осью абсцисс составляет точка с координатами ({y1},{y2})\nУгол равен: {angle(y1, y2)} рад.')
#2

def isprime(num):
    l = []
    for i in range(1,num):
        count = 0
        for k in range(1, i + 1):
            if (i % k) == 0:
                count += 1
            if count == 2 and (k == i):
                l.append(i)
    return l


def ispal(x):
    binary = bin(x)[2:]
    q = False
    if binary == binary[::-1]:
        q = True
    return q
            
  
n = input('Введите любое натуральное число\n')
while(not(n.isdigit())):
    n = input('Вы ввели не натуральное число! \tПовторите попытку\n')
n = int(n)
l = isprime(n)
print(l)
print('Палиндромы:')
for i in range(len(l)):
    if ispal(l[i]):
        print(f'{l[i]}: {bin(l[i])[2:]}')



#traash
'''

def secsys(x):
    helpnum = 0
    sum = 0
    county = 1
    while(helpnum != 1):
        if(x // 2 <= 1):
            helpnum = 1
        sum = county * (x % 2) + sum
        county *= 10
        x = x // 2
    sum = county * x + sum
    return sum






  v = 0
    q = False
    l = []
    helpnum = x
    count = 1
    c = 0
    while (helpnum // 10 > 9):
        helpnum /= 10
        count += 1
    print(count)
    for p in range(count):
        if p == 0:
            v = x % 10 + v
        else:
            v = (x // p * 10) % 10
        l.append(v)
    for i in range(len(l)):
        if l[i] == l[len(l) - i - 1]:
            c += 1
    if (c >= len(l)/2):
        q = False
    else: 
        q = True
    return q
'''