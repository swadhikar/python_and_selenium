import re

code_file = 'test.py'
dunder = '__'

def is_special_method(word):
    if bool(re.search(r'__\w+__', word)):
        return re.sub('(__\w+__)\(', tagify(word), word)
    return word

def tagify(word, class_name, tag='span'):
    return '<{tag} class="{class_name}">{word}</{tag}>'.format(tag=tag, class_name=class_name, word=word)


def process_line(line):
    result_line = line
    for word in line.split():
        if is_special_method(word):
            tagified = tagify(word, class_name='special-method')
            print('tagified:', tagified)
            result_line.replace(word, tagify(word, class_name='special-method'))

    return result_line

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self):
        result_html = ''
        with open(self.filename) as f:
            for line in f:
                result_html += process_line(line)
        return result_html


# r = is_special_method('__init__')
# print(r)

f = FileReader('/home/swadhi/python_and_selenium/html_presentation/python_training/test.py')
r = f()
# print(r, end='')
