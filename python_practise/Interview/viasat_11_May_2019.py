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
        commands = """\
show application status
show tech-support
start application ise 
stop application ise\
"""

    pattern = re.compile(r'^{}.*'.format(cli_start), re.MULTILINE)

    for itr, command in enumerate(pattern.findall(PatternMapper.commands)):
        if itr == 0:
            print('Did you try to type in command:')
        print('    ' + command)

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
    # Output:
    #
    # 53736BOA
    # 7678SWA


def remove_reference_chars(in_string, reference_str):
    pattern = r'[' + reference_str + ']'
    return re.sub(pattern, '', in_string)


if __name__ == '__main__':
    # Question: 1 - Find nth prime number
    # r = is_prime(5)
    # print(r)
    # 2, 3, 5, 7, 11, 13
    n_th = get_n_th_prime(100)
    print(n_th)
    """
    /usr/bin/python3.6 /home/swadhi/python_and_selenium/python_practise/Interview/viasat_11_May_2019.py
    541
    """

    # Question 2: Auto-suggest engine
    user_input = input('Enter a command (q or quit to exit): ')

    while user_input.lower() not in ('q', 'quit'):
        auto_suggest_engine(user_input)
        user_input = input('Enter a command (q or quit to exit): ')
    """
    Enter a command (q or quit to exit): s
    Did you try to type in command:
        show application status
        show tech-support
        start application ise 
        stop application ise
    
    Enter a command (q or quit to exit): sh
    Did you try to type in command:
        show application status
        show tech-support
    
    Enter a command (q or quit to exit): st
    Did you try to type in command:
        start application ise 
        stop application ise
    
    Enter a command (q or quit to exit): sto
    Did you try to type in command:
        stop application ise
    
    Enter a command (q or quit to exit): sta
    Did you try to type in command:
        start application ise 
    
    Enter a command (q or quit to exit): q
    """

    # Question 3: OTP generator
    otp = generate_otp(5, 'BOA')
    print(otp)

    otp = generate_otp(4, 'SWA')
    print(otp)
    """
    Output:
        53736BOA
        7678SWA
    """

    # Question 4: How would you remove a series of characters passed
    # as reference from a given string?
    input_text = 'Hello world, this is awesome!'
    reference = 'aeiou'
    r = remove_reference_chars(input_text, reference)
    print(r)
    """
        Output: 
        Hll wrld, ths s wsm!
    """
