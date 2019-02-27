from collections import OrderedDict


def get_list_str(l, first_line=False):
    if not first_line:
        return '|\n    -------> ' + ' --> '.join([str(n) for n in l])
    return ' --> '.join([str(n) for n in l])


def print_it(d):
    line_1 = '|---{:<5}--> {:<5}'
    line_x = '    {:<5}'
    for k, v in d.items():
        print('|\n' + line_1.format(k, get_list_str(v[0], first_line=True)))
        for i in v[1:]:
            print(line_x.format(get_list_str(i)))


if __name__ == '__main__':
    d = OrderedDict()
    d['p1'] = [['1', '2'], ['3', '4'], ['5', '6']]
    d['p2'] = [['a', 'b'], ['d', 'e', 'f'], [1, 2, 3, 4, 'g', 'h', 'i']]
    d['p3'] = [['a', 'b'], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    d['p4'] = [['a', 'b'], ['a', 'b'], ['a', 'b']]
    d['p5'] = [['a', 'b'], ['a', 'b'], ['a', 'b']]
    d['p6'] = [['a', 'b'], ['a', 'b', 0, 1, 2, 3]]

    print_it(d)
