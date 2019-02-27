import threading
from time import sleep


def print_it(arg):
    print "{} says {}\n".format(threading.current_thread(), arg)
    sleep(5)


def main():

    our_thread = threading.Thread(target=print_it, args=('Welcome to python',), name='print_it')
    our_thread.start()

    print "Active threads: " + str(threading.active_count())
    # print threading.enumerate()
    print "Current Thread: " + str(threading.current_thread())


if __name__ == '__main__':
    main()