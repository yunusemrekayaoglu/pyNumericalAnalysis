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

def Polysum(p, q):
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
p = [6, -5, 1]
q = [2, 3]
# 8 - 2x + x ** 2


print(Polysum(p, q))