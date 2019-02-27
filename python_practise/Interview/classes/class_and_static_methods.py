# Python script to differentiate class methods and static methdods


class Employee:
    COMPANY_NAME = 'cisco'
    CEO_F_NAME = 'Bill'
    CEO_L_NAME = 'Gates'

    def __init__(self, f_name, l_name, role, salary=None):
        self.f_name = f_name
        self.l_name = l_name
        self.role = role
        self.salary = int(salary) if salary else 0

    def get_email(self):
        return self.f_name + '.' + self.l_name + '@' + Employee.COMPANY_NAME + '.com'

    @classmethod
    def employee_from_log(cls, log_str):
        first_name, lastname, _, _, role, salary = log_str.split(',')
        return cls(first_name, lastname, role, salary)

    def get_salary(self):
        return self.salary

    @classmethod
    def ceo_mail(cls):
        return cls(cls.CEO_F_NAME, cls.CEO_L_NAME, 'CEO').get_email()

    @staticmethod
    def calculate_bonus(salary, role):
        bonus_percent = 50

        if 'developer' in role:
            bonus_percent = 80
        if 'manager' in role:
            bonus_percent = 100

        bonus_amount = salary * (bonus_percent / 100)
        return salary + bonus_amount


if __name__ == '__main__':

    log_str = [
        'Johnny,Ross,auckland,technical lead,developer,1000',
        'Bill,Hastings,sydney,software engr,sr. developer,2000',
        'John,Right,melbourne,senior manager,manager,',
    ]

    for log in log_str:
        emp = Employee.employee_from_log(log)
        mail = emp.get_email()
        bonus = Employee.calculate_bonus(emp.salary, emp.role)
        print(mail)
        print('Bonus = %s' % bonus)
        print()

    # Fetching CEO details
    ceo_mail = Employee.ceo_mail()
    print('#####################################')
    print('             CEO DETAILS             ')
    print('#####################################')
    print(ceo_mail)
    print()
