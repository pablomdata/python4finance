import numpy as np
a = np.array([0, 0.5, 1.0, 1.5, 2.0])
type(a)
a[:2]  # Slicing works as for lists

# Built in methods
a.sum()
a.std()
a.cumsum()
a.max()
a.argmax()

# Careful with np.max!
np.max(2, 0)
np.max(-2, 0)  # silent fail :) second argument is the axis
np.max(0, 2)  # fail
np.maximum(-2, 0)

# Vectorized operations: operations are applied to each element
a*2
a**2
np.sqrt(a)
np.log2(a+1)

b = np.array([a, a*2])
b

b.sum(axis=0)  # sum along axis 0 ==> columns
b.sum()
b.sum(axis=1)


eye = np.identity(4)
eye

np.ones_like(eye)
np.ones((2,3))

zeros = np.zeros((2,3,4))
zeros.shape
zeros[1]


# Optimized for speed!
import time
start = time.time()
acc = 0
for i in range(1000):
    for j in range(1000):
        acc += np.random.standard_normal()
end = time.time()
print("It took (ms): ", (end-start)*1000)

# Numpy outsources the loops to underlying C code for performance
# %timeit test = np.random.standard_normal((1000,1000)).sum()

# CODE VECTORIZATION
r = np.random.standard_normal((4,3))
s = np.random.standard_normal((4,3))
r+s

# Broadcasting
2*r+3 # same as 2*r+3*np.ones_like(r)

t = np.random.standard_normal(4)

r+t # does not work!
r + t.reshape(4, 1)
r.transpose()+t # same element-wise, different order


# Functions are applied element-wise.
def f(x):
    return 3*x+5


f(3)
f(r)

import math
math.sin(math.pi)
math.sin(r)  # Error: this function only takes real numbers!
np.sin(r)
type(np.sin)  # ufunc: universal function (works with arrays too)
