from python.python_practise.misc.class_methods.rules import Rule


def call_me():
    print('Inside call me!')
    print(Rule().get())


if __name__ == '__main__':
    rule = Rule()
    rule.add('names', ['swa', 'dhi', 'kar'])
    print(rule.get())
    call_me()
