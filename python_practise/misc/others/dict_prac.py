# Python program to practise dictionary

'''
	1. Asks the user for a string, then creates the following dictionary. The values are the
	letters in the string, with the corresponding key being the place in the string.
	2. Replaces the entry whose key is the integer 3, with the value ”Pie”.
	3. Asks the user for a string of digits, then prints out the values corresponding to those
	digits.
'''

# 1 - Asks the user for a string, then creates the following dictionary. The values are the
#     letters in the string, with the corresponding key being the place in the string.
word = input('Please enter a string: >>')

# my_dict = {}
# for index, letter in enumerate(word):
    # my_dict.update({index: letter})
# print(my_dict)

# -- Using dict comprehensions
my_dict = {i: l for i, l in enumerate(word)}
# print(my_dict)

# 2 - Replaces the entry whose key is the integer 3, with the value ”Pie”.
replace_key = 3
my_dict.update({replace_key: 'pie'})
# print(my_dict)

# 3 - Asks the user for a string of digits, then prints out the values corresponding to those digits.
digits = input('Please enter a string of digits: >>')
for digit in digits:
    try:
	    print(digit,": ",my_dict[int(digit)])
    except:
        pass
