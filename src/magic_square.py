def is_valid(matrix):
    if check_diags(matrix)[0]:
        if check_diags(matrix)[1]: return True
        else: return False
    elif check_rows(matrix)[0]:
        if check_rows(matrix)[1]: return True
        else: return False
    elif check_cols(matrix)[0]: 
        if check_cols(matrix)[1]: return True
        else: return False
    elif check_rows(matrix)[0] and check_cols(matrix)[0] and check_diags(matrix)[0]: return True
    else: return True
    #if check_rows(matrix)[1] and check_cols(matrix)[1] and check_diags(matrix)[1]: return True
    #elif not check_rows(matrix)[0] and not check_cols(matrix)[0] and not check_diags(matrix)[0]: return True
    #elif check_rows(matrix)[0] and check_cols(matrix)[0] or check_diags(matrix)[0]: return True
    #else: return False
   # if not check_rows(matrix)[0] and check_cols(matrix)[1] and not check_diags(matrix)[0]: return True
   # if not check_rows(matrix)[0] and not check_cols(matrix)[0] and check_diags(matrix)[1]: return True
  #  if not check_rows(matrix)[0] and not check_cols(matrix)[0] and not check_diags(matrix)[0]: return True
 #   if not (check_rows(matrix)[1] and check_cols(matrix)[1] and check_diags(matrix)[1]): return False 

def half_valid(matrix, row_index, col_index):
    return 15 - sum(matrix[row_index][:col_index] + matrix[row_index][col_index + 1:]) in list(range(0,10))

def inner_most_if(matrix):
    if check_diags(matrix) == (True, True):
        return True
    elif check_diags(matrix) == (True, False):
        return True
    else:
        return False

def check_rows(matrix):
    can_rows_be_added, i = can_rows_be_added_up(matrix)
    if can_rows_be_added:
        if sum(matrix[i]) == 15: return True, True
        else: return True, False
    else: return False, False

def can_rows_be_added_up(matrix):
    for row in matrix:
        if None not in row: return True, matrix.index(row)
    return False, None

def check_cols(matrix):
    can_cols_be_added, i = can_cols_be_added_up(matrix)
    if can_cols_be_added:
        if sum([row[i] for row in matrix]) == 15: return True, True
        else: return True, False
    else: return False, False

def can_cols_be_added_up(matrix):
    for i in range(len(matrix[0])):
        col = [row[i] for row in matrix]
        if None not in col: return True, i
    return False, None

def check_diags(matrix):
    can_diags_be_added, forward_diag, backward_diag = can_diags_be_added_up(matrix)
    if can_diags_be_added:
        if sum(forward_diag) == 15 and sum(backward_diag) == 15: return True, True
        else: return True, False
    else: return False, False

def can_diags_be_added_up(matrix):
    forward_diag = [matrix[i][i] for i in range(len(matrix[0]))]
    backward_diag = [matrix[i][(len(matrix) - 1) - i] for i in range(len(matrix[0]))]
    if None not in forward_diag and  None not in backward_diag: return True, forward_diag, backward_diag
    else: return False, None, None