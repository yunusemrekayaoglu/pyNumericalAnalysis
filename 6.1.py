import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a)

#%%
a = np.zeros((4, 3))
print(a)

#%%
a = np.ones((4, 3)) * 3.54
print(a)

#%%
a = np.eye(3, 4)
print(a)

#%%

a = np.random.random(size = (4, 3))
print(a)

print(a[2])
print(a[2, 1])
print(a[:, 2])
#%%
a = np.random.randint(-5, 20, size = (4, 3))