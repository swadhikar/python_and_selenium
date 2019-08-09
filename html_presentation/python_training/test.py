import re

code_file = 'test.py'
dunder = '__'
statements = 'for if else try except finally with print return'.split()

def is_special_method(word):
    return

def tagify(string, class_name, pattern=None, tag='span'):
    if pattern is not None:
        return re.sub(pattern, r'<span class="{}">\1</span>'.format(class_name), string)
    return re.sub(string, r'<span class="{}">{}</span>'.format(class_name, string), string)

def process_line(line):
    result_line = ''
    for word in line.split():

        if bool(re.search(r'__\w+__', word)):   # special methods
            word = tagify(word, pattern=r'(__\w+__)', class_name='special-method')

        elif word in statements:  # statements
            word = tagify(word, class_name='statement')

        result_line += word + ' '

    return result_line

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self):
        result_html = ''
        with open(self.filename) as f:
            for line in f:
                result_html += process_line(line) + '\n'
        return result_html


# pl = process_line('def __init__():')
# print(pl)
#
# pl = process_line('for i in range():')
# print(pl)



# r = is_special_method('__init__')
# print(r)
f = FileReader('/home/swadhi/python_and_selenium/html_presentation/python_training/test.py')
r = f()
print(r, end='')
