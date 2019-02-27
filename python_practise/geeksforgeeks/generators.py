def simple_even_generator(number):
    for n in range(2, number + 1, 2):
        yield n


def simple_odd_generator(number):
    for n in range(1, number + 1, 2):
        yield n


def squares_upto(max_number):
    for number in range(1, max_number + 1):
        for i in range(2, number):
            if number / i == i:
                yield number


if __name__ == '__main__':
    # for i in simple_even_generator(10):
    #     print(i)

    # for i in simple_odd_generator(100):
    #     print(i)

    for sq in squares_upto(1000):
        print(sq)
