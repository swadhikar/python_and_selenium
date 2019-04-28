import os
from threading import Thread, current_thread, Lock


def first_method():
    def show():
        print('This is a child thread')

    t = Thread(target=show())
    t.start()
    print('This is main thread ...')


def second_method():
    class MyThread(Thread):
        def run(self):
            for _ in range(5):
                print('--- for loop inside run method ---')

    t = MyThread()
    t.start()
    print('*** Threads started ***')
    for _ in range(5):
        print('--- This is main thread ---')


def print_cube(num):
    print(f'Executed "{current_thread().name}" by process id: {os.getpid()}')
    print('Cube: {}'.format(num ** 3))


def print_square(num):
    print(f'Executed "{current_thread().name}" by process id: {os.getpid()}')
    print('Square: {}'.format(num ** 2))


def thread_it_show_pid(num=3):
    threads = [
        Thread(target=print_cube, args=(num,), name='Cube Thread'),
        Thread(target=print_square, args=(num,), name='Square Thread')
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


x = 0


def incrementer(thread_lock):
    global x
    thread_lock.acquire()
    x += 1
    thread_lock.release()


def increment_task(n_times, thread_lock):
    for _ in range(n_times):
        incrementer(thread_lock)


def manipulate_x():
    global x

    x = 0
    times = 20_000
    lock_ = Lock()

    threads = (
        Thread(target=increment_task, args=(times, lock_)),
        Thread(target=increment_task, args=(times, lock_)),
    )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    # first_method()
    # second_method()
    # thread_it_show_pid()
    manipulate_x()
