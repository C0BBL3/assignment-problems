def binary_search(entry, sorted_list, original_sorted_list = []):
    original_sorted_list = sorted_list
    if entry in original_sorted_list: return recursize_part_of_binary_search(entry, sorted_list, original_sorted_list)
    else: return False

def recursize_part_of_binary_search(entry, sorted_list, original_sorted_list):
    mid_point = sorted_list[len(sorted_list) // 2]
    if entry == mid_point: return original_sorted_list.index(mid_point)
    if entry < mid_point: return recursize_part_of_binary_search(entry, sorted_list[:len(sorted_list) // 2], original_sorted_list)
    if entry > mid_point: return recursize_part_of_binary_search(entry, sorted_list[len(sorted_list) // 2:], original_sorted_list)

print('\nPart A Testing...\n')
print('   binary_search(7, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16])')
assert binary_search(7, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16]) == 3, 'Binary Search doesnt work it has to be 3 but was {}'.format(binary_search(7, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16]))
print('   First Test passed!\n')

print('   binary_search(7, [1, 3, 5, 7, 9, 11, 13, 15])')
assert binary_search(7, [1, 3, 5, 7, 9, 11, 13, 15, 17]) == 3, 'Binary Search doesnt work it has to be 4 but was {}'.format(binary_search(7, [1, 3, 5, 7, 9, 11, 13, 15, 17]))
print('   Second Test passed!\n')

print('   binary_search(6, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])')
assert binary_search(6, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2, 'Binary Search doesnt work it has to be 4 but was {}'.format(binary_search(6, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
print('   Second Test passed!\n')

print('   binary_search(7, [1, 3, 5, 7, 9, 11, 13, 15])')
assert binary_search(7, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == False, 'Binary Search doesnt work it has to be 4 but was {}'.format(binary_search(7, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
print('   Second Test passed!\n')
print('Binary Search Works! Part A COMPLETED!\n')

print('Part B')
print('O(log(n) Base 2) where n is the length of the list, so for a length 16 list its 4 iterations.\n')

print('Part C')
print("O(log(n) Base 2) is correct for even length lists because when you're halving an array over and over you are basically undoing the exponential for 2, where if you had a length 16 list and if you halve the array you have now 8 elements and all the way down to 1 so if we were to work our way backup then it woul be 1 * 2 * 2 * 2 * 2 = 16 where each 2 is the undoing of the halving of the array. This style even works for odd numbers, for example 17, 17/2 = 8.5 and 8.5 floored is 8 so then its 8/2/2/2=4/2/2=2/2=1 so 17 can be shown as 1 * 2 * 2 * 2 * 2 as well. Therefore O(log(n) Base 2) is the correct Big-O notation for binary search.")