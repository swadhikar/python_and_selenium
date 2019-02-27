"""
    Common utility to parse a dictionary with variable arguments
"""
from copy import copy


def get_value(dictionary, *args, ignore_missing_key=False):
    """Gets a dictionary value by nested looping"""
    result = copy(dictionary)
    dict_repr = 'dictionary'

    for index, arg in enumerate(args):
        result = result[arg]
        dict_repr += '["{}"]'.format(arg)
        if type(result) != dict and arg != args[-1]:
            error = 'Unable to find key "{}" in sub dictionary: {} = {}\n' \
                .format(args[index + 1], dict_repr, result)
            if ignore_missing_key:
                print(error)
                break
            raise Exception(error)

    print("Final result retrieved: {} = {}".format(dict_repr, result))
    return result


def get_dict_value(dictionary, *args, ignore_missing_key=False):
    """ Supports case insensitive search """

    result = copy(dictionary)

    dict_repr = '<input_dict>'

    for index, arg in enumerate(args):
        # For case insensitive search convert keys to lower
        result = {k.lower(): v for k, v in result.items()}
        result = result.get(arg.lower())

        dict_repr += '["{}"]'.format(arg)

        if result is None or (type(result) != dict and arg != args[-1]):
            error = 'Unable to find key "{}" in sub dictionary: {} = {}\n' \
                .format(args[index + 1], dict_repr, result)
            if ignore_missing_key:
                print(error)
                break
            raise Exception(error)

    print('Return value: {}'.format(result))
    return result


if __name__ == '__main__':
    d = {
        'users': {
            'swad': {
                'name': {
                    'firstName': 'Swadhikar',
                    'lastName': 'Chandramohan'
                },
                'age': 29,
                'skill': 'python automation'
            },
            'lokesh': {
                'name': {
                    'firstname': 'Lokesh',
                    'lastname': 'B'
                }
            },
            'age': 30,
            'skill': 'python developer'
        }
    }

    from json import dumps
    print(dumps(d, indent=2))

    user_fn = get_dict_value(d, 'users', 'swad', 'name', 'firstname')
    user_ln = get_dict_value(d, 'Users', 'Lokesh', 'name', 'lastname')

    """
    Result:
    /usr/bin/python3.6 /home/swadhi/PycharmProjects/pyselenium/python/python_practise/dictionaries/json_result_parser.py
    {
      "users": {
        "swad": {
          "name": {
            "firstName": "Swadhikar",
            "lastName": "Chandramohan"
          },
          "age": 29,
          "skill": "python automation"
        },
        "lokesh": {
          "name": {
            "firstname": "Lokesh",
            "lastname": "B"
          }
        },
        "age": 30,
        "skill": "python developer"
      }
    }
    Return value: Swadhikar
    Return value: B
    
    Process finished with exit code 0

    """