"""Python program to post contents into fake fb wall and display the post in parallel"""
from multiprocessing import Queue, Process, current_process
from time import sleep


def wall(queue):
    """Monitor for posts and display it"""
    while True:
        if not queue.empty():
            # Unpack user and post
            user_name, post_name = queue.get()
            print("{user} has posted: {post}".format(user=user_name, post=post_name))


def post(content, queue):
    """Post contents into the wall"""
    sleep(0.1)
    user = current_process().name
    queue.put((user, content))


def main():
    """Main process"""
    queue = Queue()
    names = [None, 'Swadhikar', 'Srinath', 'Mohan', 'Nandini', 'Anand',
             'Poornima', 'Gurusankar', 'Maria', 'Rajesh', 'Raghu']

    # Start wall process
    w = Process(target=wall, args=(queue,))
    w.start()

    # Spawn post processes
    for _ in range(1, 11):
        p = Process(target=post, args=(str(_), queue), name=names[_])
        p.start()
        p.join()

    # Terminate monitoring process
    sleep(0.5)
    while w.is_alive():
        w.terminate()
        sleep(0.5)

    print("\n***Parallel Processes completed***")

if __name__ == '__main__':
    main()