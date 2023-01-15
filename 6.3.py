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


a = np.random.randint(-10, 10, size = (3, 2))
b = np.random.randint(-10, 10, size = (3, 2))
c = a * b
print(a)
print(b)
print(c)

c = MatMul_e(a, b)
print(a)
print(b)
print(c)