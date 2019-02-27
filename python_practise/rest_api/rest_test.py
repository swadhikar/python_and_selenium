from python.python_practise.json_prac.json_util import Json
import requests


# url = 'https://api.github.com/events'
# res = requests.get(url)
# json_obj = Json(res.json())
# json_obj.write_file('fail.json')
# json_obj = Json('input.json')
# json_obj.write_file('output.json')


my_dict = dict()
my_dict['name'] = 'swadhikar'
my_dict['age'] = 28
my_dict['college'] = dict()
my_dict['college']['name'] = 'TCE'
my_dict['college']['Address'] = dict()
my_dict['college']['Address']['Street'] = 'Tiruparankundram'
my_dict['college']['Address']['City'] = 'Madurai'
my_dict['marks'] = [78, 67, 54, 61, 72, 87]

j = Json(my_dict)
print(j.get_content())
print(j.get('college'))
j.write_file('dict.json', indents=4)
