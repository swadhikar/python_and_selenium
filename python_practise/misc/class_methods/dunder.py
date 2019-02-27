from collections import OrderedDict


class Rule:
    def __init__(self):
        self._rule_table = OrderedDict()

    def add(self, s, s_p, d, d_p):
        data = [d_p, s, s_p]
        if self._rule_table.get(d):
            self._rule_table[d].append(data)
        else:
            self._rule_table[d] = [data]

    def get(self):
        return self._rule_table

    def __getitem__(self, item):
        return self._rule_table[item]

    def __len__(self):
        return len(self._rule_table)

    def __iter__(self):
        for item, value in self._rule_table.items():
            yield item, value


if __name__ == '__main__':
    r = Rule()
    r.add('1', '2', '3', '4')
    r.add('10', '2', '7', '4')
    r.add('10', '2', '11', '4')

    for i in r:
        print(i)