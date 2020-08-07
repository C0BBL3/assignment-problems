from coin_flipping import probability
from divide_and_conquer_sort import divide_and_conquer_sort
from kl_divergence_for_monte_carlo_simulations import kl_divergence

flips = {
    'George': 'THTH HTHT THTH HHTH THTH TTHT THTH TTTH THTH TTHT THHT HTTH THTH THHT THHT THTH THTH THHT THTH THTH',
    'David': 'TTHH HHTT HHTT TTHH HTHT THTH THTH THTH HTHT HTHT THTH HTHT THHH THTH HHTT HHTT TTTH HHTH HTHH TTTH',
    'Elijah': 'THTT HTHT HTHH HHHT TTHH THHH TTTT HHTT TTTH TTHH HTHT HTHT TTTT HTTT TTTH HTTT TTHH THTH THHH HTHH',
    'Colby': 'HTTH HTHH THTT HHTH TTHT HTTT THHH TTHH HHTT THTH HHTT THTH THHH TTHH THTT HHTH HTTH HTHH TTHT HTTT',
    'Justin': 'THTT HTHT TTTH THHT HTHH TTTH THTH HHTH TTTT HTTH HHTT THHH HHHH THTH HTTH TTHH HTHT HHHT THHT TTTH'
}

test = {
    'test': 'HHTTHT'
}


def probability_prev_next(next_flip, prev_flip, dictionary):
    result = []
    for _, flip_sequence in dictionary.items():
        result.append(conditional_probability(next_flip, prev_flip, flip_sequence))

    return result


def conditional_probability(next_flip, prev_flip, flip_sequence):
    print('flip_sequence', flip_sequence)
    count_prev_and_next = count(prev_flip + next_flip, flip_sequence)
    print('count_prev_and_next', count_prev_and_next)

    count_prev = count(prev_flip + 'H', flip_sequence) + count(prev_flip + 'T', flip_sequence)
    print("prev_flip) + 'H'", prev_flip + 'H')
    print("count(prev_flip + 'H', flip_sequence)", count(prev_flip + 'H', flip_sequence))
    print("prev_flip) + 'T'", prev_flip + 'T')
    print("count(prev_flip + 'T', flip_sequence)", count(prev_flip + 'T', flip_sequence))

    return count_prev_and_next / count_prev

def count(string, flip_sequence):
    result = 0
    for i in range(0, len(flip_sequence) - 1):
        if flip_sequence[i] + flip_sequence[i + 1] == string:
            result += 1

    return result

def make_result_string(next, prev, dictionary):
    return ''.join([str(person) + ': ' + str(round(probability_prev_next(next, prev, dictionary)[list(dictionary.keys()).index(person)], 3)) + ' ' for person, flip_sequence in dictionary.items()])

print('"fail case"')
print(conditional_probability('T', 'T', 'TTTTTTTHTHH'))

print('debugging')
print('\nFor each Test, following probabilities for each function are...')
result_string = make_result_string('H', 'H', test)
print('    P(next flip was heads | previous flip was heads):', result_string)

result_string = make_result_string('T', 'H', test)
print('    P(next flip was tails | previous flip was heads):', result_string)

result_string = make_result_string('H', 'T', test)
print('    P(next flip was heads | previous flip was tails):', result_string)

result_string = make_result_string('T', 'T', test)
print('    P(next flip was tails | previous flip was tails):', result_string)
print('\n')

print('\nFor each person, following probabilities for each function are...')
result_string = make_result_string('H', 'H', flips)
print('    P(next flip was heads | previous flip was heads):', result_string)

result_string = make_result_string('T', 'H', flips)
print('    P(next flip was tails | previous flip was heads):', result_string)

result_string = make_result_string('H', 'T', flips)
print('    P(next flip was heads | previous flip was tails):', result_string)

result_string = make_result_string('T', 'T', flips)
print('    P(next flip was tails | previous flip was tails):', result_string)
print('\n')
