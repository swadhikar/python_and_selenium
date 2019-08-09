from threading import (
    Thread,
    Lock,
    current_thread
)

from contextlib import contextmanager

num = 0


lock = Lock()

@contextmanager
def acquire_lock():
    lock.acquire()
    yield # Returns no objects
    lock.release()


def raise_num(times=0, by=1):
    with acquire_lock():
        global num
        for _ in range(times):
            num += 1
        print('num={}'.format(num))
    print('Number is raisEd for {} times by thread: "{}"'.format(times, current_thread().name))




if __name__ == '__main__':

    threads = [
        Thread(target=raise_num, args=[1000], name='t1'),
        Thread(target=raise_num, args=[2000], name='t2'),
        Thread(target=raise_num, args=[3000], name='t3'),
        Thread(target=raise_num, args=[4000], name='t4')
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
