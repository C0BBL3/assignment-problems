def riemann_sum(function, a, b, delta_x, rule):
    if rule == 'left endpoint':
        return delta_x * sum([function(x) for x in [x / delta_x for x in range(a * delta_x, (b - delta_x) * delta_x)]])
    if rule == 'right endpoint':
        return delta_x * sum([function(x) for x in [x / delta_x for x in range((a + delta_x) * delta_x, b  * delta_x)]])
    if rule == 'midpoint':
        return delta_x * sum([function(x+delta_x/2) for x in [x / delta_x for x in range(a * delta_x, (b - delta_x) * delta_x)]])
    if rule == 'trapezoidal"':
        return delta_x * sum([function(x) / 2 if x == a or x == b else function(x) for x in [x / delta_x for x in range(a * delta_x, b  * delta_x)]])
    if rule == 'simpson':
        simpson_list = []
        for index, x in enumerate([x / delta_x for x in range(a * delta_x, (b - delta_x) * delta_x)]):
            if index == 0 or index == len([x / delta_x for x in range(a * delta_x, (b - delta_x) * delta_x)]) - 1: simpson_list.append(function(x))
            elif index % 2 == 0: simpson_list.append(2 * function(x))
            else: simpson_list.append(4 * function(x))
        return (delta_x / 3) * sum(simpson_list)