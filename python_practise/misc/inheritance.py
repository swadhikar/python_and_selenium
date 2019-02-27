# Python program to demonstrate inheritance
class Person(object):
    person_dict = {}

    def __init__(self, first_name, last_name):
        """Person initializer"""
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name):
        _first_name, _last_name = full_name.split()
        return cls(_first_name, _last_name)

    def is_person(self):
        """Returns the person information"""
        return "{} is a person!".format(self.first_name)

    def is_employee(self):
        """Returns the employee information"""
        return "{} is not an employee!".format(self.first_name)


class Employee(Person):
    def __init__(self, full_name, salary):
        super(Employee, self).from_full_name(full_name)
        self.salary = salary

    def is_employee(self):
        return "{} is an employee!".format(self.first_name)

    def get_salary(self):
        return self.salary


class Programmer(object):
    def __init__(self, language):
        self.language = language

    def get_language(self):
        return self.language


class SoftwareEngineer(Employee, Programmer):
    def __init__(self, full_name, salary, language):
        """Software Engineer initializer"""
        super(self.__class__, self).__init__(full_name, salary)
        super(self.__class__, self).__init__(language)
        print("Constructors initialized!")


if __name__ == '__main__':
    pass
    # swadhi = Person.from_full_name("Swadhikar Chandramohan")
    # print swadhi.is_person()
    # print swadhi.is_employee()
    # print
    #
    # swadhi_symc = Employee("Swadhikar Chandramohan",  1000)
    # print swadhi_symc.is_person()
    # print swadhi_symc.is_employee()
    # print

    # How to check if a class is subclass of another?
    # print issubclass(Person, Employee)
    # print issubclass(Employee, Person)
    # print issubclass(Person, object)
    # print issubclass(Employee, object)

    # sw_engr = SoftwareEngineer("Swadhikar C", 1000, 'python')
    # print sw_engr.get_salary()
    # print sw_engr.get_language()
