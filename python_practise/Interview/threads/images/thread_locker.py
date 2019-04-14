from contextlib import contextmanager
from threading import Lock, Thread, current_thread
from time import sleep

# Run a function
# The function must be protected by thread lock
# After the function gets executed, the lock should be released

sum_of_values = 0


@contextmanager
def acquire_thread_lock():
    lock = Lock()
    try:
        lock.acquire()
        yield
    finally:
        lock.release()


def value_incrementer(num_times):
    with acquire_thread_lock():
        global sum_of_values
        for _ in range(num_times):
            sum_of_values += 1


if __name__ == '__main__':
    list_times = [4543, 3423, 2422, 1253, 6233, 5231]
    list_threads = list()

    print('Creating "{}" thread instances ...'.format(len(list_times)))
    for times in list_times:
        _thread = Thread(target=value_incrementer, args=(times,), name=str(times))
        list_threads.append(_thread)

    print('Starting thread instances ...')
    for _thread in list_threads:
        _thread.start()

    print('Started jobs. Waiting for completion ...')
    for _thread in list_threads:
        _thread.join()

    print('All threads has been completed!')
    print('Final sum:', sum_of_values)

    """
        Final sum: 45964493
        Final sum: 45964493
    """