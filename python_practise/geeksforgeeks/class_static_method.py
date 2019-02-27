class Employee:
    EMP_ID_LIST = list()

    def __init__(self, emp_id, emp_name):
        Employee.__validate_emp_id(emp_id)
        self.emp_id = emp_id
        self.emp_name = emp_name

    @classmethod
    def __validate_emp_id(cls, emp_id):
        if emp_id not in cls.EMP_ID_LIST:
            cls.EMP_ID_LIST.append(emp_id)
        else:
            raise Exception('An employee with ID already exists:', emp_id)

    @classmethod
    def from_csv_data(cls, csv_data):
        emp_id, csv_data = csv_data.split(',')
        return cls(int(emp_id), csv_data)

    @classmethod
    def get_total_employees(cls):
        return len(cls.EMP_ID_LIST)

    @classmethod
    def is_employees_present(cls, emp_id):
        return emp_id in cls.EMP_ID_LIST

    @staticmethod
    def is_employee_new(emp_id):
        return emp_id > 500000

    def get_name(self):
        return self.emp_name


if __name__ == '__main__':
    # e_1 = Employee(423367, 'Swadhikar C')
    # e_2 = Employee(423368, 'Kapil Dev')
    # e_3 = Employee(423369, 'Prabhakaran')
    # total_emps = Employee.get_total_employees()
    # print('Total employees:', total_emps)
    # print()
    # print('Is employee "423370" present?', Employee.is_employees_present(423370))
    # print('Is employee "423367" present?', Employee.is_employees_present(423367))
    # print()
    # print('Is employee "423367" new?', Employee.is_employee_new(423367))
    # print('Is employee "627343" new?', Employee.is_employee_new(627343))
    e_1 = Employee.from_csv_data('500000,Rajam')
    e_1_name = e_1.get_name()
    print(e_1_name)

    e_2 = Employee.from_csv_data('500001,Swadhik')
    e_2_name = e_2.get_name()
    print(e_2_name)

