import math
import random

def probability(num_heads, num_flips):
    return (factorial(num_flips) / (factorial(num_heads) * factorial(num_flips - num_heads))) / 2 ** num_flips

def monte_carlo_probability(num_heads, num_flips, num_trials = 1000, return_heads = False):
    flips = []
    heads = 0
    for i in range(0, num_trials):
        flips.append([])
        for _ in range(num_flips):
            flips[i].append(random.randint(0,1))

    for arr in flips:
        if sum(arr) == num_heads:
            heads += 1
            
    return heads / num_trials


def generate_sample(num_flips):
    return sum([random.randint(0, 1) for _ in range(0, num_flips)])

def count_samples(num_samples, num_flips):
    generated_samples = [generate_sample(num_flips) for _ in range(0, num_samples)]
    return [generated_samples.count(i) / num_samples for i in range(0, num_flips + 1)]


def factorial(num):
    result = 1
    
    for val in range(num, 0, -1):
        result *= val

    return result
    
