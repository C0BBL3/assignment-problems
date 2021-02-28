array = [[], [], [], [], []] # has 5 empty "buckets"

class HashTable:
    def __init__(self, num_buckets , hash_string = 'abcdefghijklmnopqrstuvwxyz'):
        self.buckets = [[] for _ in range(num_buckets)]
        self.hash_string = hash_string

    def hash_function(self, string):
        return sum((self.hash_string.index(char) for char in string)) % len(self.buckets)

    def insert(self, key, value):
        index = self.hash_function(key)
        self.buckets[index].append((key, value))

    def find(self, key):
        return next((element[1] for tuplee in self.buckets for element in tuplee if element[0] == key))

print('\nTesting...\n')

print("    Testing Hash Tables's Alphabet Hashing")

hash_table = HashTable(5)

for i, char in enumerate('abcdefghijklmnopqrstuvwxyz'):
    key = 'someletters'+char
    value = [i, i**2, i**3]
    hash_table.insert(key, value)

for i, char in enumerate('abcdefghijklmnopqrstuvwxyz'):
    key = 'someletters'+char
    output_value = hash_table.find(key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value, "Hash Tables's Alphabet Hashing was not right, it should be {}, but was {}".format(desired_value, output_value)

print("    Hash Tables's Alphabet Hashing Passed!!!\n")

print('----------------------------------------------------------------\n')

print("    Testing Hash Tables's Vegtable Hashing\n")

hash_table = HashTable(3)

print("    Testing Hash Table's buckets")
assert hash_table.buckets == [[], [], []], "Hash Table's buckets was not right, it should be [[], [], []], but was {}".format(hash_table.buckets)
print("    Hash Table's buckets Passed!!!\n")

print("    Testing Hash Table's hash_function()")
assert hash_table.hash_function('cabbage') == 2, "Hash Table's hash_function() was not right, it should be 2, but was {}".format(hash_table.hash_function('cabbage'))
print("    Hash Table's hash_function() Passed!!!\n")

hash_table.insert('cabbage', 5)

print("    Testing Hash Table's insert()")
assert hash_table.buckets == [[], [], [('cabbage',5)]], "Hash Table's buckets was not right, it should be [[], [], [('cabbage',5)]], but was {}".format(hash_table.buckets)
print("    Hash Table's insert() Passed!!!\n")


hash_table.insert('cab', 20)

print("    Testing Hash Table's insert()")
assert hash_table.buckets == [[('cab', 20)], [], [('cabbage',5)]], "Hash Table's buckets was not right, it should be [[('cab', 20)], [], [('cabbage',5)]], but was {}".format(hash_table.buckets)
print("    Hash Table's insert() Passed!!!\n")

hash_table.insert('c', 17)

print("    Testing Hash Table's insert()")
assert hash_table.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17)]], "Hash Table's buckets was not right, it should be [[('cab', 20)], [], [('cabbage',5), ('c',17)]], but was {}".format(hash_table.buckets)
print("    Hash Table's insert() Passed!!!\n")

hash_table.insert('ac', 21)

print("    Testing Hash Table's insert()")
assert hash_table.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17), ('ac', 21)]], "Hash Table's buckets was not right, it should be [[('cab', 20)], [], [('cabbage',5), ('c',17), ('ac', 21)]], but was {}".format(hash_table.buckets)
print("    Hash Table's insert() Passed!!!\n")

print("    Testing Hash Table's find()")
assert hash_table.find('cabbage') == 5, "Hash Table's buckets was not right, it should be 5, but was {}".format(hash_table.find('cabbage'))
print("    Hash Table's find() Passed!!!\n")

print("    Testing Hash Table's find()")
assert hash_table.find('cab') == 20, "Hash Table's buckets was not right, it should be 5, but was {}".format(hash_table.find('cab'))
print("    Hash Table's find() Passed!!!\n")

print("    Testing Hash Table's find()")
assert hash_table.find('c') == 17, "Hash Table's buckets was not right, it should be 5, but was {}".format(hash_table.find('c'))
print("    Hash Table's find() Passed!!!\n")

print("    Testing Hash Table's find()")
assert hash_table.find('ac') == 21, "Hash Table's buckets was not right, it should be 5, but was {}".format(hash_table.find('ac'))
print("    Hash Table's find() Passed!!!\n")

print("    Hash Tables's Alphabet Vegtable Hashing Passed!!!\n")

print('----------------------------------------------------------------\n')

print('ALL TESTS PASS!!!!!')

