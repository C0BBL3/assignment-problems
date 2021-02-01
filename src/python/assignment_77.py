import math

def calc_standard_normal_probability(a, b, delta_x):
    arr = []
    for x in [x * delta_x for x in range(int(a / delta_x), int(b / delta_x))]:
        arr.append(1 / math.sqrt(2 * math.pi) * math.e ** (-x ** 2 / 2) * delta_x)
    return sum(arr)#[1 / math.sqrt(2 * math.pi) * math.e ^ (-x ^ 2 / 2) * 0.001 for x in range(a, b, 0.001)]

print('P(−1 <= x <= 1) =', calc_standard_normal_probability(-1, 1, 0.001))
print('P(−2 <= x <= 2) =', calc_standard_normal_probability(-2, 2, 0.001))
print('P(−3 <= x< = 3) =', calc_standard_normal_probability(-3, 3, 0.001))