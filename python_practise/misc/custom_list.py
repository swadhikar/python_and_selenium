def check_integer(function):
    def wrapper(self, *args):
        if type(args[-1]) is not int:
            raise ValueError('Expected integer value to add. "{}" is not an integer'.format(args[-1]))
        function(self, *args)

    return wrapper


def validate_list(function):
    def wrapper(self, sequence=[]):
        if not all(map(lambda x: type(x) is int, sequence)):
            raise ValueError('Expected all integers in the sequence:', sequence)
        function(self, sequence)

    return wrapper


class IntegerList(list):
    """"Custom list that allows only integer values"""

    @validate_list
    def __init__(self, in_sequence=[]):
        super().__init__(in_sequence)

    @check_integer
    def append(self, value):
        super().append(value)

    @check_integer
    def insert(self, index, value):
        super().insert(index, value)

    @validate_list
    def extend(self, in_list):
        super().extend(in_list)


if __name__ == '__main__':
    int_list = IntegerList([-2, -1])
    int_list.append(1)
    int_list.append(2)
    int_list.append(3)
    int_list.insert(2, 0)
    int_list.extend([8, 9, 10])
    print(int_list)
