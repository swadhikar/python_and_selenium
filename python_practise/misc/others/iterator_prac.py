class EvenNoIterator:
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start > self.end:
            raise StopIteration()

        if self.start % 2:
            self.start += 1

        return self.start


class OddNoIterator:
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start >= self.end:
            raise StopIteration()

        if not self.start % 2:
            self.start += 1

        return self.start


class DivideByNIterator:
    def __init__(self, number, first, last):
        self.n = number
        self.first = first
        self.last = last
        self.first_factor = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.first_factor += 1

        if self.first_factor == 1 and self.first % self.n:
            while self.first % self.n:
                self.first += 1

        product = self.first_factor * self.first

        if product > self.last:
            raise StopIteration()

        return product


if __name__ == '__main__':
    # for n in EvenNoIterator(5, 10):
    #     print(n)
    #
    # print()
    #
    # for n in OddNoIterator(1, 10):
    #     print(n)
    #
    # print()
    #
    # for n in DivideByNIterator(12, 1, 100):
    #     print(n)
    n = EvenNoIterator(3, 13)

    while True:
        try:
            print(n.__next__())
        except StopIteration:
            break
