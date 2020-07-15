def combine_sorted_lists(list_1, list_2):
    x, y = 0, 0
    sorted_arr = []
    while x < len(list_1) and y < len(list_2):
        min_1 = min(list_1[x:])
        min_2 = min(list_2[y:])

        if min_1 < min_2:
            sorted_arr.append(min_1)
            x += 1

        elif min_2 < min_1:
            sorted_arr.append(min_2)
            y += 1

    sorted_arr += list_1[x:]
    sorted_arr += list_2[y:]
    return sorted_arr