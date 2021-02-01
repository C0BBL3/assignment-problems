from magic_square import is_valid
import sys
sys.path.append('src/python')

print('\nTesting... \n')

arr1 = [[1, 2, None], [None, 3, None], [None, None, None]]

arr2 = [[1, 2, None], [None, 3, None], [None, None, 4]]

arr3 = [[1, 2, None], [None, 3, None], [5, 6, 4]]

arr4 = [[None, None, None], [None, 3, None], [5, 6, 4]]

print("    Testing is_valid() #1")
assert is_valid(arr1) == True, "is_valid was not right, it should be True because because no rows, columns, or diagonals are completely filled in, but was {}".format(is_valid(arr1))
print("    is_valid() #1 Passed!!!\n")

print("    Testing is_valid() #2")
assert is_valid(arr2) == False, "is_valid was not right, it should be False because a diagonal is filled in and it doesn't sum to 15, but was {}".format(is_valid(arr2))
print("    is_valid() #2 Passed!!!\n")

print("    Testing is_valid() #3")
assert is_valid(arr3) == False, "is_valid was not right, it should be False because a diagonal is filled in and it doesn't sum to 15 and it doesn't matter that the bottom row does sum to 15, but was {}".format(is_valid(arr3))
print("    is_valid() #3 Passed!!!\n")

print("    Testing is_valid() #4")
assert is_valid(arr4) == True, "is_valid was not right, it should be True because there is one row that's filled in and it sums to 15, but was {}".format(is_valid(arr4))
print("    is_valid() #4 Passed!!!\n")

print('All Tests Passed!!!')
