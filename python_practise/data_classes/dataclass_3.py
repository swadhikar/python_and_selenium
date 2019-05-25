""" field and post-init processing"""
from dataclasses import dataclass, field
from random import randint


def random_number_generator():
    return randint(20, 30)


@dataclass(unsafe_hash=True)
class Person:
    name: str
    city: str
    age: int = field(default_factory=random_number_generator)
    is_senior: bool = field(default=False, init=False)

    def __post_init__(self):
        if self.age >= 60:
            self.is_senior = True


if __name__ == '__main__':
    p = Person('Nikhil', 'Delhi', 61)
    print(p)
    print(p.is_senior)

    # p = Person('Swadhikar', 'Chennai', 30)
    # f = p.__dataclass_fields__
    # print(f['age'])
    # p.age = random_number_generator()
    # print()
    # print(p)
    # print(hash(p))
    #
    # p1 = Person('Swadhikar', 'Chennai', 29)
    #
    # print(p == p1)  # True; Checks for equality of attributes
    # print(p is p1)  # False; Checks for identity
