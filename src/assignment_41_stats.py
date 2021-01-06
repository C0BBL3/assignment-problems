def p(k):
    return k ** -4 if k>=68 else 0

def sum_for_problem_2(x):
    return sum([p(k) for k in range(1, x)])

c =  1 / sum_for_problem_2(10000000)
print('c = ', c)

#def sum_for_problem_5(x):
#    return sum([c * p(k) for k in range(25, 31)])

#print('There is a ', sum_for_problem_5(1000000), 'percent chance that k is lower than 30 and greater than 25.')

def sum_for_problem_6():
    value, k = 0, 68
    while value < .95:
        value += c * p(k)
        k += 1
    return k, value


print('I am', sum_for_problem_6()[1] * 100, 'percent sure that k is below', sum_for_problem_6()[0] )
