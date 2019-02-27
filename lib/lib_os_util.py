# Python module to carry all the os related utilities
from lib_command import Command
from lib import variables
from log_util.logger import log
from time import sleep

from datetime import datetime


def capture_screen(path=None, filename='screen_print'):
    if not path:
        path = variables.SCREENSHOT_PATH

    filename = path + filename
    cmd = 'screencapture {}.png'.format(filename)

    sleep(1)

    if not Command.run(cmd):
        log.error("Failed to capture screen")
        return 0

    log.info("Captured screen: " + filename)
    return 1


def get_current_timestamp():
    return "{:%b_%d_%Y_%H_%M_%S}".format(datetime.now())


if __name__ == '__main__':
    for _ in xrange(4):
        print get_current_timestamp()
        sleep(3)
