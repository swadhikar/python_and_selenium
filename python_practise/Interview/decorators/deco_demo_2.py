# Python script to capitalize underscore separated string using decorators
import time


def another_function():
    print('another function')


def turn_into_another_function(fnc):
    return another_function


@turn_into_another_function
def a_function():
    print('a function')


# a = turn_into_another_function(a_function)
# a_function()


# print(camelcase_name_list)
def timer(fnc):
    """
        Takes in a function and runs and prints the time it took
        to run the method

        @param      fnc     function to run
    """

    def wrapper(*fnc_args):
        t1 = time.time()
        fnc(*fnc_args)
        t2 = time.time()
        print('Function "{}" took "{}" time'.format(fnc.__name__, t2 - t1))

    return wrapper


def sleep_decorator(fnc):
    """
        Limits how fast the function is
        called
    """
    def inner(*args, **kwargs):
        time.sleep(1)
        fnc(*args, **kwargs)

    return inner


def mapper(fnc):
    def inner(list_of_values):
        return [fnc(value) for value in list_of_values]

    return inner


@mapper
def camelcase(s):
    return ''.join([c.capitalize() for c in s.split('_')])


# @timer
@sleep_decorator
def wait(n):
    time.sleep(n)


# name_list = ['export_endpoints()', 'validate_inputs()', 'configure_smtp_server()']
# camelcase_name_list = camelcase(name_list)

wait(1)
