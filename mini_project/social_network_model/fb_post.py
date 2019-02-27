"""Python program to post contents into fake fb wall as a file and display the post in parallel"""
from fb_util import FileMonitor
from time import sleep

posts_dict = {}
posts_file = "fb_posts.txt"
file_monitor = FileMonitor(posts_file)


def post(username):
    """Post contents into the wall"""
    content = raw_input("Enter something to post: >> ")
    content = "{user},{content}\n".format(user=username, content=content)

    with open(posts_file, 'a') as post_obj:
        sleep(0.1)
        post_obj.write(content)


def main():
    """Main process"""
    # Clean up file
    open(posts_file, 'w').close()

    i = 0
    names = ['Swadhikar', 'Gurusankar', 'Maria', 'Rajesh', 'Raghu']

    while True:
        sleep(0.2)
        post(names[i % len(names)])
        i += 1

if __name__ == '__main__':
    main()
