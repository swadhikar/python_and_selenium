import requests
from pprint import pprint
from python.python_practise.json_prac.json_util import Json


def get_user_data(json_text, user_id):
    j = Json(json_text)
    user_data = dict()

    for i in range(j.num_elements):
        elem = j.get_element_at_index(i)
        if elem['userId'] == user_id:
            k = elem['id']
            user_data[k] = {}
            user_data[k]['title'] = elem['title']
            user_data[k]['body'] = elem['body']

    return user_data


url = 'https://jsonplaceholder.typicode.com/posts'

r = requests.get(url)

# print('Response:')
# print(r.text)

# sc = r.status_code
# print(f'Status code: {sc}')
print('Request processed successfully!')
# pprint(get_user_data(r.text, user_id=1))
# pprint(get_user_data(r.text, user_id=2))
# pprint(get_user_data(r.text, user_id=3))
pprint(get_user_data(r.text, user_id=10))