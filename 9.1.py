import numpy as np
import matplotlib.pyplot as plt


def Lu(a):
    """
    Lu Ayrıştırma Yöntemi
    """
    
    n, _ = a.shape
    L = np.eye(n)
    U = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i <= j:
                U[i, j] = a[i, j]
                for k in range(i - 1):
                    U[i, j] -= L[i, k] * U[k, j]
            else:
                L[i, j] = a[i, j]
                for k in range(j -1):
                    L[i, j] -= L[i, k] * U[k, j]
                L[i, j] /= U[i, j]
    return L, U

def DetLu(a):
    """
    Lu ayrıştırma yaklaışımı ile determinant Çözümü
    """
    n, _ = a.shape
    L, U = Lu(a)
    d = 1
    for i in range(n):
        d *= U[i, j]
    return d

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


def Gauss(a, b):
    """
    Gauss Eleme Yöntemi
    """
    n, _ = a.shape
    
    #a matrisinin alt üçgeni sıfırlanır
    for k in range(n - 1): # Tuttuğum satır
        for i in range(k + 1, n): # Yok edilen satır
            p = a[i, k] / a[k, k]
            for j in range(k, n): # İşlem yapılan sütun
                a[i, j] -= p * a[k, j]
            b[i] -= p * b[k]
    # Yukarı doğru işlem yaparak çözümleri bulunur
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        t = b[i]
        for j in range(i + 1, n):
            t -= a[i, j] * x[j]
        x[i] = t / a[i, i]
    return x


def LuSolve(a, b):
    n, _ = a.shape
    L, U = Lu(a.copy())
    y = np.zeros(n)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i, j] *y[j]
            
    # Yukarı doğru işlem yaparak çözümleri bulunur
    x = np.zeros(n)
    for i in range(n -1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]
    return x
            


n = 5
a = np.random.uniform(-2, 2, size = (n, n))
xx = np.random.randint(-10, 10, size = (n, ))
b = np.dot(a, xx)

print(a)
print(xx)
print(b)
x = LuSolve(a.copy(), b)
print(x)