import numpy as np
import matplotlib.pyplot as plt

def Polyval(p, x):
    """
    Bir polinomdaki bir x değerine karşılık gelen polinom değeri
    """
    n = len(p)
    y = 0
    for j in range(n):
        y += p[j] * x ** j
    return y

def Polysum(p, q):
    """
    İki polinomun toplamını yapan fonksiyon
    """
    m = len(p)
    n = len(q)
    k = max(m, n)
    s = np.zeros(k)
    for i in range(k):
        if i < m:
            s[i] += p[i]
        if i < n:
            s[i] += q[i]
    return s

def Polymul(p, q):
    """
    İki polinomun çarpımını yapan fonksiyon
    """
    m = len(p)
    n = len(q)
    k = m + n - 1 
    s = np.zeros(k)
    for i in range(k):
        for j in range(m):
            if 0 <= (i - j) < n:
                s[i] += p[j] * q[i - j]            
            
    return s     




def Polyder(p):
    """
    Verilen bir polinomun türevinin katsayılarını bulur
    """
    m = len(p)
    s = np.zeros(m - 1)
    for i in range(m - 1):
        s[i] = p[i + 1] * (i + 1)
    return s


def Polyint(p):
    """
    Verilen bir polinomun integralinin katsayılarını bulur
    """
    m = len(p)
    s = np.zeros(m + 1)
    for i in range(1, m + 1):
        s[i] = p[i - 1] / i
    return s


def Poly(r):
    """
    Kökleri verilen bir polinomun katsayılarının bulunması
    """
    n = len(r)
    p = [-r[0], 1]
    for i in range(1, n):
        q = [-r[i], 1]
        p = Polymul(p, q)
    return p


def Polydiv(p, r):
    n = len(p)
    s = []
    t = 0
    for i in range(n - 1, 0, -1):
        s.append(p[i] + r * t)
        t = p[i] + r * t
    return s[::-1]

def  Newton(p, x0, Nmax = 100, tol = 1e-4):
    """
    Newton Raphson Yöntemi ile denklem çözümü
    """
    q = Polyder(p)
    for i in range(Nmax):
        x1 = x0 - Polyval(p, x0) / Polyval(q, x0)
        if np.abs(x1 - x0) < tol:
            break
        x0 = x1
    return x1
def Roots(p):
    n = len(p)
    r = np.zeros(n - 1)
    for i in range(n - 1):
        r[i] = Newton(p, 1)
        p = Polydiv(p, r[i])
    return r
    
r = np.random.randint(-5, 5, size = 6)
print(r)
p = Poly(r)
print(p)
rr = Roots(p)
print(rr)