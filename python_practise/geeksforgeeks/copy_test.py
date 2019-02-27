import python.geeksforgeeks.eXceptions
# importing "copy" for copy operations
import copy

# # initializing list 1
li1 = [1, 2, [3, 5], 4]

# # using copy to shallow copy
# li2 = copy.copy(li1)
li2 = copy.deepcopy(li1)

print(li1)
print(li2)

li2[2][0] = 7

print(li1)
print(li2)
