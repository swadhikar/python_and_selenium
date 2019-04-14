""" Decorators using context lib """


def remove_string_list_items(func):
    def wrapper(in_list):
        modified_list = (item for item in in_list if type(item) is int)  # Generator comprehension
        return func(modified_list)

    return wrapper


@remove_string_list_items
def summer(in_list):
    _sum = 0
    for num in in_list:
        _sum += num
    return _sum


if __name__ == '__main__':
    list_items = ['Swadhikar', 28, 'cse', 'Vivek', 29, 'ece', 'thangav', 30, 'eee']
    result = summer(list_items)
    print(result)
