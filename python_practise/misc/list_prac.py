# Python exercises
"""
1. Use a list comprehension to construct the list [’ab’, ’ac’, ’ad’, ’bb’, ’bc’, ’bd’].
2. Use a slice on the above list to construct the list [’ab’, ’ad’, ’bc’].
3. Use a list comprehension to construct the list [’1a’, ’2a’, ’3a’, ’4a’].
4. Simultaneously remove the element ’2a’ from the above list and print it.
5. Copy the above list and add ’2a’ back into the list such that the original is still missing
it.
6. Use a list comprehension to construct the list [’abe’, ’abf’, ’ace’, ’acf’, ’ade’, ’adf’,
’bbe’, ’bbf’, ’bce’, ’bcf’, ’bde’, ’bdf’]
"""

# 1 - construct list [’ab’, ’ac’, ’ad’, ’bb’, ’bc’, ’bd’] using comprehensions
my_list = [ a + b for a in ['a', 'b'] for b in ['b', 'c', 'd']]
# print(my_list)

# 2 - Use a slice on the above list to construct the list [’ab’, ’ad’, ’bc’].
new_list = my_list[::2]
# print(new_list)

# 3 - Use a list comprehension to construct the list [’1a’, ’2a’, ’3a’, ’4a’].
alpha_num_list = [str(i) + 'a' for i in range(1, 5)]
# print(alpha_num_list)

# 4 - Simultaneously remove the element ’2a’ from the above list and print it
remove_index = 1
removed_elem = alpha_num_list.pop(remove_index)
print(f'{alpha_num_list}        : Original list')

# 5 - Copy the above list and add ’2a’ back into the list such that the original is still missing it
copy_list = alpha_num_list[:]
copy_list.insert(remove_index, removed_elem)
print(f'{copy_list}  : Copied list')