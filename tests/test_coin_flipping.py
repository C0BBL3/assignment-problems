import sys
sys.path.append('src')
from coin_flipping import probability, monte_carlo_probability

print('probability', probability(5, 8))

print('monte_carlo_probability', monte_carlo_probability(5, 8))

