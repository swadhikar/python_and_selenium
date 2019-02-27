#! /usr/bin/python
from python.log_util.logger import log
from contextlib import contextmanager
import os


@contextmanager
def change_directory(destination):
    """Context manager to change directory back and forth"""
    cwd = os.getcwd()
    try:
        os.chdir(destination)
        log.info('switched to directory: ' + destination)
        yield
    finally:
        os.chdir(cwd)
        log.info('switched back to original directory: ' + cwd)


@contextmanager
def write_file(filename):
    f = None
    try:
        f = open(filename, 'w')
        yield f
    finally:
        if f:
            f.close()
            log.info('File closed: ' + filename)


if __name__ == '__main__':
    dest = '/home/swadhi/Documents/AWS/aws_notes'
    with change_directory(dest):
        ls_root = os.listdir('.')
        log.info("Contents of directory '{}': ".format(dest))
        [log.debug('  >>> ' + ls) for ls in sorted(ls_root)]

    filename = '/tmp/test.txt'
    with write_file(filename) as file:
        file.write('Swadhikar Chandramohan\n')
        log.info(f'Written line to file: {filename}')

"""
Output:

/usr/bin/python3.6 /home/swadhi/PycharmProjects/pyselenium/python/python_practise/context_manager/cm_func.py
2017-12-24 09:16:31,992: INFO  - switched to directory: /home/swadhi/Documents/AWS/aws_notes
2017-12-24 09:16:31,992: INFO  - Contents of directory '/home/swadhi/Documents/AWS/aws_notes': 
2017-12-24 09:16:31,992: DEBUG -   >>> .git
2017-12-24 09:16:31,992: DEBUG -   >>> dec_03.txt
2017-12-24 09:16:31,992: DEBUG -   >>> dec_10.txt
2017-12-24 09:16:31,992: DEBUG -   >>> nov_12.txt
2017-12-24 09:16:31,992: DEBUG -   >>> nov_19.txt
2017-12-24 09:16:31,992: DEBUG -   >>> nov_26.txt
2017-12-24 09:16:31,993: DEBUG -   >>> oct_08.txt
2017-12-24 09:16:31,993: DEBUG -   >>> oct_15.txt
2017-12-24 09:16:31,993: DEBUG -   >>> oct_21.txt
2017-12-24 09:16:31,993: DEBUG -   >>> oct_29.txt
2017-12-24 09:16:31,993: DEBUG -   >>> reference_notes.txt
2017-12-24 09:16:31,993: DEBUG -   >>> sep_16.txt
2017-12-24 09:16:31,993: DEBUG -   >>> sep_24.txt
2017-12-24 09:16:31,993: DEBUG -   >>> sep_24_2017.txt
2017-12-24 09:16:31,993: INFO  - switched back to original directory: /home/swadhi/PycharmProjects/pyselenium/python/python_practise/context_manager
2017-12-24 09:16:31,993: INFO  - Written line to file: /tmp/test.txt
2017-12-24 09:16:31,993: INFO  - File closed: /tmp/test.txt

Process finished with exit code 0

"""