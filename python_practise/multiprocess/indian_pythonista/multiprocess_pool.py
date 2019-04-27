import multiprocessing
import os


def square(x):
    print('Processed by pid:', os.getpid())
    return x ** 2


i_list = [1, 2, 3, 4, 5, 6]

# Create a multiprocessing pool
m_pool = multiprocessing.Pool()

# Execute pool
r_list = m_pool.map(square, i_list)
print(r_list)
