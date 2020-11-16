def partition(arr, low, high):
    smol_element_index = low-1
    pivot = arr[high]
    for element_index in range(low, high):
        if arr[element_index] <= pivot:
            smol_element_index +=1
            arr[smol_element_index], arr[element_index] = arr[element_index], arr[smol_element_index]
    arr[smol_element_index+1], arr[high] = arr[high], arr[smol_element_index+1]
    return smol_element_index + 1
 
def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)
        return arr

arr = [5, 8, -1, 9, 10, 3.14, 2, 0, 7, 6]
print('Testing Quick sort with [5, 8, -1, 9, 10, 3.14, 2, 0, 7, 6]')
print('quick_sort([5, 8, -1, 9, 10, 3.14, 2, 0, 7, 6]) =', quick_sort(arr, 0, len(arr) - 1))
assert quick_sort(arr, 0, len(arr) - 1) == [-1, 0, 2, 3.14, 5, 6, 7, 8, 9, 10], 'quicksort bad {}'.format(quick_sort(arr, 0, len(arr) - 1))
print('Quick sort Works!!')
