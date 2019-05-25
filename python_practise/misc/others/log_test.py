from log_util.logger import log


def add(a, b):
    return a + b


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    try:
        res = x / y
    except ZeroDivisionError:
        log.exception("Division by zero")
    else:
        return res

if __name__ == '__main__':
    x = 10
    y = 0

    log.debug("Add: {} + {} = {}".format(x, y, add(x, y)))
    log.debug("Sub: {} - {} = {}".format(x, y, sub(x, y)))
    log.debug("Mul: {} * {} = {}".format(x, y, mul(x, y)))
    log.exception("Div: {} / {} = {}".format(x, y, div(x, y)))
    log.info("Simple calculator successfully implemented!")
