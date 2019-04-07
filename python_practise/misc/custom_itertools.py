import itertools


def basic_count():
    counter = itertools.count(5, step=-2.5)
    print(next(counter))
    print(next(counter))
    print(next(counter))
    print(next(counter))
    print(next(counter))


def count_example():
    counter = itertools.count(start=0, step=-1)
    data = [100, 200, 300, 400]
    daily_data = zip(counter, data)
    print(list(daily_data))
    daily_data_long = itertools.zip_longest(range(10), data)
    print(list(daily_data_long))


def simple_cycle():
    iterable = (1, 2, 3,)
    cycle_ref = itertools.cycle(iterable)

    print(next(cycle_ref))
    print(next(cycle_ref))
    print(next(cycle_ref))
    print(next(cycle_ref))
    print(next(cycle_ref))
    print(next(cycle_ref))


def switch_example():
    switch_cmds = ['On', 'Off']
    cycle_ref = itertools.cycle(switch_cmds)
    print(next(cycle_ref), end=', ')
    print(next(cycle_ref), end=', ')
    print(next(cycle_ref), end=', ')
    print(next(cycle_ref))


def simple_repeater():
    repeater = itertools.repeat(2)
    print(next(repeater))
    print(next(repeater))
    print(next(repeater))

    repeater = itertools.repeat(2, times=2)
    print(next(repeater))
    print(next(repeater))
    print(next(repeater))  # StopIteration will be raised at this point!
    print(next(repeater))


def square_repeater():
    squares = map(pow, range(10), itertools.repeat(2))
    print(list(squares))


def starmap():
    def fullname(first, last):
        return first.capitalize() + ' ' + last.capitalize()

    list_of_names = [
        ('swadhikar', 'chandramohan'),
        ('rajkumar', 's'),
        ('shenbaga', 'velraj')
    ]

    list_full_names = itertools.starmap(fullname, list_of_names)
    print(list(list_full_names))


def simple_chain():
    for item in itertools.chain(letters, numbers, parents):
        print(item, end=' ')
    """
        /usr/bin/python3.5 /home/swadhi/python_and_selenium/python_practise/misc/custom_itertools.py
        z y x 1 2 3 4 Corey Nicole
    """


def simple_slicer():
    result = itertools.islice(range_of_ten, 5)
    print(list(result))

    result = itertools.islice(range_of_ten, 1, 5)  # Start and end
    print(list(result))

    result = itertools.islice(range_of_ten, 1, 5, 2)  # Step by 2
    print(list(result))
    """
        [0, 1, 2, 3, 4]
        [1, 2, 3, 4]
        [1, 3]
    """


def log_slicer():
    log_file = 'logfile.log'

    with open(log_file, 'r') as f:
        header = itertools.islice(f, 3)
        for line in header:
            print(line, end='')


# Global vars
letters = ['z', 'y', 'x']
numbers = [1, 2, 3, 4]
parents = ['Corey', 'Nicole']
range_of_ten = range(10)


def main():
    pass
    # basic_count()
    # count_example()
    # simple_cycle()
    # switch_example()
    # simple_repeater()
    # square_repeater()
    # starmap()
    # simple_chain()
    # simple_slicer()
    log_slicer()


if __name__ == '__main__':
    main()
