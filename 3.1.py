import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * np.cos(x) + x ** 3 + 1

def f2(x):
    return x ** 2 - 5 * x + 6
    
def f3(x):
    return x ** 2 - 4
    

def secant(f, x0, x1, Nmax = 1000, tol = 1e-4): 
    """
    Sekant Yöntemi
    """
    for i in range(Nmax):
        x2 = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
        if np.abs(f(x2)) < tol:
            break
        print("{:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}\n".format(x0, x1, x2, f(x0), f(x1), f(x2)))
        x0 = x1
        x1 = x2
    return x2


x = np.linspace(-4, 4, 100)
y = f(x)
plt.plot(x, y)
plt.grid(1)

x0 = secant(f, x0 = 1, x1 = 2, tol = 1e-12)

print("Fonksiyonun Kökü: {}".format(x0))
print("Kökün Fonksiyondaki Değeri: {}".format(f(x0)))