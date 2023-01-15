import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * np.cos(x) + x ** 3 + 1

def f2(x):
    return x ** 2 - 5 * x + 6
    
def f3(x):
    return x ** 2 - 4
    

def RegulaFalse(f, a, b, Nmax = 1000, tol = 1e-4): 
    """
    Regula False ile Denklem Çözümü
    """
    for i in range(Nmax):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if np.abs(f(c)) < tol:
            break
        print("{:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}\n".format(a, b, c, f(a), f(b), f(c)))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c


x = np.linspace(-4, 4, 100)
y = f(x)
plt.plot(x, y)
plt.grid(1)

a = RegulaFalse(f, a = 1, b = 2, tol = 1e-12)

print("Fonksiyonun Kökü: {}".format(a))
print("Kökün Fonksiyondaki Değeri: {}".format(f(a)))