def p(k):
    return k ** -5 if not 0 < k < 25 else 0

def sum_for_problem_2(x):
    return sum([p(k) for k in range(1, x)])

print('c = ', 1 / sum_for_problem_2(1000000))

def sum_for_problem_5(x):
    return sum([1443199.7831770328 * p(k) for k in range(25, 31)])

print('There is a ', sum_for_problem_5(1000000), 'percent chance that k is lower than 30 and greater than 25.')

def sum_for_problem_6():
    value, k = 0, 25
    while value < .95:
        value += 1443199.7831770328 * p(k)
        k += 1
    return k, value


print('I am', sum_for_problem_6()[1] * 100, 'percent sure that k is below', sum_for_problem_6()[0] )
