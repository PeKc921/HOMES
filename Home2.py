import math
#1
a, b = input('Введите 2 вещественных числа отличных от нуля\n').split()
if a == 0 or b == 0:
    print('Ошибка! Вы ввели 0')
else:
    print(f'A / B = {round(float(a) / float(b), 3)}; B / A = {round(float(b) / float(a), 3)}')

#2
discount = 0
cart = input('Введите общую стоимость покупки\n')
if float(cart) > 20:
    discount = 0.35
money = round(float(cart) * (1 - discount), 2)
print(f'Итоговая стоимость вашей корзины составляет {money}у.е. Ваша скидка - {discount*100}%')    
#3
month = int(input('Введите целое число от 1 до 12 включительно\n'))
if month > 0 and month < 13:
    if month > 2 and month < 6:
        if month == 3:
            print(f'{month} - Март. Весна')
        elif month == 4:
            print(f'{month} - Апрель. Весна')
        else:
            print(f'{month} - Май. Весна')
    elif month > 8 and month < 12:
        if month == 9:
            print(f'{month} - Сентябрь. Осень')
        elif month == 10:
            print(f'{month} - Октябрь. Осень')
        else:
            print(f'{month} - Ноябрь. Осень')
    elif month > 5 and month < 9:
        if month == 3:
            print(f'{month} - Июнь. Лето')
        elif month == 4:
            print(f'{month} - Июль. Лето')
        else:
            print(f'{month} - Август. Лето')
    else:
        if month == 12:
            print(f'{month} - Декабрь. Зима')
        elif month == 1:
            print(f'{month} - Январь. Зима')
        else:
            print(f'{month} - Февраль. Зима')
else:
    print('Вы ввели неправильное число!')