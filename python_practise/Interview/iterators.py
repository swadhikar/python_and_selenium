
class PassMarkIterator(object):
    pass_mark = 40

    def __init__(self, __dictionary):
        self.__dictionary = __dictionary
        self.__index = -1
        self.__pass = list()
        self.generate_pass()

    def __iter__(self):
        return self

    def generate_pass(self):
        __dictionary = self.__dictionary
        for student in __dictionary:
            if __dictionary[student] >= 40:
                self.__pass.append((student, __dictionary[student]))

    def next(self):
        self.__index += 1
        if self.__index < len(self.__pass):
            return self.__pass[self.__index]
        else:
            raise StopIteration

class FailMarkIterator(object):
    pass_mark = 40

    def __init__(self, __dictionary):
        self.__dictionary = __dictionary
        self.__index = -1
        self.__pass = list()
        self.generate_pass()

    def __iter__(self):
        return self

    def generate_pass(self):
        __dictionary = self.__dictionary
        for student in __dictionary:
            if __dictionary[student] < 40:
                self.__pass.append((student, __dictionary[student]))

    def next(self):
        self.__index += 1
        if self.__index < len(self.__pass):
            return self.__pass[self.__index]
        else:
            raise StopIteration


if __name__ == '__main__':
    p = PassMarkIterator({'Swadhi': 40, 'Mohan': 80, 'Nandini': 70, 'Raghu': 30, \
                          'Gowtham': 35, 'Arul': 76})

    print "Passed:"
    try:
        for i in xrange(10):
            print p.next()
    except StopIteration:
        pass

    print "Failed:"
    f = FailMarkIterator({'Swadhi': 40, 'Mohan': 80, 'Nandini': 70, 'Raghu': 30, \
                          'Gowtham': 30, 'Arul': 76})

    try:
        for i in xrange(10):
            print f.next()
    except StopIteration:
        pass
