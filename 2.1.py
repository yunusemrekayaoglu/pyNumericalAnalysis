import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x * np.cos(x) + x ** 3 + 1

def f(x):
    return x ** 2 - 5 * x + 6
def IkiyeBolme(f, a, b, Nmax = 100, tol = 1e-4): #Yarılama Yöntemi
    """İkiye Bölme Yöntemi İle Denklem Çözümü
    """
    for i in range(Nmax):
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        
        if np.abs(b-a) < tol:
            break
        #print("i = {0:5.2f}\na = {0:5.2f}\nb = {0:5.2f}\nm = {0:5.2f}\nf(a) = {0:5.2f}\nf(b) = {0:5.2f}\nf(m)\n\n".format(i, a, b, m, f(a), f(b), f(m)))
        
    return (a + b) / 2
    
    
    
x = np.linspace(-2, 2, 100)
y = f(x)
plt.plot(x,y)
plt.grid()

x0 = IkiyeBolme(f, a = -2, b = 2, tol = 1e-8)

print("Fonksiyonun Kökü: {}".format(x0))
print("Kökün Fonksiyondaki Değeri: {}".format(f(x0)))