# To run this code use the below command in terminal
#
# $ python3 <path/to/this/file>/merge_dicts.py
#

details = {'name': 'Michael Kennedy', 'id': 1}  # id is subject to change in another dictionary
address = {'street': 'Greed Street', 'city': 'Willow village', 'country': 'United States'}
work = {'title': 'Software Architect', 'id': 271, 'company': 'zoho corp.'}

# Merge dictionaries in a non python way
emp = {}
for k in details:
    emp[k] = details[k]
for k in address:
    emp[k] = address[k]
for k in work:
    emp[k] = work[k]
print(emp, '\n')


# Classical way
classic_emp = details.copy()
classic_emp.update(address)
classic_emp.update(work)
print(classic_emp, '\n')

# Using dictionary comprehensions
comp_emp = {k: v for d in [details, address, work] for k, v in d.items()}
print(comp_emp, '\n')

# For python version 3.5+
# new_emp = {**details, **address, **work}
# print(new_emp, '\n')

boolean = emp == classic_emp == comp_emp # == new_emp
print('Is dictionaries equal:', boolean)
