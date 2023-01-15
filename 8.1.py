import numpy as np
import matplotlib.pyplot as plt


def DetGauss(A):
    a = np.copy(A)
    n, _ = a.shape
    for k in range(n - 1): # Tuttuğumuz satır
        for i in range(k + 1, n): # Yok edilen satır
            p = a[i, k] / a[k, k]
            for j in range(k, n):
                a[i, j] -= p * a[k, j]
    t = 1
    for i in range(n):
        t *= a[i, i]
    return t



def Cramer(a, b):
    n, _ = a.shape
    x = np.zeros(n)
    detA = DetGauss(a)
    for i in range(n):
        Ai = np.copy(a)
        Ai[:, i] = b.copy()
        x[i] = DetGauss(Ai) / detA
    return x



n = 5                
a = np.random.uniform(-2, 2, size = (n, n))
xx = np.random.randint(-10, 10, size = (n))
b = np.dot(a, xx)


print(a)
print(xx)
print(b)
x = Cramer(a, b)
print(x)