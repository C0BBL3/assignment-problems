import sys
sys.path.append('src')

from combine_sorted_lists import combine_sorted_lists

cbl_1 = combine_sorted_lists([1, 3, 4, 5, 7],[2, 6])

assert cbl_1 == [1, 2, 3, 4, 5, 6, 7], 'Combine Sorted Lists should be [1, 2, 3, 4, 5, 6, 7] but was {}'.format(cbl_1)

cbl_2 = combine_sorted_lists([2, 3, 4, 5, 7, 9],[1, 6, 8])

assert cbl_2 == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'Combine Sorted Lists should be [1, 2, 3, 4, 5, 6, 7, 8, 9] but was {}'.format(cbl_2)

cbl_3 = combine_sorted_lists([21], [69, 420])

assert cbl_3 == [21, 69, 420], 'Combine Sorted Lists should be [21, 69, 420] but was {}'.format(cbl_3)

cbl_4 = combine_sorted_lists([1, 3, 5, 7, 9],[2, 4, 6, 8])

assert cbl_4 == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'Combine Sorted Lists should be [1, 2, 3, 4, 5, 6, 7, 8, 9] but was {}'.format(cbl_4)

print('All Tests PASSED!!!')