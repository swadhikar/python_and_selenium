from multiprocessing import Pool
from time import time


def squarer():
    s = 0
    for i in range(100):
        s += i*i
    return s


if __name__ == '__main__':
    timestamp = time()
    p = Pool(processes=4)
    result = p.map(squarer, range(1000000))
    p.close()
    p.join()

    print("Pool processing took: {} secs".format(time() - timestamp))

    t2 = time()
    result = []

    # Perform complex mathematical operations
    for x in range(1000000):
        result.append(squarer(x))

    print("Serial processing took: {} secs".format(time() - t2))