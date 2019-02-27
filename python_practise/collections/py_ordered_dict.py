# Python script to demonstrate ordered dictionary
# https://docs.python.org/2/library/collections.html#ordereddict-examples-and-recipes
from collections import OrderedDict

def sort_by_value(item):
	return item[1]
	
def sort_by_key(item):
	return item[0]

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

od = OrderedDict(sorted(d.items(), key=sort_by_value))
print("Sort by value:\n", od)
print() 

nod = OrderedDict(sorted(d.items(), key=sort_by_key))
print("Sort by key:\n", nod)
print()

"""
Sort by value:
 OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

Sort by key:
 OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
"""