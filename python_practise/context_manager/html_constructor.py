from contextlib import contextmanager
from contextlib import redirect_stdout
from contextlib import suppress
from collections import namedtuple
import os
import io
from python.log_util.logger import log


Tag = namedtuple('Tag', 'TITLE H1 H2 P')


@contextmanager
def show_tag(tag):
    print('<{}>'.format(tag), end='')
    yield
    print('</{}>'.format(tag))


if __name__ == '__main__':
    t = Tag('title', 'h1', 'h2', 'p')

    with show_tag(t.TITLE):
        print("Welcome Page", end='')

    with show_tag(t.P):
        print("Paragraph tag", end='')

    files = ['unknowfile.file', './remfile.txt']
    for file in files:
        with suppress(FileNotFoundError):
            os.remove(file)

    f = io.StringIO()
    with redirect_stdout(f):
        help(pow)
    help_pow = f.getvalue()

    log.info('Help (POW): \n' + help_pow)




