# Pass mark generator
from time import sleep

class PassFailGenerator(object):
    """ Takes in a dictionary of student name and marks and returns a generator \
        of passed and failed candidates"""
    pass_mark = 40

    def __init__(self, dictionary):
        self.__dictionary = dictionary
        self.__pass = None
        self.__fail = None

    def generate_pass(self):
        __dictionary = self.__dictionary
        self.__pass = ((k, __dictionary[k]) for k in __dictionary if __dictionary[k] >= 40)
        for item in self.__pass:
            yield item

    def generate_fail(self):
        __dictionary = self.__dictionary
        self.__fail = ((k, __dictionary[k]) for k in __dictionary if __dictionary[k] < 40)
        for item in self.__fail:
            yield item

if __name__ == '__main__':
    p = PassFailGenerator({'Swadhi': 40, 'Mohan': 80, 'Nandini': 70, 'Raghu': 30, \
                          'Gowtham': 35, 'Arul': 76})
    g = p.generate_pass()
    try:
        for i in range(100000):
            print g.next()
            sleep(0.5)
    except StopIteration:
        pass

    print

    f = p.generate_fail()
    try:
        for i in range(100000):
            print f.next()
            sleep(0.5)
    except StopIteration:
        pass
