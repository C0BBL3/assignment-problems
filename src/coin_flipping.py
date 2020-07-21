import math
import random

def probability(num_heads, num_flips):
    return (math.factorial(num_flips) / (math.factorial(num_heads) * math.factorial(num_flips - num_heads))) / 2 ** num_flips

def monte_carlo_probability(num_heads, num_flips):
    flips = []
    heads = 0
    for i in range(0, 1000):
        flips.append([])
        for _ in range(num_flips):
            flips[i].append(random.randint(0,1))

    for arr in flips:
        if sum(arr) == num_heads:
            heads += 1
            
    return heads / 1000
