class Rule:
    def __init__(self):
        self._rule_table = dict()

    def add(self, name, value):
        self._rule_table.update({name: value})

    def get(self):
        return self._rule_table
