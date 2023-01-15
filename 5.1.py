import numpy as np
import matplotlib.pyplot as plt

def Polyval(p, x):
    """
    Bir polinomdaki bir x değerine karşılık gelen polinom değeri
    """
    m = len(x)
    n = len(p)
    y = 0
    for i in range(m):        
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

            
p = [6, -5, 1]
q = [2, 3]
# 8 - 2x + x ** 2


print(Polyder(p))
print(Polyint(p))

s = Polyder(p)
print(s)
w = Polyint(s)
print(w)