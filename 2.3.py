import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * np.cos(x) + x ** 3 + 1

def df(x):
    
    return np.cos(x) - x * np.sin(x) + 3 * x ** 2

def f2(x):
    return x ** 2 - 5 * x + 6 

def f3(x):
    return x ** 2 - 4

def Newton(f, x0, Nmax = 100, tol = 1e-4): # Newton Raphson Yöntemi
    """ Newton Raphson Yöntemi İle Denklem Çözümü
    """
    
    for i in range(Nmax):
        x1 = x0 - f(x0) / df(x0)
        if np.abs(x1 - x0) < tol:
            break
        x0 = x1
    return x1
        
x = np.linspace(1, 4, 100)
y = f(x)
plt.plot(x,y)
plt.grid()

x0 = Newton(f, x0 = 1)

print("Fonksiyonun Kökü: {}".format(x0))
print("Kökün Fonksiyondaki Değeri: {}".format(f(x0)))