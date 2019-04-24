from dataclasses import dataclass


@dataclass(order=True, unsafe_hash=True)
class Person:
    name: str
    age: int
    city: str


if __name__ == '__main__':
    p1 = Person('TName', 12, 'Chennai')
    # p2 = Person('TName', 13, 'Chennai')
    print(p1)
    print(hash(p1))
    p1.name = 'Swadhikar'
    print()
    print(p1)
    print(hash(p1))
