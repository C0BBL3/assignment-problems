import sys
sys.path.append('src')
from magic_square import is_valid

def fix_arr(array):
    for i, arr in enumerate(array):
        for j, num in enumerate(arr):
            if num == 0:
                array[i][j] = None
    return array

for num_1 in range(0, 10):
    for num_2 in range(0, 10):
        for num_3 in range(0, 10):
            for num_4 in range(0, 10):
                for num_5 in range(0, 10):
                    for num_6 in range(0, 10):
                        for num_7 in range(0, 10):
                            for num_8 in range(0, 10):
                                for num_9 in range(0, 10):
                                    arr = [[num_1, num_2, num_3], [num_4, num_5, num_6], [num_7, num_8, num_9]]
                                    arr = fix_arr(arr)
                                    if is_valid(arr):
                                        for ar in arr:
                                            print(ar)
                                    else:
                                        continue 


