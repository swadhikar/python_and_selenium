# Python array creation using numpy
# Ref: https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
# repl.it: https://repl.it/J1jL/15
import numpy as np 

array = np.zeros((3,3))
print(array)
print()

print("Array with 2 nos. of 3x4 array")
array = np.ones((2,3,4), dtype=np.int16)
print(array)
print(array.dtype)
print()

print("Create empty array")
array = np.empty((3,3))
print(array)
print(array.dtype)
print()

# arange is anologous to range function
print("Array created using 'arange' method")
array = np.arange(9).reshape(3,3)
print(array)
print(array.dtype)
print()

# arange for start to end increment by step
print("Create array with start, stop and step")
array = np.arange(2, 21, 2).reshape(2, 5)
print(array)
print("Total size:", array.size*array.itemsize,"bytes")
