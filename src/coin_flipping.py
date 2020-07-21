import math

def probability(num_heads, num_flips):
    return (math.factorial(num_flips) / (math.factorial(num_heads) * math.factorial(num_flips - num_heads))) / 2 ** num_flips

def monte_carlo_probability(num_heads, num_flips):
