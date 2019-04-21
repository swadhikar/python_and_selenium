from dataclasses import dataclass


class Person:
    """ Usual way of defining class without dataclasses"""

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return '{classname}(name={name}, age={age}, city={city})'.format(
            classname=self.__class__.__name__,
            name=self.name,
            age=self.age,
            city=self.city
        )

    def __eq__(self, other):
        return (self.name, self.age, self.city) == (other.name, other.age, other.city)


@dataclass
class NewPerson:
    """Implementation of dataclass"""
    name: str
    age: int
    city: str

    @property
    def email(self):
        return self.name.lower() + '_' + self.city + str(self.age) + '@company.com'


if __name__ == '__main__':
    # person_1 = Person('swadhikar', 29, 'chennai')
    # person_2 = Person('swadhikar', 29, 'chennai')
    # print(person_1 == person_2)

    new_person_1 = NewPerson('Vivek', 30, 'chennai')
    new_person_2 = NewPerson('Vivek', 30, 'chennai')
    print(new_person_1)
    print(new_person_1 == new_person_2)
    print(new_person_1.email)
    """
        NewPerson(name='Vivek', age=30, city='chennai')
        True
        vivek_chennai30@company.com
    """
