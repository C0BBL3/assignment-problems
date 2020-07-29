import math
from coin_flipping import monte_carlo_probability, probability


def make_p_and_q(samples):
    return [sum([monte_carlo_probability(j, 5) for j in range(0, 5)]) for i in range(0, samples)], [sum([probability(j, 5) for j in range(0, 5)]) for i in range(0, samples)]

p_1, q_1 = make_p_and_q(100)
p_2, q_2 = make_p_and_q(1000)
p_3, q_3 = make_p_and_q(10000)

def kl_divergence(p, q):
    if len(p) == len(q):
        return sum([p[x] * math.log(p[x] / q[x]) for x in range(0, len(p))])


print('Computing KL Divergence for MC Simulations...')
print('100 samples --> KL Divergence = {}'.format(kl_divergence(p_1, q_1)))
print('1000 samples --> KL Divergence = {}'.format(kl_divergence(p_2, q_2)))
print('10000 samples --> KL Divergence = {}'.format(kl_divergence(p_3, q_3)))

# As the number of samples increases, the KL divergence converges to 0 because the more samples
# there are the more accurate the monte carlo simulation gets and therefore the closer in resembelance
# monte carlo distribution gets to the true distribution.
