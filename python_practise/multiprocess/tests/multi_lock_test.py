from multiprocess import Lock, Process


def f(lock, num):
    lock.acquire()
    print 'Hello world: {}'.format(num)
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    
    for num in range(10):
        p = Process(target=f, args=(lock, num))
        p.start()
        p.join()    # To print in sequential order
    # for