# Check if a given dictionary a subset of a dictionary

sports = {"geeksforgeeks": 1, "practice": 2, "contribute": 3}

find = {"practice": 2, 'contribute': 3}


# # Method 1:
# for k, v in find.items():
#     if (k, v) not in sports.items():
#         print('{}: {} DOES NOT exists in main dict'.format(k, v))

# # Method 2:
if all((k, v) in sports.items() for k, v in find.items()):
    print('Is subset!')
else:
    print('Is not subset :(')
