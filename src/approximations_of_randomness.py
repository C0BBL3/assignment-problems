from coin_flipping import probability
from divide_and_conquer_sort import divide_and_conquer_sort
from kl_divergence_for_monte_carlo_simulations import kl_divergence
print('hello1')
def order_flip_sequence(flip_sequence):
    print('hello4.1')
    list_flip_sequence = flip_sequence.split(' ')
    print('hello4.2')
    new_list_flip_sequence = []
    for flips in list_flip_sequence:
        print('hello4.3')
        new_list_flip_sequence.append(flips.count('H'))
    print('hello4.5')
    new_list_flip_sequence.sort()
    return new_list_flip_sequence #make it so the number of heads is ordered
print('hello2') 


flips = {
    'George': 'THTH HTHT THTH HHTH THTH TTHT THTH TTTH THTH TTHT THHT HTTH THTH THHT THHT THTH THTH THHT THTH THTH',
    'David': 'TTHH HHTT HHTT TTHH HTHT THTH THTH THTH HTHT HTHT THTH HTHT THHH THTH HHTT HHTT TTTH HHTH HTHH TTTH',
    'Elijah': 'THTT HTHT HTHH HHHT TTHH THHH TTTT HHTT TTTH TTHH HTHT HTHT TTTT HTTT TTTH HTTT TTHH THTH THHH HTHH',
    'Colby': 'HTTH HTHH THTT HHTH TTHT HTTT THHH TTHH HHTT THTH HHTT THTH THHH TTHH THTT HHTH HTTH HTHH TTHT HTTT',
    'Justin': 'THTT HTHT TTTH THHT HTHH TTTH THTH HHTH TTTT HTTH HHTT THHH HHHH THTH HTTH TTHH HTHT HHHT THHT TTTH'
}
print('hello3')
ordered_flip_sequence = []
ordered_random_flip_sequence = []
ordered_true_distribution_flip_sequence = []
i = 0

for person, flip_sequence in flips.items():
    ordered_random_flip_sequence.append([])
    print('hello4')
    ordered_flip_sequence = order_flip_sequence(flip_sequence)
    print('ordered_flip_sequence', ordered_flip_sequence)
    print('hello4.5')
    for j in range(0, 5):
        print('hello5', j)
        ordered_random_flip_sequence[i].append(ordered_flip_sequence.count(j))
        print('ordered_random_flip_sequence', ordered_random_flip_sequence)

    i += 1

print('hello6')
#print('ordered_random_flip_sequence', ordered_random_flip_sequence)
# more for future plotting thats why its ordered
diverged_flip_seqences = [kl_divergence(ordered_random_flip_sequence[i], [probability(j, 5) for j in range(0, 5)]) for i in range(0, 5)]

print('Divergence')
print("    George's samples divergence", diverged_flip_seqences[0])
print("    David's samples divergence", diverged_flip_seqences[1])
print("    Elijah's samples divergence", diverged_flip_seqences[2])
print("    Colby's samples divergence", diverged_flip_seqences[3])
print("    Justin's samples divergence", diverged_flip_seqences[4])
print('\n')

if diverged_flip_seqences.index(min(diverged_flip_seqences)) == 0:
    print("    George's samples were the closest to true distribution at a KL Divergence of:", min(diverged_flip_seqences))
if diverged_flip_seqences.index(min(diverged_flip_seqences)) == 1:
    print("    David's samples were the closest to true distribution at a KL Divergence of:", min(diverged_flip_seqences))
if diverged_flip_seqences.index(min(diverged_flip_seqences)) == 2:
    print("    Elijah's samples were the closest to true distribution at a KL Divergence of:", min(diverged_flip_seqences))
if diverged_flip_seqences.index(min(diverged_flip_seqences)) == 3:
    print("    Colby's samples were the closest to true distribution at a KL Divergence of:", min(diverged_flip_seqences))
if diverged_flip_seqences.index(min(diverged_flip_seqences)) == 4:
    print("    Justin's samples were the closest to true distribution at a KL Divergence of:", min(diverged_flip_seqences))

