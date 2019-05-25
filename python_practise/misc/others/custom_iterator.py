class PrimeNumberIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.__validate(start, end)
        self.__last_prime = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration

        if self.start == 2:
            prime_number = self.start
            self.start += 1
            return prime_number

        while self.start < self.end:
            if self.__is_prime_number(self.start):
                prime_number = self.start
                self.start += 1
                return prime_number
            self.start += 1
        else:
            raise StopIteration

    def __is_prime_number(self, number):
        self.__upper_limit = self.start // 2
        for divider in range(2, self.__upper_limit + 1):
            if number % divider == 0:
                return False
        return True

    @staticmethod
    def __validate(start, end):
        if start < 0 or end < 0:
            error = 'Negative number not allowed: ({}, {})'.format(start, end)
            raise ValueError(error)

        if end < start:
            error = 'starting number should be less than ending number: ({}, {})'.format(start, end)
            raise ValueError(error)
        

class OddNumberIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration

        if not self.__is_odd_number(self.start):
            self.start += 1

        odd_number = self.start
        self.start += 2

        return odd_number

    @staticmethod
    def __is_odd_number(number):
        return bool(number % 2)


if __name__ == '__main__':
    prime_itr = PrimeNumberIterator(1, 15)

    print(next(prime_itr))
    print(next(prime_itr))
    print(next(prime_itr))
    print(next(prime_itr))
    print(next(prime_itr))
    print(next(prime_itr))
    print(next(prime_itr))
    print(next(prime_itr))

    # for num in prime_itr:
    #     print(num)
