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
    count_prev_and_next = [flip_sequence.count(prev_flip+next_flip) for person, flip_sequence in dictionary.items()]
    count_prev = [flip_sequence.count(str(prev_flip) + 'H') + flip_sequence.count(str(prev_flip) + 'T') for person, flip_sequence in dictionary.items()]
    return [count_prev_and_next[i] / count_prev[i] for i in range(0, len(count_prev_and_next))]

print('debugging')
result_string = ''.join(['test' + ': ' + str(round(probability_prev_next('T', 'H', test)[list(test.keys()).index(person)], 3)) + str(round(probability_prev_next('H', 'T', test)[list(test.keys()).index(person)], 3)) + ' ' for person, flip_sequence in test.items()])
print('    test', result_string)

print('\nFor each person, following probabilities for each function are...')
result_string = ''.join([str(person) + ': ' + str(round(probability_prev_next('H', 'H', flips)[list(flips.keys()).index(person)], 3)) + ' ' for person, flip_sequence in flips.items()])
print('    P(next flip was heads | previous flip was heads):', result_string)

result_string = ''.join([str(person) + ': ' + str(round(probability_prev_next('T', 'H', flips)[list(flips.keys()).index(person)], 3)) + ' ' for person, flip_sequence in flips.items()])
print('    P(next flip was tails | previous flip was heads):', result_string)

result_string = ''.join([str(person) + ': ' + str(round(probability_prev_next('H', 'T', flips)[list(flips.keys()).index(person)], 3)) + ' ' for person, flip_sequence in flips.items()])
print('    P(next flip was heads | previous flip was tails):', result_string)

result_string = ''.join([str(person) + ': ' + str(round(probability_prev_next('T', 'T', flips)[list(flips.keys()).index(person)], 3)) + ' ' for person, flip_sequence in flips.items()])
print('    P(next flip was tails | previous flip was tails):', result_string)
print('\n')
