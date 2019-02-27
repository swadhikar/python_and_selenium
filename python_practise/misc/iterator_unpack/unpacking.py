from python.python_practise.misc.my_generator.i_generator import Fibonacci


def tuple_unpack():
    i_tuple = 'name', 'company', 'age'
    name, *_ = i_tuple
    print(name)
    print(_)


def i_generator():
    yield 1
    yield 'swadhikar'
    yield 7


def generator_unpack():
    i, name, i = i_generator()
    print(name)
    print(i)


if __name__ == '__main__':
    # tuple_unpack()
    # generator_unpack()
    for i in Fibonacci():
        print(i)
    print()

    *rest, last = Fibonacci()
    print(last)
    print(rest)