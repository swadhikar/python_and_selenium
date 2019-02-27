def hello_decorator(function):
    def inner(arg):
        print('*****************************************')
        # function(*args, **kwargs)
        function(arg + '!')
        print('*****************************************')

    return inner


def team_decorator(*args, **kwargs):
    print('*** Reportees of ', kwargs['like'], '***')
    for member in args:
        print('   - ' + member)

    def inner(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)

        return wrapper

    return inner


@hello_decorator
def print_name(name):
    print('Welcome', name)


@team_decorator('vivek', 'thangavel', 'naveen', like='swad')
def swad_team(functions):
    print(functions[0] + ' team functions include:')

    for function in functions[1:]:
        print('  # ' + function)


if __name__ == '__main__':
    # print_name('swadhi')
    swad_team(['Automation', 'Code fix', 'Test case Automation'])
    swad_team(['Automation', 'Code fix', 'Test case Automation'])
    swad_team(['Automation', 'Code fix', 'Test case Automation'])
    swad_team(['Manual', 'Fuck with ISE', 'Write test case'])
