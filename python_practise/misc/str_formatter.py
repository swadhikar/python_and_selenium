person = {'name': 'Swadhikar', 'age': 27}
my_list = ['Swadhikar', 27]


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def method_1():
    """
        Formatting with default placeholders
    """
    sentence = "My name is {} and my age is {}".format(person['name'], person['age'])
    print sentence


def method_2():
    """
        Formatting with indexed place holders
    """
    sentence = "My name is {0} and my age is {1}".format(person['name'], person['age'])
    print sentence


def method_3():
    """
        Formatting with indexed placeholders explained
    """
    tag = "h1"
    text = "This is a headline"

    sentence = "<{0}>{1}</{0}>".format(tag, text)
    print sentence


def method_4():
    """
        Formatting dictionary with indexed placeholders
    """
    sentence = "My name is {0[name]} and my age is {0[age]}".format(person)
    print sentence


def method_5():
    """
        Formatting list with indexed placeholders
    """
    sentence = "My name is {0[0]} and my age is {0[1]}".format(my_list)
    print sentence


def method_6():
    """
        Formatting with instance variables
    """
    p1 = Person('Jack', '33')

    sentence = "Hello I am {0.name}!, {0.age} years old".format(p1)
    print sentence

    p2 = Person("Peter", '28')

    sentence = "Hello I am {0.name}!, {0.age} years old".format(p2)
    print sentence


def method_7():
    """
        Formatting with keywords
    """
    sentence = "Hello I am {name} and {age} years old!".format(name="Jenn", age="23")
    print sentence


def method_8():
    """
        Formatting with keyword args
    """
    sentence = "Hello I am {name} and {age} years old!".format(**person)
    print sentence


def method_9():
    """
        Formatting with zero pads
    """
    for _ in range(11):
        print "The value is: {:02}".format(_)


def method_10():
    """
        Formatting decimal digits
    """
    pi = 3.14159265
    print "Pi is equal to: {:0.2f}".format(pi)


def method_11():
    """
        Formatting dates
    """
    import datetime

    my_date = datetime.datetime(year=1989, month=10, day=30, hour=10, minute=40, second=10)
    print "{:%b %d, %Y}".format(my_date)


if __name__ == '__main__':
    pass
    # method_1()
    # method_2()
    # method_3()
    # method_4()
    # method_5()
    # method_6()
    # method_7()
    # method_8()
    # method_9()
    # method_10()
    # method_11()
