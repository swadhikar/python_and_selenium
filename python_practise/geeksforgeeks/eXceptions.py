def validate_int(function):
    def wrapper(*args):
        for arg in args:
            if type(arg) is not int:
                raise StringNotAllowedException(arg, 'integer addition')
        return function(*args)

    return wrapper


class StringNotAllowedException(Exception):
    def __init__(self, number, operation='undefined'):
        self.number = number
        self.__emsg = '"{}" is not a valid argument to perform: {}'.format(number, operation)

    def get_message(self):
        return '"{}" is of type: {}'.format(self.number, type(self.number))

    def __str__(self):
        return self.get_message()


class Addition:
    def __init__(self):
        pass

    @staticmethod
    @validate_int
    def add_numbers(num_1, num_2):
        return num_1 + num_2


print(Addition.add_numbers(10, 3))

# if __name__ == '__main__':
# try:
# r = Addition.add_numbers(1, 2)
# print(r)
# Addition.add_numbers(3, 1)
# Addition.add_numbers(1, 'a')
# r = Addition.add_numbers(10, 3)
# print(r)

# except StringNotAllowedException as se:
#     # print('ERROR:', se.get_message())
#     raise
