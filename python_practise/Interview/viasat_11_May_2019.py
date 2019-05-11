import re
import time
import random


class Timer:
    def __init__(self, last_updated=None):
        self.__last_updated = last_updated

    def update_time(self, time_):
        self.__last_updated = time_

    def get_last_update(self):
        return self.__last_updated


def get_n_th_prime(n):
    """How would you find n_th prime number"""

    def is_prime(number):
        if number == 1:
            return False
        for n in range(2, number):
            if not number % n:
                return False
        return True

    start = 2
    n_th = 1

    while True:
        start += 1
        if is_prime(start):
            n_th += 1
            if n_th == n:
                return start


def auto_suggest_engine(cli_start):
    class PatternMapper:
        patterns = {
            re.compile('sh.*'): ['show application status', 'show tech-support'],
            re.compile('st.*'): ['stop application ise', 'start application ise'],
            re.compile('sta.*'): ['start application ise'],
            re.compile('sto.*'): ['stop application ise'],
        }

    for pattern in PatternMapper.patterns:
        if pattern.search(cli_start):
            print('Did you try to type in command:')
            for suggestion in PatternMapper.patterns[pattern]:
                print('    ' + suggestion)
    print()


class GeneratedOTP:
    OTP_LIST = list()


def generate_otp(length=5, suffix=None):
    # timer = Timer()

    def get_range(size):
        return int('1' + '0' * (size - 1)), int('9' * size)

    # Generate logic
    start, end = get_range(length)
    random_str = str(random.randrange(start, end))

    if random_str in GeneratedOTP.OTP_LIST:
        print('OTP already exists. Regenerating ...')
        return generate_otp(length, suffix)

    GeneratedOTP.OTP_LIST.append(random_str)
    if suffix is not None:
        random_str += suffix

    return random_str


if __name__ == '__main__':
    # Question: 1 - Find nth prime number
    # r = is_prime(5)
    # print(r)
    # 2, 3, 5, 7, 11, 13
    n_th = get_n_th_prime(100)
    print(n_th)

    # Question 2: Auto-suggest engine
    user_input = input('Enter a command (q or quit to exit): ')

    while user_input.lower() not in ('q', 'quit'):
        auto_suggest_engine(user_input)
        user_input = input('Enter a command (q or quit to exit): ')

    # Question 3: OTP generator
    otp = generate_otp(5, 'BOA')
    print(otp)

    otp = generate_otp(4, 'SWA')
    print(otp)
