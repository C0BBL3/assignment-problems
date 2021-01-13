def riemann_sum(function, a, b, n, rule):

    delta_x = (b-a)/n

    def range_a_b(a,b,start,n,delta_x):
        arr = []
        for x in range(0, n):
            arr.append(a + x * delta_x)
        return arr

    range_a_b_ = range_a_b(a,b,0,n+1,delta_x)
    
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
            result += function(x / 2 + range_a_b_[index+1] / 2)
        return delta_x * result

    if rule == 'trapezoidal':
        result = 0
        for x in range_a_b_[1:-1]:
            result += function(x)
        return delta_x * (function(a) / 2 + result + function(b) / 2)

    if rule == 'simpson':
        result = 0
        for index, x in enumerate(range_a_b_[1:-1]):
            if (index+1) % 2 == 0: 
                result += function(x) * 2
                continue
            elif (index+1)  % 2 != 0: 
                result += function(x) * 4
                continue
        return (delta_x / 3) * (function(a) + result + function(b))