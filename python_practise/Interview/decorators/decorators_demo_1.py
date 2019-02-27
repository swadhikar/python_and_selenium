from time import time, sleep
from mini_project.social_network_model.fb_util import PasswordManager


def timer(func):
    """Decorator function to print the execution time of method decorated"""
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print("{} took {} seconds".format(func.__name__, end - start))
    return wrapper


@timer
def calc_square(numbers):
    squares = list()
    for number in numbers:
        squares.append(number**2)
    return squares


@timer
def wait_function(count):
    for i in range(count):
        sleep(0.1)


@timer
def create_user():
    user = PasswordManager()
    user.create_user()

if __name__ == '__main__':
    for _ in xrange(5):
        # calc_square(xrange(100000))
        wait_function(_)
        # create_user()