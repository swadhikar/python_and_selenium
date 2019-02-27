# Python array creation using numpy
# Ref: https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
# repl.it: https://repl.it/J1jL/13
import numpy as np 

l = [1,2,3,4]
ar = np.array(l)
print(ar)
print(ar.dtype)

l = [(1.2, 2.1, 3.4,), (4.0, 5.2, 6.4)]
ar1 = np.array(l, dtype=complex)
# ar1.reshape(3, 2)
print(ar1)
print(ar1.dtype)

"""
[1 2 3 4]
int64
[[ 1.2+0.j  2.1+0.j  3.4+0.j]
 [ 4.0+0.j  5.2+0.j  6.4+0.j]]
complex128
"""