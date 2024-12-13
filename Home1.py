import math
#1

r = int(input('Введите радиус данной окружности в см.\n'))
l = round(2 * math.pi * r,2)
s = round(math.pi * r**2,2)
print(f'Радиус нашей окружности - {r} см. \nДлина окружности - {l} см.\nПлощадь круга - {s} см^2')
#2

print('\tx\t y')
x = 10
y = 55
print(f'\t{x}\t {y}')
x, y = y, x
print(f'\t{x}\t {y}')
#3

l = int(input('Введите длину маятника в метрах\n'))
t = round(2 * math.pi * math.sqrt(l/9.81),2)
print(f'Период колебания матника с длиной {l}м = {t} секунд.')