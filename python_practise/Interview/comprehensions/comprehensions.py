# Python script to demonstrate use of various comprehensions
def lc_even_nos(limit):
    """list_comprehensions: Find the list of even integers in the given limit"""
    return [i for i in range(1, limit) if not i%2]


def lc_square_nos(start=1, limit=1):
    """list_comprehensions: Find the list of square of numbers in the given limit"""
    return [s**2 for s in range(start, limit)]


def sc_square_roots(start=1, limit=1):
    """set_comprehensions: Find the set of square roots of number in given limit"""
    return {s for s in range(start, limit) if int(s**0.5) == float(s**0.5)}


def dc_city_country():
    """Dictionary comprehension to map city and country"""
    cities = ['Chennai', 'New york', 'Sidney', 'Auckland']
    countries = ['India', 'USA', 'Australia', 'New Zealand']
    return {city: country for city, country in zip(cities, countries)}


def generator_object(list_of_numbers):
    """Decorator that has generator inner method"""
    def div_by_five():
        for num in list_of_numbers:
            if not num % 5:
                yield True
            else:
                yield False
    return div_by_five()


def gc_square(numbers):
    """Generator object returns all square nos. divisible by 10"""
    return ((n, n**2) for n in numbers if not n**2 % 10)


def main():
    # print lc_even_nos(11)
    # print lc_square_nos(start=5, limit=10)
    # print sc_square_roots(start=5, limit=100)
    # print dc_city_country()
    # for i in genera   tor_object(range(5, 26)): print i
    for sq in gc_square(range(1, 201)): print sq

if __name__ == '__main__':
    main()