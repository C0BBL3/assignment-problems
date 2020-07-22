import sys
sys.path.append('src')
from coin_flipping import probability, monte_carlo_probability

print('probability', probability(5, 8))

print('monte_carlo_probability 1:', monte_carlo_probability(5, 8))
print('monte_carlo_probability 2:', monte_carlo_probability(5, 8))
print('monte_carlo_probability 3:', monte_carlo_probability(5, 8))

