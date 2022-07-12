# hash map/hash table are internal data structure and dictionary is the python specific implementation of hash table

# in list we use number indexes , in dictionary we use string/number as indexes, internally dictionary stores data as list but
# there is a hash function which convert the string(index) to a number which we can use as a index to find data from the list(which is the underlaying data structure)

# the main moto in hashTable/dictionary is that using string as an index is more meaningfull for humans rather than just a number

''' https://docs.python.org/3/library/operator.html '''


def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100  # assuming 100 is the size of the list


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
t['one'] = 1
print(t['one'])
del t['one']
print(t['one'])
