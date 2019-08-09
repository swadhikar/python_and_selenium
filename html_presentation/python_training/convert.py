import re

code_file = 'test.py'
dunder = '__'
keywords = ['print', 'False', 'class', 'finally', 'is', 'return', 'None', 'continue', 'for', 'lambda', 'try', 'True', 'def', 'from', 'nonlocal', 'while', 'and', 'del', 'global', 'not', 'with', 'as', 'elif', 'if', 'or', 'yield', 'assert', 'else', 'import', 'pass', 'break', 'except', 'in', 'raise']
_self = ['self', 'cls']
special_chars = ['(', ')', ':', '.', '=']
annotations = ['@', 'staticmethod', 'classmethod', 'property']


def get_html_template():
    fmt_string = """<!DOCTYPE html>
<html>
  <head>
    <title>
      Python Training
    </title>
    <link href="style.css" rel="stylesheet" type="text/css">
  </head>

  <body>
    <div class="box">
<pre class="code">{}</pre>
    </div>
  </body>
</html>"""
    return fmt_string

def tagify(string, class_name, tag='span'):
    return re.sub(string, r'<span class="{}">{}</span>'.format(class_name, string), string)

def process_line(line):

    # if line.lstrip().startswith('#'):
    #     return '<span class="comments">' + line.rstrip('\n') + '</span>'

    result_line = ''
    string_started = False
    started_string = None
    comment_started = False

    line_words = re.findall(r'\w+|[a-zA-Z]+|[#():,.= +\'\"@]|__\w+__', line)
    print(line_words)

    for index in range(len(line_words)):
        word = line_words[index]

        if word == '#':
            comment_started = True
            word = '<span class="comments">' + word

        if comment_started:
            if index == len(line_words) - 1:
                print('******comment ended******')
                result_line += word + '</span>'
                string_started = False
                return result_line
            else:
                result_line += word
            continue

        if string_started:
            if word == started_string:
                result_line += word + '</span>'
                string_started = False
            else:
                result_line += word
            continue

        if word in ("'", '"', '"""', "'''") and not string_started:
            started_string = word
            word = '<span class="strings">' + word
            string_started = True
            result_line += word
            continue

        if re.search(r'__\w+__', word):   # special methods __init__, __repr__
            class_name = 'special-method'
            word = re.sub(r'__(\w+)__', r'<span class="{}">__\1__</span>'.format(class_name), word)

        elif index < len(line_words) - 1 and line_words[index + 1] == '(':
            if line_words[index - 2] not in ('class', 'def'):
                word = tagify(word, class_name='function-call')
            else:
                word = tagify(word, class_name='definition')

        elif word in keywords:
            word = tagify(word, class_name='keywords')

        elif word in _self:
            word = tagify(word, class_name='self')

        elif word == '@' or line_words[index - 1] == '@':
            word = tagify(word, class_name='annotations')

        result_line += word

    return result_line

class File:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self):
        result_html = ''
        with open(self.filename) as f:
            for line in f:
                result_html += process_line(line) + '\n'
        template = get_html_template()
        html_content = template.format(result_html)
        with open('./index.html', 'w') as f:
            f.write(html_content)

f = File('code.py')
f()
