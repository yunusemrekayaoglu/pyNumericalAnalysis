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
            
            
p = [6, -5, 1]
q = [2, 3]
# 8 - 2x + x ** 2


print(Polymul(p, q))