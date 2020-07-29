import math
import random

def probability(num_heads, num_flips):
    return (factorial(num_flips) / (factorial(num_heads) * factorial(num_flips - num_heads))) / 2 ** num_flips

def monte_carlo_probability(num_heads, num_flips, return_num_head = False):
    return sum([random.randint(0, 1) for _ in range(num_flips)]) / 10

def factorial(num):
    result = 1
    
    for val in range(num, 0, -1):
        result *= val

    return result
    
