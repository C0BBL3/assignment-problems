import matplotlib.pyplot as plt
from riemann_sum import riemann_sum
import math

standard_normal_distribution_function = lambda x: 1 / math.sqrt(2 * math.pi) * math.e ** (-x ** 2 / 2)

def calc_standard_normal_probability(a,b,n,rule):
    return riemann_sum(standard_normal_distribution_function, a, b, (b-a)/n, rule)

left = [calc_standard_normal_probability(0,1,n,'left endpoint') for n in range(2,101,2)]
right = [calc_standard_normal_probability(0,1,n,'right endpoint') for n in range(2,101,2)]
mid = [calc_standard_normal_probability(0,1,n,'midpoint') for n in range(2,101,2)]
trap = [calc_standard_normal_probability(0,1,n,'trapezoidal') for n in range(2,101,2)]
simp = [calc_standard_normal_probability(0,1,n,'simpson') for n in range(2,101,2)]
'''
plt.plot([calc_standard_normal_probability(0,1,n,'left endpoint') for n in range(2,101,2)], linewidth=2.5)
plt.plot([calc_standard_normal_probability(0,1,n,'right endpoint') for n in range(2,101,2)], linewidth=2.5)
plt.plot([calc_standard_normal_probability(0,1,n,'midpoint') for n in range(2,101,2)], linewidth=2.5)
plt.plot([calc_standard_normal_probability(0,1,n,'trapezoidal') for n in range(2,101,2)], linewidth=2.5)
plt.plot([calc_standard_normal_probability(0,1,n,'simpson') for n in range(2,101,2)], linewidth=2.5)
plt.plot([0.34 for n in range(2,101)], linewidth=5)
plt.legend(['left', 'right', 'midpoint', 'trapezoidal', 'simpson'])
plt.ylabel('P(0<=x<=1)')
plt.xlabel('n')
plt.savefig('plot.png')
plt.show()'''