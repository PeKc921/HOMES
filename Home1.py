import math

r = int(input('Введите радиус данной окружности в см.\n'))
l = round(2 * math.pi * r,2)
s = round(math.pi * r**2,2)
print(f'Радиус нашей окружности - {r} см. \nДлина окружности - {l} см.\nПлощадь круга - {s} см^2')