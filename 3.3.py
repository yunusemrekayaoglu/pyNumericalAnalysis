import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * np.cos(x) + x ** 3 + 1

def f2(x):
    return x ** 2 - 5 * x + 6

def g2(x):
    return (x ** 2 + 6) / 5    

def f3(x):
    return x ** 2 - 4
    

def FixedPoint(f, g, x0, Nmax = 1000, tol = 1e-4): 
    """
    Sabit Nokta ile Denklem Çözümü
    """
    for i in range(Nmax):
        
        x1 = g(x0)
        if np.abs(f(x1)) < tol:
            break
        print("{:5.2f} {:5.2f} {:5.2f} {:5.2f}\n".format(x0, x1, f(x0), f(x1)))
        
        x0 = x1
    return x1

x = np.linspace(-4, 4, 100)
y = f(x)
plt.plot(x,y)
plt.grid(1)

x0 = FixedPoint(f2, g2, x0 = 1)

print("Fonksiyonun Kökü: {}".format(x0))
print("Kökün Fonksiyondaki Değeri: {}".format(f(x0)))
        