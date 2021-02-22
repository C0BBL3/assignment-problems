array = [[], [], [], [], []] # has 5 empty "buckets"

def hash_function(string, hash_string = 'abcdefghijklmnopqrstuvwxyz'):
    return sum((hash_string.index(char) for char in string)) % len(array)

def insert(array, key, value):
    index = hash_function(key)
    array[index].append((key, value))

def find(array, key):
    return next((element[1] for tuplee in array for element in tuplee if element[0] == key))

print('\nTesting...\n')

print("    Testing Hash Tables's Alphabet Hashing")

for i, char in enumerate('abcdefghijklmnopqrstuvwxyz'):
    key = 'someletters'+char
    value = [i, i**2, i**3]
    insert(array, key, value)

for i, char in enumerate('abcdefghijklmnopqrstuvwxyz'):
    key = 'someletters'+char
    output_value = find(array, key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value, "Hash Tables's Alphabet Hashing was not right, it should be {}, but was {}".format(desired_value, output_value)

print("    Hash Tables's Alphabet Hashing Passed!!!\n")

print('ALL TESTS PASS!!!!!')

