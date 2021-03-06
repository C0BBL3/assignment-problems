import math
from coin_flipping import monte_carlo_probability, probability, count_samples


def make_p_and_q(samples):
    return count_samples(samples, 5), [probability(i, 5) for i in range(0, 6)]

p_1, q_1 = make_p_and_q(100)
p_2, q_2 = make_p_and_q(1000)
p_3, q_3 = make_p_and_q(10000)

def kl_divergence(p, q):
    return sum([p[x] * math.log(p[x] / q[x]) if p[x] != 0 and q[x] != 0 else 0 for x in range(0, len(p)) if p[x] != 0 and q[x] != 0])

#
#print('Computing KL Divergence for MC Simulations...')
#print('100 samples --> KL Divergence = {}'.format(kl_divergence(p_1, q_1)))
#print('1000 samples --> KL Divergence = {}'.format(kl_divergence(p_2, q_2)))
#print('10000 samples --> KL Divergence = {}'.format(kl_divergence(p_3, q_3)))

# As the number of samples increases, the KL divergence converges to 0 because the more samples
# there are the more accurate the monte carlo simulation gets and therefore the closer in resembelance
# monte carlo distribution gets to the true distribution.
