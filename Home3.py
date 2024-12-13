#1
n = int(input('Введите колиечство n натуральных чисел не превышающее 100 для расчета суммы их кубов\n'))
sum = 0
if n > 100:
    print('Ошибка! Вы ввели число большее 100')
else:
    for i in range(n+1):
        sum = sum + i * i * i
    print(f'Сумма кубов всех натуральных чисел до {n} равна {sum}')
    print()   
#2
print('     Таблица умножения')
for i in range(1,10):
    for j in range(1,10):
        if(j*i) / 10 >= 1:
            print(j*i, end=' ') 
        else:
            print(j*i, end='  ') 
    print()
#3
print('Таблица умножения наоборот')
for i in range(1,10):
    for j in range(1,10):
        if((10 - j)*i) / 10 >= 1:
            print((10 - j)*i, end=' ') 
        else:
            print((10 - j)*i, end='  ') 
    print()
#*
print('Таблица умножения наоборот (в другую сторону)')
for i in range(1,10):
    for j in range(1,10):
        if((10 - i)*j) / 10 >= 1:
            print((10 - i)*j, end=' ') 
        else:
            print((10 - i)*j, end='  ') 
    print()