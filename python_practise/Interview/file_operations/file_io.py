from time import sleep

class StaticReader(object):
    """Allows to read file only"""
    def __init__(self, filename):
        self.contents = self._read_file(filename)

    @staticmethod
    def _read_file(filename):
        lines = []

        with open(filename) as f_obj:
            for item in f_obj:
                lines.append(item)

        return tuple(lines)

    def next_line(self):
        for item in self.contents:
            yield str(item).rstrip('\n')

    def show_lines(self):
        print len(self.contents)


if __name__ == '__main__':
    r = StaticReader('./file.txt')
    i = 0

    for line in r.next_line():
        print line
        sleep(0.5)
        i += 1

        if i > 10:  # Break loop conditionally
            break
