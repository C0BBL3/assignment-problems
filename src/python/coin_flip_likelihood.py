import matplotlib.pyplot as plt

def probability_likelihood(heads_count, tails_count, probability=None):
    if probability != None:
        return round((probability ** heads_count) * (1 - probability)**tails_count, 5)
    else:
        return 'L(p) = p ^ ' + str(heads_count) + ' * 1-p ^ ' + str(tails_count)
    

print('L(p = 0.5 | HHTTH) =', probability_likelihood(3, 2, probability=0.5))  # 0.5 ^ 3 * 0.5 ^ 2 = 0.03125 | 3 + 1 + 2 + 5 = 11 | this works

print('L(p = 0.55 | HHTTH) =', probability_likelihood(3, 2, probability=0.55))  # 0.55 ^ 3 * 0.45^2 = 0.03369 | 3 + 3 + 6 + 9 = 21 | this works

print('L(p | HHTTH) =>', probability_likelihood(3, 2))  # L(p) = p ^ 3 * p ^ 2

range_of_numbers = [x / 100 for x in range(0, 101)]

plt.style.use('bmh')
plt.plot([probability_likelihood(3, 2, i) for i in range_of_numbers])
plt.legend(['Predicted y-values'])
plt.ylabel('Likelihood')
plt.xlabel('Probability')
plt.title('Likelihood vs Probability')
plt.savefig('coin-flip-likelihood.png')
plt.show()
