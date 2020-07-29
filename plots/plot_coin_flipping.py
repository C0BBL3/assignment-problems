
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
from coin_flipping import probability, monte_carlo_probability
plt.style.use('bmh')
plt.plot([i for i in range(0, 11)], [probability(i, 10) for i in range(0,11)], linewidth=2.5)
plt.plot([i for i in range(0, 11)], [monte_carlo_probability(i, 10) for i in range(0,11)], linewidth=0.75)
plt.plot([i for i in range(0, 11)], [monte_carlo_probability(i, 10) for i in range(0,11)], linewidth=0.75)
plt.plot([i for i in range(0, 11)], [monte_carlo_probability(i, 10) for i in range(0,11)], linewidth=0.75)
plt.plot([i for i in range(0, 11)], [monte_carlo_probability(i, 10) for i in range(0,11)], linewidth=0.75)
plt.plot([i for i in range(0, 11)], [monte_carlo_probability(i, 10) for i in range(0,11)], linewidth=0.75)
plt.legend(['P(x)', 'MC #1', 'MC #2', 'MC #3', 'MC #4', 'MC #5'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('Graph of P(x)')
plt.savefig('plot.png')
plt.show()