num_list = range(1, 101)

tall_buildings = {
    'burj khalifa':              828,
    'shanghai tower':            632,
    'abraj al-bait clock tower': 601,
    'ping an finance center':    599,
    'lotte world tower':         554,
}


def is_prime(num):
    if num < 2:
        return False
    return all(num % i for i in range(2, num))


def is_fibonacci(num):
    history = 0, 1
    while sum(history) < num:
        history = history[1], sum(history)

    return sum(history) == num


def set_comprehension(numbers):
    """ Find numbers that are both prime and fibonacci """
    primes = {num for num in numbers if is_prime(num)}
    fibos = {num for num in numbers if is_fibonacci(num)}
    primo_fibo = primes & fibos

    print('prime and fibonacci number:', primo_fibo, '-> (undordered, since sets are unordered bags!)')

    """
        prime and fibonacci number: {13, 89, 2, 3, 5} -> (undordered, since sets are unordered bags!)
    """


def dict_comprehension(tall_buildings):
    # names_dict = {name.capitalize(): height for name, height in tall_buildings.items() if 'tower' in name}
    names_dict = {
        name.capitalize(): tall_buildings[name]
        for name in tall_buildings
        if 'tower' in name
    }
    print(names_dict)

    """
        {'Abraj al-bait clock tower': 601, 'Shanghai tower': 632, 'Lotte world tower': 554}
    """


def list_comprehension(num_list):
    fibo_primo = [num for num in num_list if is_fibonacci(num) and is_prime(num)]
    print(fibo_primo)
    """[2, 3, 5, 13, 89]"""


def generator_statement(num_list=None):
    fibo_primo = (num for num in num_list if is_prime(num) and is_fibonacci(num))
    print(list(fibo_primo))
    """[2, 3, 5, 13, 89]"""


if __name__ == '__main__':
    set_comprehension(num_list)
    dict_comprehension(tall_buildings)
    list_comprehension(num_list)
    generator_statement(num_list)
