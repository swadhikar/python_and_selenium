import logging
import sys

from lib.variables import LOG_FILE


class LogUtil(object):
    def __init__(self):
        self._logger = logging.getLogger('PySelenium')
        _file_handle = logging.FileHandler(LOG_FILE)
        _formatter = logging.Formatter('%(asctime)-15s: %(levelname)-4s - %(message)s')
        _file_handle.setFormatter(_formatter)
        self._logger.addHandler(_file_handle)
        self._logger.setLevel(logging.DEBUG)

    def error(self, message):
        self._logger.error(message)

    def warn(self, message):
        self._logger.warn(message)

    def info(self, message):
        self._logger.info(message)


logUtil = LogUtil()


def write(message=""):
    """ Logs to the log file without timestamp and log levels """

    old_sysout = sys.stdout
    with open(LOG_FILE, 'a') as log_file:
        sys.stdout = log_file
        print message
    sys.stdout = old_sysout


def error(message):
    """ Log message as error """

    logUtil.error(message)


def info(message):
    """ Log message as information """

    logUtil.info(message)


def warn(message):
    """ Log message as warning """

    logUtil.warn(message)


if __name__ == '__main__':
    pass
