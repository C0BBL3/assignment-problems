import math

def calc_standard_normal_probability(a, b):
    arr = []
    for x in [x / 1000 for x in range(a * 1000, b * 1000)]:
        arr.append(1 / math.sqrt(2 * math.pi) * math.e ** (-x ** 2 / 2) * 0.001)
    return sum(arr)#[1 / math.sqrt(2 * math.pi) * math.e ^ (-x ^ 2 / 2) * 0.001 for x in range(a, b, 0.001)]

print('P(−1 <= x <= 1) =', calc_standard_normal_probability(-1, 1))
print('P(−2 <= x <= 2) =', calc_standard_normal_probability(-2, 2))
print('P(−3 <= x< = 3) =', calc_standard_normal_probability(-3, 3))