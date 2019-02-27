from time import time
from threading import Thread
from queue import Queue

class ImageDownloader(Thread):
    def __int__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.number = 1

    def run(self):
        queue = self.queue
        image_url = queue.get()
        self.download_image(image_url, self.number)
        self.number += 1
        self.queue.task_done()  # Don't know what the heck is this

    def download_image(self, url, image_no):
        from urllib2 import urlopen

        image = urlopen(url)

        with open('./images/image_{}.jpg'.format(image_no), 'wb') as jpg:
            jpg.write(image.read())

        image.close()

def get_links():
    addr = 'http://www.behindwoods.com/tamil-movies/' \
           'baahubali-2/stills-photos-pictures/baahubali-2-stills-photos-pictures-{}.jpg'

    links = list()

    for i in xrange(255, 265):
        image = addr.format(i)
        links.append(image)

    return links

def main():
    timestamp = time()
    links = get_links()

    queue = Queue()

    # Create 4 threads
    for x in xrange(4):
        worker = ImageDownloader(queue)
        worker.daemon = True
        worker.start()

    # Put the tasks in the queue
    for link in links:
        print("Queuing link: '{}'".format(link))
        queue.put(link)

    # Make main to wait to wait for all threads to complete
    queue.join()

    print("Total time: {} seconds".format(timestamp - time()))


if __name__ == '__main__':
    main()