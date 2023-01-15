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



                
a = np.random.randint(-10, 10, size = (3, 2))
b = np.random.randint(-10, 10, size = (2, 3))
c = np.dot(a, b) # a@b
print(a)
print(b)
print(c)

c = MatTranspose(a, b)
print(a)
print(b)
print(c)