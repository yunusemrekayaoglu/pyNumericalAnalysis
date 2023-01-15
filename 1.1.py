import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x * np.cos(x) + x ** 3 + 1

x = np.linspace(-2, 2, 11)
y = f(x)

plt.plot(x, y, 'o-')
plt.grid()