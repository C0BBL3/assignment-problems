def quick_sort_without_swaps(arr):
    if len(arr) > 1:
        pivot = arr[len(arr) // 2]
        sorted_left_arr, sorted_right_arr = [], []
        for item in arr:
            if item < pivot: sorted_left_arr.append(item)
            elif item > pivot: sorted_right_arr.append(item)
        sorted_left_arr = quick_sort_without_swaps(sorted_left_arr)
        sorted_right_arr = quick_sort_without_swaps(sorted_right_arr)
        return sorted_left_arr + [pivot] + sorted_right_arr
    else:
        return arr

print('Testing Quick sort with [5, 8, -1, 9, 10, 3.14, 2, 0, 7, 6]')
print('quick_sort_without_swaps([5, 8, -1, 9, 10, 3.14, 2, 0, 7, 6]) =', quick_sort_without_swaps([5, 8, -1, 9, 10, 3.14, 2, 0, 7, 6]))
assert quick_sort_without_swaps([5, 8, -1, 9, 10, 3.14, 2, 0, 7, 6]) == [-1, 0, 2, 3.14, 5, 6, 7, 8, 9, 10], 'quicksort bad {}'.format(quick_sort_without_swaps([-1, 0, 2, 3.14, 5, 6, 7, 8, 9, 10]))
print('Quick sort Works!!')
