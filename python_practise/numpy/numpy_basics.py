# Numpy basics
# repl.it: https://repl.it/J1jL/13
# Ref: https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

import numpy as np

a = np.arange(12).reshape(3, 4)

print("Array:\n",a)
print("Shape:", a.shape)
print("Dimensions:", a.ndim)
print("Array type:", type(a))
print("Datatype:", a.dtype)
print("Size of each element(Bytes):", a.itemsize)
print("Total size of array:", a.size)
print("Total size of this array:", a.size * a.itemsize)

# Lets create an array using numpy
print("\nNew array:")
b = np.array(range(4))
print(b)
print(type(b))

"""
Array:
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
Shape: (3, 4)
Dimensions: 2
Array type: <class 'numpy.ndarray'>
Datatype: int64
Size of each element(Bytes): 8
Total size of array: 12
Total size of this array: 96

New array:
[0 1 2 3]
<class 'numpy.ndarray'>
"""