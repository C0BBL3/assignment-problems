import sys
sys.path.append('src')
from magic_square import is_valid, half_valid

def fix_arr(array):
    arr = [[value for value in row] for row in array]
    for i, row in enumerate(arr):
        for j, value in enumerate(row):
            if value == 0:
                arr[i][j] = None
    return arr

def increase_index(index, col_index):
    if col_index == 0:
        if index[0] <= 2 and index[1] < 2: return index[0], 2
        elif index[0] < 2 and index[1] >= 2: return index[0] + 1, 1
        elif index[0] >= 2 and index[1] >= 2: return None
    elif col_index == 1:
        if index[0] <= 2 and index[1] < 1: return index[0], 2
        elif index[0] < 2 and index[1] >= 1: return index[0] + 1, 0
        elif index[0] >= 2 and index[1] >= 1: return None
    else:
        if index[0] <= 2 and index[1] < 1: return index[0], 1
        elif index[0] < 2 and index[1] >= 1: return index[0] + 1, 0
        elif index[0] >= 2 and index[1] >= 1: return None

index = (0,0)
arr = [[0 for i in range(0,3)] for i in range(0,3)]
while True:
    col_index = 0
    if half_valid(arr, index[0], col_index):
        while sum(arr[index[0]]) < 15:
            arr[index[0]][col_index] += 1
            if is_valid(fix_arr(arr)):
                for row in arr: print(row)
                print('')
        arr[index[0]][col_index] = 0
    if arr[index[0]][index[1]] < 9: 
        arr[index[0]][index[1]] += 1
        continue
    else:
        index = increase_index(index, col_index)
        if index == None:
            index = (0, 0)
            if col_index < 2: col_index += 1
            else: exit()



