"""
    Task 2:

    Step 1:
        Inside main:
            From the class from previous task create 5 to 6 employee objects like below:
                emp_1 = Employee(...)
                emp_2 = Employee(...)
                ...

    Step 2:
        Write a class named Company with methods
            1. __init__(list_of_employees)
            2. get_total_employees(): This method should return the total number of employees passed in the init

    Step 3:
        Now, to the class Employee as in below snippet, add a default argument to __init__ method: language='python'
        Add another method get_language as below that returns the language of the employee

    Step 4:
        delete all the employee instances created so far: emp_1, ... using del emp_1, ...

    Step 5:
        Now in main, create 5 to 6 employee instances as before along with the language parameter.
        Eg. emp_1 = Employee('swad', 'c', 'cisco', 'perl')

    Step 6:
        Now create one Company instance by passing the employees created above as list.
        In Company class, write methods:
            1. get_employees(language): this method should accept a language as input and return all
               the employees with that given language

               If an employee with language is not found, it must be logged and an empty list should be returned
               eg. company_instance.get_employees('java') -> [<emp object 1>, <emp object 2> , ...]

            2. get_employee_mails(language):
                Same as above, but instead of employee objects return the employee mail ids

                eg. company_instance.get_employee_mails('java') -> [swad.c@hcl.com, ...]
"""
# class Employee:
#     def __init__(self, name, ..., language='python'):
#         self.name = ...
#         ...
#         self.language = language
#
#     def get_language(self):
#         return ...
