import numpy as np
import matplotlib.pyplot as plt

def MatSum(a, b):
    m, n = a.shape
    c = np.zeros(a.shape)
    for i in range(m):
        for j in range(n):
            c[i, j] = a[i, j] + b[i, j]
    return c


def MatMul_e(a, b):
    m, n = a.shape
    c = np.zeros(a.shape)
    for i in range(m):
        for j in range(n):
            c[i, j] = a[i, j] * b[i, j]
    return c

def MatMul(a, b):
    m, pa = a.shape
    pb, n = b.shape
    c = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            for k in range(pa):
                c[i, j] += a[i, k] * b[k, j]
    return c
                
def MatTranspose(a):
    m, n = a.shape
    c = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            c[i, j] = a[j, i]
    return c

def MatDiag(a):
    m, n = a.shape
    c = np.zeros(min(m, n))
    for i in range(n):
        c[i] = a[i, i]
    return c


def MatMinor(a, I = 0, J = 0):
    m, n = a.shape
    c = np.zeros((m - 1, n - 1))
    ii = -1
    for i in range(m):
        if i == I:
            continue
        else:
            ii += 1
        jj = -1
        for j in range(n):
            if j == J:
                continue
            else:
                jj += 1
            c[ii, jj] = a[i, j]
        return c

def DetLaplace(a):
    n, _ = a.shape
    if n == 1:
        return a[0, 0]
    t = 0
    i = 0
    for j in range(n):
        M = MatMinor(a, i, j)
        t += (-1) ** (i + j) * a[i, j] * DetLaplace(M)
    return t


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



                
a = np.random.uniform(-1, 1, size = (10, 10))


print(np.linalg.det(a))

c = DetGauss(a)
print("Gauss det(a) : {}".format(c))