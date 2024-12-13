import os
import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return [(p**b + a**b) / p**b for p in x]

g = 0
dir = os.getcwd()
a = 1
b = 0.5
x = np.linspace(-1, 1, 1000)
plt.ylim(-5, 5)
plt.plot(x, f(x), color='grey', label='a = 1, b = 1')
a = 1
b = -0.5
plt.plot(x, f(x), color='pink', label='a = 2, b = 1')
a = 1
b = -1.5
plt.plot(x, f(x), color='green', label='a = 1, b = 2')
plt.axvline(g, color='red', linestyle='--', label='Точка разрыва')
plt.legend(loc='lower right', title='Функции')
plt.xlabel('Значение координаты X')
plt.ylabel('Значение координаты Y')
plt.savefig(dir + '/firstgraph.png', dpi=300)
plt.grid()
plt.show()
