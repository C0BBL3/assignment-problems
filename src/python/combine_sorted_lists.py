def combine_sorted_lists(list_1, list_2):
    x, y = 0, 0
    sorted_arr = []
    while x < len(list_1) and y < len(list_2):

        if list_1[x] < list_2[y]:
            sorted_arr.append(list_1[x])
            x += 1

        elif list_2[y] < list_1[x]:
            sorted_arr.append(list_2[y])
            y += 1

    sorted_arr += list_1[x:] #append the rest  
    sorted_arr += list_2[y:] #of both arrays
    return sorted_arr