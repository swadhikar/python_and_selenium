# Python program to terminate a thread using a global variable
import threading


def infinitizer():
    """Loops infinitely until dead is set to True"""
    global dead
    x = 0

    while not dead:
        x += 1

    print x


def main():
    global dead
    dead = False

    our_thread = threading.Thread(target=infinitizer, name='OurThread')
    our_thread.start()

    print our_thread.is_alive()
    print threading.enumerate()

    raw_input("Hit enter to terminate!")
    dead = True

    raw_input("Our thread is still running! Wait a bit and hit enter again to terminate!\n")
    print our_thread.is_alive()

    print threading.active_count()

if __name__ == '__main__':
    main()