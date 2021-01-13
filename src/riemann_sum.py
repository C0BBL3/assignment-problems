def riemann_sum(function, a, b, delta_x, rule):

    def range_a_b(a,b,delta_x):
        print('a', a)
        print('b', b)
        print('delta_x', delta_x)
        print('int(a / delta_x)', int(a / delta_x))
        print('int(b / delta_x)', int((b+delta_x) / delta_x))
        arr = []
        for x in range(int(a / delta_x), int((b+delta_x) / delta_x)):
            arr.append(x * delta_x)
        return arr

    range_a_b_ = range_a_b(a,b,delta_x)
    print(range_a_b_)

    if rule == 'left endpoint':
        result = 0
        for x in range_a_b_[:-1]:
            result += function(x)
        return delta_x * result

    if rule == 'right endpoint':
        result = 0
        for x in range_a_b_[1:]:
            result += function(x)
        return delta_x * result

    if rule == 'midpoint':
        result = 0
        for index, x in enumerate(range_a_b_[:-1]):
            result += function((range_a_b_[index+1]+x)/2)
        return delta_x * result

    if rule == 'trapezoidal':
        result = 0
        for index, x in enumerate(range_a_b_):
            if index == 0 or index == len(range_a_b_) - 1:
                result += function(x) / 2
            else:
                result += function(x)
        return delta_x * result

    if rule == 'simpson':
        result = 0
        for index, x in enumerate(range_a_b_):
            if index == 0 or index == len(range_a_b_) - 1:
                result += function(x)
                continue
            elif index % 2 == 0: 
                result += function(x) * 2
                continue
            elif index % 2 != 0: 
                result += function(x) * 4
                continue
        return (delta_x / 3) * result

import math

print(riemann_sum(lambda x: 1 / math.sqrt(2 * math.pi) * math.e ** (-x ** 2 / 2), 0, 1, 1/2, 'midpoint'))