from combine_sorted_lists import combine_sorted_lists

def divide_and_conquer_sort(arr): 
    if len(arr) >= 2: 
        first_half = arr[len(arr) // 2:]
        second_half = arr[:len(arr) // 2]
        sorted_first_half = divide_and_conquer_sort(first_half)
        sorted_second_half = divide_and_conquer_sort(second_half)
  
          
        arr = combine_sorted_lists(sorted_first_half, sorted_second_half)
        
    
    return arr
  