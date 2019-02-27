from collections import Counter

def simple_set():
    l = ['a', 'e', 'i', 'o', 'u']
    s = frozenset(l)
    i = s.intersection(['a', 'e'])
    for e in i:
        print e

class Vowels:
    """Create a frozenset of vowels and does not allow add elements"""
    __vowels = frozenset(['a', 'e', 'i', 'o', 'u'])

    @classmethod
    def is_vowel(cls, *elems):
        """
            Check if all given elements are vowel
        """
        if cls.__vowels.intersection(list(elems)) == frozenset(elems):
            return True
        return False

    @classmethod
    def get_vowels_as_list(cls):
        return list(cls.__vowels)

class MultiSet:
    """
        Houses the implementation of dictionary of elements and their occurences
        example: m = MultiSet({'a': 100, 'b': 50})
                 m.get_count('a')      -> 100
                 m.get_highest()       -> ('a', 100)
                 m.get_highest_key()   -> 'a'
                 m.get_highest_value() -> 100
    """
    def __init__(self, dict_items):
        """
            Creates an instance of MultiSet class with initial

            :param  dict_items - Dictionary of items and their count
        """
        self.counter = Counter(dict_items)

    def add(self, new_dict):
        """Update a dictionary to the multiset"""
        self.counter.update(new_dict)

    def get_count(self, key):
        """Given a key return the count. 0 if key does not exists"""
        count = self.counter.get(key)
        if not count:
            count = 0
        return count

    def get_highest(self):
        """Returns a tuple of highest key and value"""
        return self.counter.most_common()[0]

    def get_highest_key(self):
        """Returns a highest key"""
        return self.counter.most_common()[0][0]

    def get_highest_value(self):
        """Returns a highest value"""
        return self.counter.most_common()[0][1]

    def __str__(self):
        """Give a string representation to an object"""
        return str(dict(self.counter))

if __name__ == '__main__':
    # simple_set()
    # print Vowels.is_vowel('a', 'e')
    # print Vowels.get_vowels_as_list()
    m = MultiSet({'a': 1})
    m.add({'b': 2})
    print (m)
    m.add({'a': 2})
    print (m)
    m.add({'a': 3})
    print (m)
    print
    # print(m.get_count('d'))

    print m.get_highest()

    m.add({'e': 100})
    print m.get_highest()
    print m.get_highest_key()
    print m.get_highest_value()
