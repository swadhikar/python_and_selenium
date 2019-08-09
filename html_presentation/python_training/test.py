import re

code_file = 'test.py'
dunder = '__'
keywords = ['print', 'False', 'class', 'finally', 'is', 'return', 'None', 'continue', 'for', 'lambda', 'try', 'True', 'def', 'from', 'nonlocal', 'while', 'and', 'del', 'global', 'not', 'with', 'as', 'elif', 'if', 'or', 'yield', 'assert', 'else', 'import', 'pass', 'break', 'except', 'in', 'raise']
_self = 'self'
special_chars = ['(', ')', ':', '.', '=']

def is_special_method(word):
    return

def tagify(string, class_name, tag='span'):
    return re.sub(string, r'<span class="{}">{}</span>'.format(class_name, string), string)

def process_line(line):
    result_line = ''

    line_words = re.findall(r'\w+|[a-zA-Z]+|[#():,.= +\'\"]|__\w+__', line)

    for index in range(len(line_words)):
        word = line_words[index]

        if bool(re.search(r'__\w+__', word)):   # special methods
            class_name = 'special-method'
            word = re.sub(r'__(\w+)__', r'<span class="{}">__\1__</span>'.format(class_name), word)

        elif index < len(line_words) - 1 and line_words[index + 1] == '(':
            word = tagify(word, class_name='function-call')

        elif word in keywords:
            word = tagify(word, class_name='keywords')

        elif word == _self:
            word = tagify(word, class_name='self')

        result_line += word

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


f = FileReader('/home/swadhi/python_and_selenium/html_presentation/result.py')
r = f()
print(r, end='')
