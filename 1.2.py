import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x * np.cos(x) + x ** 3 + 1

x = -1
dx = 1e-5
y1 = np.abs(f(x))
while x < -0.5:
    y = np.abs(f(x))
    if y < y1:
        x1 = x
        y1 = y
    x += dx
    
    
print(x1, f(x1))
    