import random

def random_draw(distribution):
    cumulative_distribution = [sum(distribution[:index + 1]) for index in range(len(distribution))]
    random_number = random.randint(0,1)
    for index, number in enumerate(cumulative_distribution):
        if random_number > number: continue
        return index

    
print(random_draw([0.5, 0.5]))
print(random_draw([0.25, 0.25, 0.5]))
print(random_draw([0.05, 0.2, 0.15, 0.3, 0.1, 0.2]))
