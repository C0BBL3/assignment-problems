import sys
sys.path.append('src')
from magic_square import is_valid, half_valid

def fix_array(array):
    arr = [[value for value in row] for row in array]
    for i, row in enumerate(arr):
        for j, value in enumerate(row):
            if value == 0:
                arr[i][j] = None
    return arr

def no_duplicate_entries(arr):
    for i, row_1 in enumerate(arr):
        for j, value in enumerate(row_1):
            if not (value in row_1[:j] + row_1[j+1:]):
                for row_2 in arr[:i] + arr[i+1:]:
                    if value in row_2:
                        return False
            else:
                return False
    return True

index = (0,0)
max_index = (2,2)
for num_1 in range(0,10):
    for num_2 in range(0,10):
        for num_3 in range(0,10):
            for num_4 in range(0,10):
                arr = [[num_1, num_2], [num_3, num_4]]
                filled_arr = [[arr[i][j] if j < max_index[1] else 15 - sum(arr[i]) for j in range(0, max_index[1] + 1)] if i < max_index[0] else [15 - sum([row[j] for row in arr]) if j < max_index[1] else 15 - sum([arr[i][j] for i in range(0, max_index[0]) for j in range(0, max_index[1]) if i == j]) for j in range(0, max_index[1] + 1)] for i in range(0, max_index[0] + 1)]
                #I know its bad but look its 357 cols wide AND it works wrote it first try too, it is wider than wide putin, IT HAS TO STAY!!
                fixed_arr = fix_arr(filled_arr)
                if no_duplicate_entries(fixed_arr) and is_valid(fixed_arr):
                    for row in fix_arr(fixed_arr): print(row)
                    exit()

