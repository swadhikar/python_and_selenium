from time import time, sleep


def memoize_cubes(function):
    memory = {}

    def inner(num):
        if num not in memory:
            memory[num] = function(num)
        return memory[num]

    return inner


@memoize_cubes
def calculate_cube(number):
    sleep(0.25)
    return number ** 3


if __name__ == '__main__':
    start = time()

    r = calculate_cube(10)
    print(r)

    r = calculate_cube(1000)
    print(r)

    r = calculate_cube(10)
    print(r)

    r = calculate_cube(10)
    print(r)

    end = time()

    print('Run time:', end - start)
