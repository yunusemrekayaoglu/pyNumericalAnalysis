import numpy as np
import matplotlib.pyplot as plt

def Polyval(p, x):
    m = len(x)
    n = len(p)
    y = 0
    for i in range(m):        
        for j in range(n):
            y += p[j] * x ** j
    return y

p = [6, -5, 1]
# 6 - 5 * 4 + 4 ** 2

x = np.array([4, 3, 8, 6, 9, 12])
y = Polyval(p, x)
print("x: {}\nP(x): {}".format(x, y))


#%%

x1 = np.linspace(0, 5, 100)
y1 = Polyval(p, x)

plt.plot(x1, y1)
plt.grid(True)