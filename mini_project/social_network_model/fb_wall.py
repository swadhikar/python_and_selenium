"""Python program to post contents into fake fb wall as a file and display the post in parallel"""
from multiprocessing import Process
from subprocess import check_output
from fb_util import User, FileMonitor

posts_dict = {}
separator = ","
posts_file = "fb_posts.txt"
file_monitor = FileMonitor(posts_file)


def wall():
    """Monitor for posts from a file and display it"""
    while True:
        if file_monitor.monitor():
            post_name = check_output('tail -1 {}'.format(posts_file), shell=True)
            if not post_name:
                continue

            user_name, post_name = post_name.split(separator.lstrip('\n'))
            if post_name in posts_dict:
                continue

            posts_dict[post_name] = 1

            print("{user} has posted: {post}".format(user=user_name, post=post_name))


def main():
    """Main process"""
    # Clean up file
    open(posts_file, 'w').close()

    # Login user
    user = User()
    if not user.login():
        return 0

    # Monitor posts
    w = Process(target=wall)
    w.start()


if __name__ == '__main__':
    main()
