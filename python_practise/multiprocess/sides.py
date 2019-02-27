from multiprocessing import Process
from time import time

squares = []


def calc_square(numbers):
    global squares
    for n in num
        bers:
        squares.append(n * n)
    print squares


if __name__ == '__main__':
    time_stamp = time()

    p_1 = Process(target=calc_square, args=(range(10),))
    p_1.start()
    p_1.join()

    print squares

    print("Completed in {} seconds!".format(time() - time_stamp))
