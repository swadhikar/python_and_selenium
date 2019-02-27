class Fib:
    def __init__(self, end=None):
        self.a, self.b = 0, 1
        self.end = 10 if end is None else end


class FibItr(Fib):
    def __init__(self, end):
        super().__init__(end)

    def __iter__(self):
        for _ in range(self.end):
            self.a, self.b = self.b, self.a + self.b
            yield self.a


class FibGen(Fib):
    def __init__(self, end):
        super().__init__(end)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.end:
            raise StopIteration

        self.a, self.b, self.end = self.b, self.a + self.b, self.end - 1
        return self.a


if __name__ == '__main__':
    fib = FibItr(5)
    for i in fib:
        print(i, end=' ')
    print()
    for i in FibGen(5):
        print(i, end=' ')
