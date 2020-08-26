import math
from coin_flipping import probability

probabilities = [probability(i, 4) for i in range(0, 5)]

def expected_value(X, num_flips=4):
    return sum([x * X[x] for x in range(0, num_flips + 1)])

def variance(X, num_flips=4):
    return sum([((x - expected_value(X)) ** 2) * X[x] for x in range(0, num_flips + 1)])

def st_dev(X):
    return math.sqrt(variance(X))

def probability_likelihood(heads_count, tails_count, probability=None):
    if probability != None:
        return round((probability ** heads_count) * (1 - probability)**tails_count, 5)
    else:
        return 'L(p) = p ^ ' + str(heads_count) + ' * 1-p ^ ' + str(tails_count)

print('\nQuestion A.1: 0 Heads:', probabilities[0], '1 Head:', probabilities[1], '2 Heads:', probabilities[2], '3 Heads:', probabilities[3], '4 Heads:', probabilities[4])  # num_flips! / num_heads! * (num_flips - num_heads)! / 2 ** num_flips

print('Question A.2: X would be 2 heads out of 4 flips because an unbiased coin would be HTHT or THTH, and both have 2 heads, therefore X would be 2.')  # 4 * 0.5 = 2

print('Question A.3:', expected_value(probabilities))  # E x*p(x) = 2

print('Question A.4:', variance([i for i in range(0, 5)]))  # E (X-X¯)^2 = 1

print('Question A.5:', st_dev([i for i in range(0, 5)]), '\n') # Sqrt(1) = 1

biased_probabilities = [probability_likelihood(i, 4 - i) for i in range(0, 5)]

print('biased_probabilities', biased_probabilities)

print('\nQuestion B.1: 0 Heads:', biased_probabilities[0], '1 Head:', biased_probabilities[1], '2 Heads:', biased_probabilities[2], '3 Heads:', biased_probabilities[3], '4 Heads:', biased_probabilities[4])  # num_flips! / num_heads! * (num_flips - num_heads)! / 2 ** num_flips

print('Question B.2: Y would be Lamba * 4 heads out of 4 flips.')

print('Question B.3: E(Lambda) = (((Y[0]-2) ^ 2) * Lambda ^ 4) + (((Y[1]-2) ^ 2) * Lambda ^ 3) + (((Y[2]-2) ^ 2) * Lambda ^ 2) + (((Y[3]-2) ^ 2) * Lambda ^ 3) + (((Y[4]-2) ^ 2) * Lambda ^ 4)')

print('Question B.4: V(Lambda) = (((0 - E(Lambda)) ^ 2) * Lambda ^ 4) + (((1 - E(Lambda)) ^ 2) * Lambda ^ 3) + (((2 - E(Lambda)) ^ 2) * Lambda ^ 2) + (((3 - E(Lambda)) ^ 2) * Lambda ^ 3) + (((4 - E(Lambda)) ^ 2) * Lambda ^ 4)')

print('Question B.5: Sqrt(V(Lambda))\n')

