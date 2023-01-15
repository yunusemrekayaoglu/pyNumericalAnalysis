import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x) - x ** 2

def RegulaFalse(f, a, b, Nmax = 1000, tol = 1e-4):
    """
    a Yöntemi ile Denklem Çözümü
    """
    
    for i in range(Nmax):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if np.abs(f(c)) < tol:
            break
        print("{:5.2f} {:5.2f} {:5.2f} {:5.2f} {:5.2f} {:5.2f} \n".format(a, b, c, f(a), f(b), f(c)))
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        return c

x = np.linspace(-4, 4, 100)
y = f(x)
plt.figure()
plt.plot(x, y)

x0 = RegulaFalse(f, a = 1, b = 2, tol = 1e-6)

print("Fonksiyonun Kökü: {}".format(x0))
print("Kökün Fonksiyondaki Değeri: {}".format(f(x0)))