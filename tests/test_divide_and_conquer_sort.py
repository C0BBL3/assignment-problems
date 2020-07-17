import sys
sys.path.append('src')

from divide_and_conquer_sort import divide_and_conquer_sort

print('Testing...')

print('List #1...')

result = divide_and_conquer_sort([2, 4, 1, 3, 6, 5, 7])

assert result == [1, 2, 3, 4, 5, 6, 7], 'List #1 was wrong and was {}'.format(result)
print('List #1 Passed!')

print('List #1...')

result = divide_and_conquer_sort([4, 1, 3, 6, 5, 7, 9, 8, 2])

assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'List #2 was wrong and was {}'.format(result)
print('List #2 Passed!')

print('List #3...')

result = divide_and_conquer_sort([7, 3, 2, 4, 5, 6, 1])

assert result == [1, 2, 3, 4, 5, 6, 7], 'List #3 was wrong and was {}'.format(result)
print('List #3 Passed!')

print('List #4...')

result = divide_and_conquer_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])

assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'List #4 was wrong and was {}'.format(result)
print('List #4 Passed!')

print('All Tests PASSED!!!!')